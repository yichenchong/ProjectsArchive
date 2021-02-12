# ProjectileRocket

A quick script to simulate the physics of high-velocity projectile spacecraft launching mechanisms. I primarily used it to see if the numbers that SpinLaunch provided were feasible.

It is a bit more complicated than the projectile equations we usually use, because it accounts for both gravitational change as the projectile leaves the surface of the Earth, as well as the change in atmospheric density as it leaves the atmosphere (resulting in a change of drag).

As such, the script uses multivariable numeric integration techniques (I tried to solve the differential equation analytically, but the solution appears out of my reach, so I resorted to numerical techniques) to estimate the trajectory of such a projectile.

