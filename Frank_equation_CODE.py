# frank_equation.py
# Requires Python 3.8+
import hashlib
import math
import itertools
import random

def sha256_hex(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()

def hex_to_bits(hexstr: str) -> str:
    return bin(int(hexstr, 16))[2:].zfill(len(hexstr)*4)

def nth_hash(seed: str, n: int) -> str:
    """Compute s_n by iterating s_{k+1} = H(s_k || k) starting from s0 = H(seed)."""
    s = sha256_hex(seed.encode('utf-8'))
    if n == 0:
        return s
    for k in range(0, n):
        concat = bytes.fromhex(s) + str(k).encode('utf-8')
        s = sha256_hex(concat)
    return s

def extract_controls(s_hex: str, used_bits=0):
    """
    Return a dict with:
      - axis: 0->X,1->Y,2->Z
      - low_first: bool
      - permutation: list of indices 0..7 for ordering subcubes
    used_bits: how many bits already consumed (for chaining; default 0)
    """
    bits = hex_to_bits(s_hex)
    # grab first 3 bits for axis
    pos = used_bits
    axis_bits = bits[pos:pos+3]
    if len(axis_bits) < 3:
        raise ValueError("not enough bits")
    axis_val = int(axis_bits, 2) % 3   # pragmatic: map into {0,1,2}
    pos += 3

    # next bit decides low/high (pragmatic: use only 1 bit)
    low_high_bit = bits[pos]
    low_first = (low_high_bit == '0')
    pos += 1

    # use the following 16 bits (or as many left) as a seed integer for permutation
    seed_bits = bits[pos:pos+16]
    if len(seed_bits) == 0:
        seed_int = 0
    else:
        seed_int = int(seed_bits, 2)
    pos += len(seed_bits)

    # produce a deterministic permutation of 8 using the seed
    rng = random.Random(seed_int) #This ensure deterministic permutation based on the hash, emphasizing the cryptographic control.
    perm = list(range(8))
    rng.shuffle(perm)

    controls = {
        'axis': axis_val,            # 0=X,1=Y,2=Z
        'low_first': low_first,      # True if low side first
        'perm': perm,
        'bits_used': pos
    }
    return controls

def epsilon_approx(A_prev: int) -> int:
    """
    Use the approximation from the PDF:
      k_n = floor(log2(8*A_prev)) - floor(log2(A_prev))
      eps = floor(8*A_prev * 2^{-k_n})
    """
    if A_prev <= 0:
        return 0
    k_n = math.floor(math.log2(8 * A_prev)) - math.floor(math.log2(A_prev))
    eps = math.floor((8 * A_prev) * (2 ** (-k_n)))
    return int(eps)

def compute_sequence(seed_phrase: str, levels: int = 4):
    """
    Returns a list of dicts for n = 0..levels with Fn = (Cn, An, sn) metadata.
    We do not store full geometry Cn (would be large); we store controls/permutations.
    """
    results = []
    # s0 = H(seed_phrase)
    s0 = sha256_hex(seed_phrase.encode('utf-8'))
    A0 = 52
    results.append({'n':0, 's': s0, 'A': A0, 'controls': None})
    s = s0
    A = A0
    used_bits = 0
    for n in range(0, levels):
        # compute s_{n+1} = H(s_n || n)
        concat = bytes.fromhex(s) + str(n).encode('utf-8')
        s_next = sha256_hex(concat)
        # extract controls from s_next
        controls = extract_controls(s_next, used_bits=0)  # new level, start at 0
        # compute A_{n+1}
        eps = epsilon_approx(A)
        A_next = 8 * A - eps
        results.append({'n': n+1, 's': s_next, 'A': A_next, 'controls': controls, 'eps': eps})
        # iterate
        s = s_next
        A = A_next
    return results

if _name_ == "_main_":
    seed = "my secret dragon 123"
    seq = compute_sequence(seed, levels=5)
    for entry in seq:
        n = entry['n']
        print(f"n={n}, A={entry['A']}, s_prefix={entry['s'][:16]}...")
        if entry['controls'] is not None:
            c = entry['controls']
            axis_map = {0:'X',1:'Y',2:'Z'}

            print(f"  axis={axis_map[c['axis']]}, low_first={c['low_first']}, perm={c['perm']}, eps={entry.get('eps')}")
