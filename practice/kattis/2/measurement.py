"""https://open.kattis.com/problems/measurement"""

adj_list = {}


def add_node(node, adj_list=adj_list):
    adj_list[node] = []


add_node('th')
add_node('in')
add_node('ft')
add_node('yd')
add_node('ch')
add_node('fur')
add_node('mi')
add_node('lea')


def add_children(parent, children, adj_list=adj_list):
    temp = adj_list[parent]
    temp.append(children)
    adj_list[parent] = temp


add_children('in', {'th': 1000})
add_children('th', {'in': 1/1000})

add_children('ft', {'in': 12})
add_children('in', {'ft': 1/12})

add_children('yd', {'ft': 3})
add_children('ft', {'yd': 1/3})

add_children('ch', {'yd': 22})
add_children('yd', {'ch': 1/22})

add_children('fur', {'ch': 10})
add_children('ch', {'fur': 1/10})

add_children('mi', {'fur': 8})
add_children('fur', {'mi': 1/8})

add_children('lea', {'mi': 3})
add_children('mi', {'lea': 1/3})


start_unit = 'ft'
end_unit = 'in'
