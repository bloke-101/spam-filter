from node import Node

class Trie:
    def __init__(self):
        self.__root = Node()

    def __is_root(self, node):
        return node == self.__root

    def __has_next(self, node, char):
        return node.next.get(char)

    def insert(self, keyword):
        cur_node = self.__root
        for char in keyword:
            if not cur_node.next.get(char):
                cur_node.next[char] = Trie()
            cur_node = cur_node.next[char]
        cur_node.is_end = True

    def __get_short_suf_link(self, node):
        if not node.short_suf_link:
            if node.suf_link.is_end:
                node.short_suf_link = node.suf_link
            elif node.is_end:
                node.short_suf_link = node
            elif node.suf_link.is_root:
                node.short_suf_link = None
            else:
                link = self.__get_short_suf_link(node.suf_link)
                node.short_suf_link = link
        return node.short_suf_link
    
    def __get_next_suf_link(self, node, char):
        return node.next[char] if node.next.get(char) else node
    
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
                is_root = self.__is_root(p_suf_link)
                has_next = self.__has_next(p_suf_link, p_char)
                while not (is_root or has_next):
                    p_suf_link = p_suf_link.suf_link

                next = self.__get_next_suf_link(p_suf_link, p_char)
                short = self.__get_short_suf_link(cur_node)
                child.suf_link = next
                cur_node.short_suf_link = short
                queue.append(child)

    def __go(self, node, char):
        while not (node.is_root or node.next.get(char)):
            node = node.suf_link
        if node.next.get(char):
            return node.next[char]
        return node

    def find_all_patterns(self, text):
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
