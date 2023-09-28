from random import randint
from board import Board
from player import Player
from bank import Bank


def next_player_index():
    value = 0
    while True:
        yield value
        value = (value + 1) & 3


def roll_dices() -> int:
    return randint(1, 6) + randint(1, 6)


class Game:
    def __init__(self, players: list[Player], points_to_win: int):
        self.players = players
        self.board = Board(players)
        self.points_to_win = points_to_win
        self.bank = Bank()

    def loop(self):
        # pregame. Everyone places 2 villages and 2 roads
        self.place_starting_villages_and_roads()
        current_player = self.next_player()
        while True:
            if self.has_winner():
                break
            dice = roll_dices()
            if dice == 7:
                self.remove_too_many_cards()
                self.rob(current_player)
            self.give_resources()
            self.play(current_player)
            self.update_longest_road()
            self.update_army()
            current_player = self.next_player()

    def next_player(self) -> Player:
        return self.players[next(next_player_index())]

    def has_winner(self):
        for player in self.players:
            if player.points >= self.points_to_win:
                return True
        return False

    def place_starting_villages_and_roads(self) -> None:
        for player in self.players:
            nodes = player.village_and_road()
            self.board.place_village_and_road(nodes)
        for i in range(len(self.players), -1, -1):
            nodes = player.village_and_road()
            self.board.place_village_and_road(nodes)

    def remove_too_many_cards(self) -> None:
        for player in self.players:
            if player.cards > 7:
                discarded_cards = player.discard_cards()
                self.bank.add(discarded_cards)

    def rob(self, current_player: Player) -> None:
        tile = current_player.select_tile_for_robber()
        self.board.move_robber(tile)
        robable_players = self.board.get_robable_players()
        current_player.rob(robable_players)

    def give_resources(self) -> None:
        players_resources = self.board.get_resources()
        for player, resources in players_resources:
            player.add(resources)

    def play(self, player: Player) -> None:
        played_card = False
        while True:
            decision = player.decision()
            if decision == "village":
                position = player.village_position()
                self.board.place_village(position, player)
            elif decision == "city":
                position = player.city_position()
                self.board.place_city(position, player)
            elif decision == "road":
                nodes = player.road_position()
                self.board.place_road(nodes)
            elif decision == "play_card" and played_card:
                card = player.play_card()
                self.execute_card(card, player)
                played_card = True
            elif decision == "trade":
                self.trade()
            else:
                break

    def execute_card(self, card: str, current_player: Player) -> None:
        if card == "knight":
            self.rob(current_player)
            current_player.army += 1
        elif card == "road":
            nodes = current_player.road_position()
            self.board.place_road(nodes)
            nodes = current_player.road_position()
            self.board.place_road(nodes)
        elif card == "cards":
            current_player.add_two_resources_because_of_action_card()
        elif card == "monopoly":
            desired = current_player.monopoly_resource()
            amount = 0
            for player in self.players:
                if player == current_player:
                    continue
                removed_cards = player.remove(desired)
                amount += len(removed_cards)
            current_player.add([desired] * amount)

    def trade(self, current_player: Player) -> None:
        offer = current_player.offer()  # (give,get)
        reactions = (
            []
        )  # [reaction, other_offer]. Reaction can be "accept","decline","change"
        for player in self.players:
            if player == current_player:
                continue
            reactions.append(player.react_to_offer())
        # TODO: finish trading
