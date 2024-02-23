# Cellular automata based in Conway's Game of Life
In this project I created a cellular automata with the following rules:
- If a live cell has less than 2 neighbours alive, it becomes a dead cell (simulating underpopulation)
- If a live cell has 2 or 3 neighbours alive, it lives to the next generation
- If a live cell has more than 3 neighbours alive, it becomes a dead cell (simulating overpoulation)
- If a dead cell has exactly 3 neighbours alive, it becomes an alive cell (simulation reproduction)

In this example I've used the same rules as the Conway's Game of Life as described above.

## Graphic Interface

For a graphical representation of the cellular automata I opted to use Pygame as the game can be represented as simple squares and a grid.\
And that's the only external library necessary for this project, you can install pygame in your local machine by executing the following command in your terminal:

```
pip install pygame
```
or
```
pip3 install pygame
```
## Video example
When you execute the program by running:
```
python3 cell.py
```
When the window pop up appears you can hit the `space` key to begin the simulation
![](https://github.com/YuriAikau/Celular_Automata/blob/main/images/test.gif)
While on the simulation you can pause it anytime by pressing the `space` key, the unpausing it by pressing `space` again. You can also toggle any given cell (alive or dead) by clicking in their respective square.\
To quit you simply click on the 'X' button on the top of the window.
