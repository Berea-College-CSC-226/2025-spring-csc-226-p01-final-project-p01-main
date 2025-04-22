from inspect import getframeinfo, stack
from finalcode import Planet, Rocket


def unittest(did_pass):
    """
    Print the result of a unit test.
    :param did_pass: a boolean representing the test
    :return: None
    """

    caller = getframeinfo(stack()[1][0])
    linenum = caller.lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def genomics_test_suite():
    venus = Planet("Venus", "Second planet from the Sun.", 200, 260)
    mercury = Planet("Mercury", "Closest to the Sun.", 265, 305)
    earth = Planet("Earth", "Our home planet.", 340, 380)
    mars = Planet("Mars", "The Red Planet.", 430, 460)
    jupiter = Planet("Jupiter", "The largest planet.", 470, 560)
    saturn = Planet("Saturn", "Famous for its rings.", 600, 670)
    uranus = Planet("Uranus", "Has a tilted rotation.", 710, 770)
    neptune = Planet("Neptune", "Furthest from the Sun.", 790, 860)

    # Testing Venus
    unittest(venus.is_hit(200) == True)
    unittest(venus.is_hit(220) == True)
    unittest(venus.is_hit(240) == True)
    unittest(venus.is_hit(260) == True)
    unittest(venus.is_hit(280) == False)

    # Testing Mercury
    unittest(mercury.is_hit(280) == True)
    unittest(mercury.is_hit(300) == True)
    unittest(mercury.is_hit(305) == True)
    unittest(mercury.is_hit(265) == True)
    unittest(mercury.is_hit(260) == False)

    # Testing Earth
    unittest(earth.is_hit(340) == True)
    unittest(earth.is_hit(360) == True)
    unittest(earth.is_hit(380) == True)
    unittest(earth.is_hit(339) == False)

    # Testing Mars
    unittest(mars.is_hit(430) == True)
    unittest(mars.is_hit(445) == True)
    unittest(mars.is_hit(460) == True)
    unittest(mars.is_hit(461) == False)

    # Testing Jupiter
    unittest(jupiter.is_hit(470) == True)
    unittest(jupiter.is_hit(500) == True)
    unittest(jupiter.is_hit(560) == True)
    unittest(jupiter.is_hit(561) == False)

    # Testing Saturn
    unittest(saturn.is_hit(600) == True)
    unittest(saturn.is_hit(635) == True)
    unittest(saturn.is_hit(670) == True)
    unittest(saturn.is_hit(680) == False)

    # Testing Uranus
    unittest(uranus.is_hit(710) == True)
    unittest(uranus.is_hit(740) == True)
    unittest(uranus.is_hit(770) == True)
    unittest(uranus.is_hit(709) == False)

    # Testing Neptune
    unittest(neptune.is_hit(790) == True)
    unittest(neptune.is_hit(825) == True)
    unittest(neptune.is_hit(860) == True)
    unittest(neptune.is_hit(861) == False)

    rocket = Rocket()
    planet_zones = [
        Planet("Venus", "Second planet from the Sun.", 200, 260),
        Planet("Mercury", "Closest to the Sun.", 265, 305),
        Planet("Earth", "Our home planet.", 340, 380),
        Planet("Mars", "The Red Planet.", 430, 460),
        Planet("Jupiter", "The largest planet.", 470, 560),
        Planet("Saturn", "Famous for its rings.", 600, 670),
        Planet("Uranus", "Has a tilted rotation.", 710, 770),
        Planet("Neptune", "Furthest from the Sun.", 790, 860),
    ]
    unittest(rocket.check_planet(planet_zones, testing=True) == venus)
    unittest(rocket.check_planet(planet_zones, testing=True) == mercury)
    unittest(rocket.check_planet(planet_zones, testing=True) == earth)
    unittest(rocket.check_planet(planet_zones, testing=True) == mars)
    unittest(rocket.check_planet(planet_zones, testing=True) == jupiter)
    unittest(rocket.check_planet(planet_zones, testing=True) == saturn)
    unittest(rocket.check_planet(planet_zones, testing=True) == uranus)
    unittest(rocket.check_planet(planet_zones, testing=True) == neptune)


    unittest(rocket.check_planet(planet_zones) == None)




def main():
    print('started')
    genomics_test_suite()


main()

