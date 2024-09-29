class TreeNode:
    def __init__(self):
        self.Children={}
        self.IsEnd=False
class Trie:
    def __init__(self):
        self.root=TreeNode()
    def Add(self,word):
        CurrentNode=self.root
        for character in word:
            if character not in CurrentNode.Children:
                CurrentNode.Children[character]=TreeNode()
            CurrentNode=CurrentNode.Children[character]
        CurrentNode.IsEnd=True

    def Search(self,word):
        CurrentNode=self.root
        for character in word:
            if character not in CurrentNode.Children:
                return False
            CurrentNode=CurrentNode.Children[character]
        if CurrentNode.IsEnd:
            return True
        return False
    def Remove(self,word):
        if not self.Search(word):
            print("Word not found.. Can't Remove")
        CurrentNode=self.root
        for character in word:
            CurrentNode=CurrentNode.Children[character]
        CurrentNode.IsEnd=False






trieDs=Trie()
trieDs.Add("APPLE")
trieDs.Add("APPLICATION")
trieDs.Remove("APP")

