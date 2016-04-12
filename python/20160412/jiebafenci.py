#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-04-12 17:26:12
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import jieba
import urllib2, urllib


# test_str = "我来到北京清华大学"
# seg_list = jieba.cut(test_str, cut_all=True)
# print "Full Mode: ", "/ ".join(seg_list)

def gen_trie(f_name):
    lfreq = {}
    trie = {}
    ltotal = 0.0
    with open(f_name, 'rb') as f:
        lineno = 0
        for line in f.read().rstrip().decode('utf-8').split('\n'):
            lineno += 1
            try:    
                word,freq,_ = line.split(' ')
                freq = float(freq)
                lfreq[word] = freq
                ltotal+=freq
                p = trie
                for c in word:
                    if c not in p:
                        p[c] ={}
                    p = p[c]
                p['']='' #ending flag
            except ValueError, e:
                logger.debug('%s at line %s %s' % (f_name,  lineno, line))
                raise ValueError, e
    return trie, lfreq, ltotal
if __name__ == '__main__':
    a, b, c = gen_trie('a.txt')
    for i in a:
        print i.encode('utf-8')
    for j in b:
        print j.encode('utf-8')
    print c