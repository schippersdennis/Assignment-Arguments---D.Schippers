# Do not modify these lines
__winc_id__ = "7b9401ad7f544be2a23321292dd61cb6"
__human_name__ = "arguments"

# Add your code after this line

# Part 1: Greet Template.
def greet(name, greeting="Hello"):
    mod_greeting = (
        greeting[: greeting.find("<")] + name + greeting[greeting.find(">") + 1 :]
    )
    return f"{greeting}, {name}!" if greeting == "Hello" else mod_greeting


print(greet("Bob", "What's up, <name>!"))

# Part 2: Force.
def force(mass, body):
    body = body.lower()
    planets = {
        "sun": 274,
        "jupiter": 24.92,
        "neptune": 11.15,
        "saturn": 10.44,
        "earth": 9.798,
        "uranus": 8.87,
        "venus": 9.87,
        "mars": 3.71,
        "mercury": 3.7,
        "moon": 1.62,
        "pluto": 0.58,
    }

    force = mass * round(planets[body], 1)

    return f"F = {round(force, 2)} N"


print(force(mass=0.1, body="earth"))

# Part 3: Gravity.
def pull(m1, m2, d):
    G = 6.674 * 10e-11
    pull = G * ((m1 * m2) / d ** 2)
    return pull


print(pull(m1=800, m2=1500, d=3))
