class Node:
    def __init__(self):
        self.__next = {}
        self.__is_end = False
        self.__suf_link = None
        self.__short_suf_link = None

    @property
    def next(self):
        return self.__next
    
    @property
    def is_end(self):
        return self.__is_end
    
    @is_end.setter
    def is_end(self, is_end):
        self.__is_end = is_end

    @property
    def suf_link(self):
        return self.__suf_link

    @suf_link.setter
    def suf_link(self, suf_link):
        self.__suf_link = suf_link

    @property
    def short_suf_link(self):
        return self.__short_suf_link

    @short_suf_link.setter
    def short_suf_link(self, short_suf_link):
        self.__short_suf_link = short_suf_link
