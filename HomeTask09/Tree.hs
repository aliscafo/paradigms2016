module Tree (BinaryTree, lookup, insert) where
import Prelude hiding (lookup)


-- Реализовать двоичное дерево поиска без балансировки (4 балла)
data BinaryTree k v = Null | Node k v (BinaryTree k v) (BinaryTree k v) deriving (Show, Eq)


-- “Ord k =>” требует, чтобы элементы типа k можно было сравнивать 
lookup :: Ord k => k -> BinaryTree k v -> Maybe v
lookup k Null = Nothing 
lookup k (Node key value left right) 
        | k == key = Just value
        | k < key = lookup k left
        | k > key = lookup k right 


insert :: Ord k => k -> v -> BinaryTree k v -> BinaryTree k v
insert k v Null = Node k v Null Null
insert k v (Node key value left right)
        | k == key = Node key v left right
        | k < key = Node key value (insert k v left) right
        | k > key = Node key value left (insert k v right)


tree_min :: Ord k => BinaryTree k v -> k
tree_min (Node k v Null Null) = k
tree_min (Node k v left Null) = min k (tree_min left)
tree_min (Node k v Null right) = min k (tree_min right)
tree_min (Node k v left right) = min k (min (tree_min left) (tree_min right))


find_min :: Ord k => k -> BinaryTree k v -> v
find_min k (Node key value left right) 
        | k == key = value
        | k < key = find_min k left
        | k > key = find_min k right 


delete :: Ord k => k -> BinaryTree k v -> BinaryTree k v
delete k Null = Null
delete k (Node key value left right)
	| k < key = Node key value (delete k left) right
	| k > key = Node key value left (delete k right)
	| k == key = if is_null right
			then left
		else if is_null left
			then right
		else (Node minimum (find_min minimum right) left (delete minimum right))
			where 
				minimum = (tree_min right)
	        	  	is_null Null = True
				is_null _ = False 
