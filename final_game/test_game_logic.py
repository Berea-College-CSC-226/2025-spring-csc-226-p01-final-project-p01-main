import unittest
from finalcode import Planet, Rocket, HEIGHT


class TestRocketGame(unittest.TestCase):

    def test_planet_hit_detection(self):
        # Create a test planet in a known range
        planet = Planet("Test", "Test planet", 100, 200)

        # Test different x positions
        self.assertTrue(planet.is_hit(150))  # Should be within range
        self.assertFalse(planet.is_hit(99))  # Should be outside range
        self.assertFalse(planet.is_hit(201))  # Should be outside range

    def test_planet_info(self):
        # Create a planet instance and check its info
        planet = Planet("Mars", "The Red Planet.", 400, 460)
        self.assertEqual(planet.get_info(), "Mars: The Red Planet.")

    def test_rocket_initialization_and_reset(self):
        # Initialize the rocket
        rocket = Rocket()

        # Check initial position and state
        self.assertEqual(rocket.x, 0)
        self.assertEqual(rocket.y, HEIGHT // 2 - 30)  # This should match the default y-value

        # Move the rocket and reset it
        rocket.x = 250
        rocket.reset()

        # Check if the rocket has reset to the starting position
        self.assertEqual(rocket.x, 0)
        self.assertIsNone(rocket.current_planet)

    def test_rocket_move_right(self):
        # Initialize the rocket
        rocket = Rocket()

        # Save the initial position
        initial_x = rocket.x

        # Move the rocket right by one step
        rocket.move_right()

        # Check if the rocket's x position increased by its speed
        self.assertEqual(rocket.x, initial_x + rocket.speed)

    def test_rocket_check_planet(self):
        # Initialize the rocket
        rocket = Rocket()

        # Set the rocket's x to land on Earth
        rocket.x = 310  # Earth zone

        # Check if the rocket detects the planet
        planet = rocket.check_planet()

        # Verify that Earth is detected
        self.assertIsNotNone(planet)
        self.assertEqual(planet.name, "Earth")


if __name__ == '__main__':
    unittest.main()


