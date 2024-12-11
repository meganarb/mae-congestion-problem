# M.A.E Congestion Problem

## Project Overview

The M.A.E Congestion Problem is a simulation project that explores traffic congestion as a collective action problem. The project focuses on the scenario where students commute to school, choosing between two transportation options: bus or car. This choice, when made by multiple individuals, leads to traffic issues due to limited road space.

Below are our different stages of our project presentations.
<h2>Project History</h2>
  <h3>1st Iteration:</h3>
    <a href="https://uflorida-my.sharepoint.com/:p:/g/personal/egiron_ufl_edu/EbzQyMYT8TZAjG-deU-WgJwBD0MQurBSNnY9yr-mRaPqYw?e=a6fPDg">Click Here to View Our First Presentation<a>
  <h3>2nd Iteration.</h3>
    <a href="https://uflorida-my.sharepoint.com/:p:/g/personal/egiron_ufl_edu/EQ8FcKa_Q3NIl_HodE7qynoBTn9bDdhCR5cewVtorGZaOQ?e=crPwxD">Click Here to View Our Second Presentation<a>
  <h3>3rd Iteration.</h3>
      <a href="https://uflorida-my.sharepoint.com/:p:/g/personal/egiron_ufl_edu/EbMzl-hWpVZHmMbQq3wraO4BWp_hQrkxnr-2EPTRHGksAw?e=RFAFaa">Click Here to View Our Third Presentation<a>
      <br>The code in this "in-progress" repository is our 3rd iteration of our project.</br>

## How To Run
Make sure to have python working on your device and run the Testing_updatedAlgorithm.py to run our simulations!

## Project Scenario
### When students travel to campus they have the option to take a car or bus. Depending on their decision, it can contribute to road congestion because of the limit road space available. In our game, these are the contraints: 
* N players
* 2 strategies: car or bus
* Limited amount of road space
* Set number of buses
* Players can switch strategy depending on delay

## Mechanism
* Current: we are using the repetition mechanism
* It simulates days as rounds 
* We make it a possibility for players to switch strategy depending on the level of congestion on the road (delay function is high)

## Delay Function
$$D_{i}(car) = F\left(\sum_{i=1}^{C}\left(\frac{S_{c}}{R}\right) +\frac{S_{c}}{R}\right) + \frac{S_{b}}{R}$$
$$D_{i}(bus) = F\left(\sum_{i=1}^{C}\frac{S_{c}}{R}\right) + B +\frac{S_{b}}{R}$$
$$F(x) = \left\lbrace \begin{array}{cl}L & : \ x \geq t \\\\cx & : \ otherwise\end{array} \right. $$

* $$D_{i}(car)$$ – delay when the player takes a car
* $$D_{i}(bus)$$ – delay when the player takes the bus
* $$S_{c}$$ – size of car 
* $$S_{b}$$ – space taken by busses
* $$C$$ – number of cars (other than the player)
* $$R$$ – available road space 
* $$B$$ – delay caused by taking bus
* $$L$$ – large constant
* $$t$$ – threshold for traffic becoming too congested
* $$c$$ – constant for scaling x in F

## Nash and Pareto
Nash Equilibrium:
* $$B > F\left(\sum_{i=1}^{C}\left(\frac{S_{c}}{R}\right) +\frac{S_{c}}{R}\right) - F\left(\sum_{i=1}^{C}\frac{S_{c}}{R}\right)$$
  * when all players are traveling by car
  * when $$\sum_{i=1}^{C}\frac{S_{c}}{R} \geq t$$
* $$B < F\left(\sum_{i=1}^{C}\left(\frac{S_{c}}{R}\right) +\frac{S_{c}}{R}\right) - F\left(\sum_{i=1}^{C}\frac{S_{c}}{R}\right)$$
  * when all players are traveling by bus
* $$B = F\left(\sum_{i=1}^{C}\left(\frac{S_{c}}{R}\right) +\frac{S_{c}}{R}\right) - F\left(\sum_{i=1}^{C}\frac{S_{c}}{R}\right)$$
  * nash for all player strategy combinations, except for when $$\sum_{i=1}^{C}\frac{S_{c}}{R} = t$$   
 
Pareto:
* $$B > F\left(\sum_{i=1}^{C}\left(\frac{S_{c}}{R}\right) +\frac{S_{c}}{R}\right) - F\left(\sum_{i=1}^{C}\frac{S_{c}}{R}\right)$$
  * all strategy combinations are pareto except for when $$\sum_{i=1}^{C}\frac{S_{c}}{R} = t$$ or all players are in cars
* $$B \leq F\left(\sum_{i=1}^{C}\left(\frac{S_{c}}{R}\right) +\frac{S_{c}}{R}\right) - F\left(\sum_{i=1}^{C}\frac{S_{c}}{R}\right)$$
  * when everyone takes the bus

## Simulation Analysis
### Defined Variables
* Bus constant: 10
* Threshold to Switch: 0.4
* Chance to switch if threshold met: 0.3

### Results
* Congestion is affected by player choices:
  * As more players take cars, more of the road is taken up, resulting in higher delays for all players
  * As more players take the bus, less of the road is taken up, resulting in lower delays for all players
* With the repetition mechanism, players had the chance to change their strategy day by day; some things we noticed:
  * When traffic becomes unbearable, players are more likely to switch to bus in an attempt to aleviate some traffic
  * When traffic is lighter, players are much less likely to switch
  * After a certain number of rounds, if the congestion gets below a certain level, players stop switching entirely
  * In cases where there is less space on the road, increasing the number of rounds makes it more likely to reach an equilibrium
  * In cases where there is a lot of excess space on the road, equilibrium is reached quicker and the number of rounds does not affect it as much
 
Example:

One-off game:

<img src="https://github.com/user-attachments/assets/1ea203ac-cb06-44b3-94ab-09e8838d6843" alt="Alt Text" width="800" height="180">

5th and 10th rounds of repeated game (with same starting values as one-off):

<img src="https://github.com/user-attachments/assets/4c589d22-109b-4f6e-bee3-5052e97a221d" alt="Alt Text" width="300" height="300">

<img src="https://github.com/user-attachments/assets/ac39ccc0-9f37-4b81-8d0d-602b80b1a337" alt="Alt Text" width="300" height="300">

