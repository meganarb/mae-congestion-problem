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
* Players can switch strategy depending on delay.

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
* $$c$$ – constant for scaling x in F

## Nash and Pareto
![image](https://github.com/user-attachments/assets/8ddea3e0-1185-4719-8e9a-28a8f1b48114)
![image](https://github.com/user-attachments/assets/9b67490f-94d9-4d1e-a1dd-8634db7c49ec)

## Simulation Analysis
### Defined Variables
* Bus constant:
* Threshold to Switch:
* Chance to switch if threshold met:

### Results
* Self note: provide screenshots of trend
* Then talk about what is happening such as difference in delay related to road taken up and trends of delays and road taken up.
