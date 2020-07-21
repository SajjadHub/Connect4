import math
import random
import Connect4
# Copied from codebox/connect4
# Node class for Monte carlo search tree


class Node:
    def __init__(self, parent, action):
        self.parent = parent
        self.action = action  # [player_id, col]
        self.visits = 0
        self.score = 0
        self.children = None

    def is_leaf(self):
        return self.children is None or self.is_terminal()

    def is_terminal(self):
        return self.children == []


class Tree():
    def __init__(self):
        self.root = Node(None, None)


class RandomStrategy():
    def move(self, game, player_id):
        try:
            return random.choice(get_valid_moves(game.board))
        except IndexError:
            game.gameOver = True
            return


def get_valid_moves(board):
    return [i for i, v in enumerate(board[5]) if v == 0]


class MCT():
    def __init__(self, rollout_limit):
        self.rollout_limit = rollout_limit

    def move(self, game, id):
        tree = Tree()

        for i in range(self.rollout_limit):
            self.simulate(game, tree, id)

        return max(tree.root.children, key=lambda c: c.visits).action[1]

    def simulate(self, game, tree, id):
        currentNode = tree.root
        nodes_to_update = [currentNode]

        while not currentNode.is_leaf():
            currentNode = self.get_highest_ucb(currentNode)
            id, col = currentNode.action
            game.move(col)
            nodes_to_update.append(currentNode)

        if not game.gameOver:
            nextPlayer = game.getNextPlayer()

            self.addChildren(currentNode, game.board, nextPlayer)
            bestChild = self.get_highest_ucb(currentNode)
            game.move(bestChild.action[1])

            randomStrategy = RandomStrategy()
            while not game.gameOver:
                nextPlayer = game.getNextPlayer()
                randMove = randomStrategy.move(game, game.activePlayer)
                game.move(randMove)

        win = game.winner == id
        draw = game.winner is None
        score = 1 if win else 0 if draw else -1

        for node_to_update in nodes_to_update:
            player_for_node = node_to_update.action[0] if node_to_update.action else None
            node_score = score
            if player_for_node != id:
                node_score *= -1
            node_to_update.visits += 1
            node_to_update.score += node_score

    def addChildren(self, parent_node, board, player_id):
        assert parent_node.children is None
        moves = get_valid_moves(board)

        children = []
        for move in moves:
            child_node = Node(parent_node, (player_id, move))
            children.append(child_node)

        parent_node.children = children

    def get_highest_ucb(self, node):
        max_ucb = -math.inf
        max_children = []
        for child in node.children:
            child_ucb = self.__ucb(child)
            if child_ucb > max_ucb:
                max_children = [child]
                max_ucb = child_ucb

            elif self.__ucb(child) == max_ucb:
                max_children.append(child)

        return random.choice(max_children)

    def __ucb(self, node):
        if node.visits == 0:
            return math.inf
        return node.score/node.visits + 2 * (math.log(node.parent.visits) / node.visits) ** 0.5


def self_play():
    NNgame = Connect4.game()
    NN = MCT(1000)

    while not NNgame.gameOver:
        id, nextCol = NN.move(NNgame, NNgame.activePlayer)
        print("beep")
        NNgame.move(nextCol)


self_play()
