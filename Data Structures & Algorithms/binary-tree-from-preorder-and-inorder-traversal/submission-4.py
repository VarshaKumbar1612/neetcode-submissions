# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # if not preorder:
        #     return None

        # root_value = preorder[0]
        # root = TreeNode(root_value)

        # mid = inorder.index(root_value)

        # root.left = self.buildTree(
        #     preorder[1:mid + 1],
        #     inorder[:mid]
        # )

        # root.right = self.buildTree(
        #     preorder[mid + 1:],
        #     inorder[mid + 1:]
        # )

        # return root

        # Map each value to its index in inorder
        inorder_pos = {value: i for i, value in enumerate(inorder)}
        preorder_idx = 0

        def build(left: int, right: int) -> Optional[TreeNode]:
            nonlocal preorder_idx

            if left > right:
                return None

            # Preorder visits root before its children
            root_val = preorder[preorder_idx]
            preorder_idx += 1

            root = TreeNode(root_val)
            mid = inorder_pos[root_val]

            # Build left subtree before right subtree
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)