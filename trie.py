from node import Node


class Trie:
    def __init__(self):
        self.__root = Node()

    def insert(self, keyword):
        cur_node = self.__root
        for char in keyword:
            if not cur_node.next.get(char):
                cur_node.next[char] = Node()
            cur_node = cur_node.next[char]
        cur_node.is_end = True

    def __get_short_suf_link(self, node):
        if node.short_suf_link:
            return node.short_suf_link
        elif node.suf_link.is_end:
            return node.suf_link
        elif node.is_end:
            return node
        elif self.__root == node.suf_link:
            return None
        else:
            return self.__get_short_suf_link(node.suf_link)        
    
    def __go(self, node, char):
        while not (node == self.__root or node.next.get(char)):
            node = node.suf_link
        return node.next.get(char, node)
    
    def set_suf_links(self):
        queue = []
        self.__root.suf_link = self.__root
        self.__root.short_suf_link = None
        
        for node in self.__root.next.values():
            node.suf_link = self.__root
            node.short_suf_link = None
            queue.append(node)
        
        while queue:
            cur_node = queue.pop(0)
            for p_char, child in cur_node.next.items():
                p_suf_link = cur_node.suf_link
                child.suf_link = self.__go(p_suf_link, p_char) 
                short_suf_link = self.__get_short_suf_link(cur_node)
                cur_node.short_suf_link = short_suf_link
                queue.append(child)

    def get_pattern_count(self, text):
        cur_node = self.__root
        count = 0
        for char in text:
            cur_node = self.__go(cur_node, char)
            if cur_node.is_end:
                count += 1
            else:
                temp = cur_node.short_suf_link
                while temp:
                    count += 1
                    temp = temp.short_suf_link
        return count
