"""
    Copyright 2012 KU Leuven Research and Development - iMinds - Distrinet

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Administrative Contact: dnet-project-office@cs.kuleuven.be
    Technical Contact: bart.vanbrabant@cs.kuleuven.be
"""

from .plugins import plugin
from itertools import chain

@plugin
def any(item_list : "list", expression : "expression") -> "bool":
    """ 
        This method returns true when at least on item evaluates expression
        to true, otherwise it returns false
        
        @param expression: An expression that accepts one arguments and 
            returns true or false
    """
    for item in item_list:
        if expression(item):
            return True
    return False

@plugin
def all(item_list : "list", expression : "expression") -> "bool":
    """
        This method returns false when at least one item does not evaluate
        expression to true, otherwise it returns true
        
        @param expression: An expression that accepts one argument and 
            returns true or false
    """
    for item in item_list:
        if not expression(item):
            return False
    return True

@plugin
def count(item_list : "list") -> "number":
    """
        Returns the number of elements in this list
    """
    return len(item_list)

@plugin
def each(item_list : "list", expression : "expression") -> "list":
    """ 
        Iterate over this list executing the expression for each item.
        
        @param expression: An expression that accepts one arguments and
            is evaluated for each item. The returns value of the expression
            is placed in a new list
    """
    new_list = []
    
    for item in item_list:
        value = expression(item)
        new_list.append(value)
        
    return new_list

@plugin
def order_by(item_list : "list", expression : "expression" = None, comparator : "epxression" = None) -> "list":
    """ 
        This operation orders a list using the object returned by 
        expression and optionally using the comparator function to determine
        the order.
        
        @param expression: The expression that selects the attributes of the
            items in the source list that are used to determine the order
            of the returned list.
            
        @param comparator: An optional expression that compares two items.     
    """
    expression_cache = {}
    def get_from_cache(item):
        """
            Function that is used to retrieve cache results
        """
        if item in expression_cache:
            return expression_cache[item]
        else:
            data = expression(item)
            expression_cache[item] = data
            return data
    
    def sort_cmp(item_a, item_b):
        """
            A function that uses the optional expressions to sort item_a list
        """
        if expression is not None:
            a_data = get_from_cache(item_a)
            b_data = get_from_cache(item_b)
        else:
            a_data = item_a
            b_data = item_b
    
        if comparator is not None:
            return comparator(a_data, b_data)
        else:
            return cmp(a_data, b_data)
    
    # sort
    return sorted(item_list, sort_cmp)

@plugin
def unique(item_list : "list") -> "bool":
    """
        Returns true if all items in this sequence are unique
    """
    seen = set()
    for item in item_list:
        if item in seen:
            return False
        seen.add(item)
    
    return True

@plugin
def select_attr(item_list : "list", attr : "string") -> "list":
    """ 
        This query method projects the list onto a new list by transforming
        the list as defined in the expression.
        
        @param expression: An expression that returns the item that is to be
            included in the resulting list. The first argument of the
            expression is the item in the source sequence.
    """
    new_list = []
    
    if isinstance(attr, str):
        expression = lambda x: getattr(x, attr)
    
    for item in item_list:
        new_list.append(expression(item))
            
    return new_list

@plugin
def select_many(item_list : "list", expression : "expression", 
                selector_expression : "expression" = None) -> "list":
    """
        This query method is similar to the select query but it merges
        the results into one list.
        
        @param expresion: An expression that returns the item that is to be
            included in the resulting list. If that item is a list itself
            it is merged into the result list. The first argument of the 
            expression is the item in the source sequence. 
            
        @param selector_expression: This optional arguments allows to 
            provide an expression that projects the result of the first
            expression. This selector expression is equivalent to what the 
            select method expects. If the returned item of expression is 
            not a list this expression is not applied.
    """
    new_list = []
    
    for item in item_list:
        result = expression(item)
        
        if not hasattr(result, "__iter__"):
            new_list.append(result)
        else:
            if selector_expression:
                for result_item in result:
                    new_list.append(selector_expression(result_item))
            else:
                new_list.extend(result)
            
    return new_list

@plugin
def where(item_list : "list", expression : "expression") -> "list":
    """ 
        This query method selects the items in the list that evaluate the
        expression to true.
        
        @param expression: An expression that returns true or false
            to determine if an item from the list is included. The first 
            argument of the expression is the item that is to be evaluated.
            The second optional argument is the index of the item in the
            list.
    """
    new_list = []
    for index in range(len(item_list)):
        item = item_list[index]
        
        if expression(item):
            new_list.append(item)
            
    return new_list

@plugin
def where_compare(item_list : "list", expr_list : "list") -> "list":
    """
        This query selects items in a list but uses the tupples in expr_list
        to select the items.
        
        @param expr_list: A list of tupples where the first item is the attr
            name and the second item in the tupple is the value
    """
    new_list = []
    
    new_expr_list = []
    for i in range(0, len(expr_list), 2):
        new_expr_list.append((expr_list[i], expr_list[i + 1]))
        
    for index in range(len(item_list)):
        item = item_list[index]
        
        for attr, value in new_expr_list:
            if getattr(item, attr) == value:
                new_list.append(item)
            
    return new_list
    

@plugin
def flatten(item_list : "list") -> "list":
    """
        Flatten this list
    """
    return list(chain.from_iterable(item_list))

    
