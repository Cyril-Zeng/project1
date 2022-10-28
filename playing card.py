#定义card类 代表每一张牌
class Card():
    ranks=['A', '2','3','4','5','6','7','8','9','10','J','Q','K']
    suits=['梅花','方块','红桃','黑桃']
    def __init__(self,rank,suit,face_up=True):
        self.rank=rank
        self.suit=suit
        self.is_face_up=face_up  #是否显示牌的正面，True为正面，False为反面

    def pic_order(self):  #牌的顺序号
        if self.rank=='A':
            FaceNum=1
        elif self.rank=='J':
            FaceNum = 11
        elif self.rank=='Q':
            FaceNum = 12
        elif self.rank=='K':
            FaceNum = 13
        else:
            FaceNum=int(self.rank)

        if self.suit=='梅花':
            Suit=1
        elif self.suit=='方块':
            Suit=2
        elif self.suit=='红桃':
            Suit=3
        elif self.suit=='黑桃':
            Suit=4
        return FaceNum+13*(Suit-1)

    def flip(self): #翻牌
        self.is_face_up=not self.is_face_up

    def printcard(self):  #打印一张牌的信息
        if self.is_face_up:
            rep=self.suit+self.rank
        else:
            rep='XX'
        return rep

#定义Hand类为一个玩家手中的牌（13张）
class Hand():
    def __init__(self):
        self.cards=[] #用于存储手中的牌

    def print_cardsinhand(self):
        if self.cards:
            rep=''
            for card in self.cards:
                rep+=str(card.printcard())+'\t'
        else:
            rep='无牌'
        return rep
    def clear(self):  #清空手牌
        self.cards=[]
    def add(self,card): #增加手牌
        self.cards.append(card)
    def give(self,card,other_hand): #把牌给其他牌手
        self.cards.remove(card)
        other_hand.cards.append(card)

class Poke(Hand):
    """A deck of playing cards"""
    def populate(self): #生成一副牌
        for suit in Card.suits:
            for rank in Card.ranks:
                self.add(Card(rank,suit))

    def shuffle(self):  #洗牌
        import random
        random.shuffle(self.cards)

    def deal(self,hands,per_hand=13): #发牌
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card=self.cards[0]
                    super().give(top_card,hand)
                else:
                    print('牌已发完')

#主函数
if __name__=='__main__':
    print('Welcome!This is the poke game!')
    players=[Hand(),Hand(),Hand(),Hand()]
    poke1=Poke()
    poke1.populate()
    poke1.shuffle()
    poke1.deal(players)
    n=1
    for hand in players:
        print('牌手',n,end=':')
        print(hand.print_cardsinhand())
        n+=1
    input('\n Press Enter to exist')











