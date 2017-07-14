def areinstances(xs, t):
    return isinstance(xs, tuple) and all(isinstance(x, t) for x in xs)

def interleave(*xss):
    result = []
    xss = [list(xs) for xs in xss]
    indices = [0 for xs in xss]
    n = 0
    while True:
        if indices[n] >= len(xss[n]):
            break
        result.append(xss[n][indices[n]])
        indices[n] += 1
        n = (n + 1) % (len(xss))
    assert all(i == len(xs) for i, xs in zip(indices, xss))
    return result

def unweave(xs):
    result = ([], [])
    for i, x in enumerate(xs):
        result[i%2].append(x)
    return tuple(result[0]), tuple(result[1])

def clear_screen():
    print("\x1b[2J\x1b[H")

def elicit_input(observations, actions):
    clear_screen()
    lines = interleave(observations, [">>> {}".format(action) for action in actions])
    print("\n\n".join(lines))
    return raw_input("\n>>> ")
