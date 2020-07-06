class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # 无根节点
        if not root:
            return []
        res = [root.val]
        # 根左右
        for node in root.children:
            res.extend(self.preorder(node))
        return res