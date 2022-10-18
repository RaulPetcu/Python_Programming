def validateDict(set_of_rules, dict):
    for rule in set_of_rules:
        rule_key = rule[0]
        prefix = rule[1]
        middle = rule[2]
        suffix = rule[3]

        # check if dict contains rule_key 
        if rule_key not in dict.keys():
            return False
        else: 
            value = dict[rule_key]
            # check if value has the prefix
            if value.find(prefix) != 0:
                return False
            # check if value has the suffix
            if value.find(suffix)!= len(value) - len(suffix):
                return False
            # check if value has the middle
            if value.find(middle) < value.find(prefix) | value.find(middle) > value.find(suffix):
                return False

    return True

print(validateDict(set_of_rules={("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}, dict={"key1": "come inside, it's too cold out", "key3": "this is not valid"}))


