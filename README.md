# MATH456

The prisoner’s dilemma is an extensively studied problem in game theory that models two rational
agents that can either cooperate for their mutual benefit or can betray each other for a greater payoff.
This problem is a classic model of cooperative decision making, and highlights the difference between
collective rationality and individual rationality. There are seven strategies in the prisoner’s dilemma our
group will investigate. These strategies are:
1. Nice: The agent always cooperates, no matter what the other agent does.
2. Mean: The agent always defects, no matter what the other agent does.
3. Tit for Tat: The agent cooperates on the first round, and then imitates its opponent’s
previous move thereafter.
4. Reverse Tit for Tat: The agent does the reverse of Tit for Tat. It defects on the first
move, then plays the opposite of the opponent’s last move.
5. Grim Trigger: The agent always cooperates until the other agent defects, after which
the agent only defects.
6. Hard Majority: The agent defects on its first move, and will continue to defect if the
number of defections of the opponent is greater than or equal to the number of times it
has cooperated, otherwise the agent cooperates.
7. Blind: The agent tries to figure out what another agent’s strategy is, then plays what’s
best against that.
Our group plans on using a neural network to model agents’ long term strategy in an iterated version
of the prisoner’s dilemma, in which the game is played numerous times. Each agent will augment their
strategy based on the previous results of each round of the game. Our model will have up to twenty
agents who have been randomly assigned the first six strategies (nice, mean, retaliating, tit for tat, reverse
tit for tat, grim trigger, and hard majority), and will go up against a singular agent playing the blind
strategy. The agent playing the blind strategy will eventually determine the strategies of the agents it’s
playing against and it will optimize its payoff based on its current understanding of each other agent’s
strategy.
The final result of this project will be a Bayesian network that visualizes the “thought process” of
the singular agent playing the blind strategy. This network will elucidate how the agent playing the
blind strategy determined the other agents’ strategy, and how they optimized their strategy to maximize
its own payoff. Some important questions that this model can answer are: which strategy takes the
blind agent fastest to determine? Which takes the longest to determine? What strategies are easy to
win against? Which are difficult to win against? The prisoner’s dilemma is an important problem in
game theory that has implications in business, economics, and psychology. Gaining deeper insight into
potential strategies used in the prisoner’s dilemma provides helpful information about how agents act in
cooperative settings, where defection may present a higher payoff than cooperation
