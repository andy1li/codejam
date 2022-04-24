# 2014 Qualification Round - D. Deceitful War
# https://code.google.com/codejam/contest/dashboard?c=2974486#s=p3

def solve(n, naomi, ken):
    # Find out first Ken's optimal strategy and then Naomi's optimal deceptive strategy
    naomi_asc = sorted(naomi)
    naomi_dsc = sorted(naomi_asc, reverse=True)
    ken_asc = sorted(ken)
    ken_dsc = sorted(ken_asc, reverse=True)
      
    deceitful_war_result = 0
    war_result = 0

    # Calculate deceitful_war:
    # To win as many rounds as possible,
    # naomi iteratively beats (ken's lightest remaining block)
    # with (her lightest possible winning block)
    # by lying that it's heavier than (ken's heaviest one) 
    # to trick him to play (his lightest remaining one)
    # until she cannot win anymore without giving aways her lies 
    i_k = 0
    # print naomi_asc
    # print ken_asc
    for naomi_lightest_possible in naomi_asc:
        if naomi_lightest_possible > ken_asc[i_k]:
            # print naomi_lightest_possible, ">", ken_asc[i_k], "@", i_k
            deceitful_war_result += 1
            i_k += 1
        # elif naomi_lightest_possible < ken_asc[i_k]:
        #   continue
        

    # Calculate war:
    # naomi always plays her heaviest remaining block
    # ken responds with as many "just heavier" block as possible
    i_k = 0
    #print naomi_dsc
    #print ken_dsc
    for naomi_heavist_remaining in naomi_dsc:
        if naomi_heavist_remaining > ken_dsc[i_k]:
            # print naomi_heavist_remaining, ken_dsc[i_k], i_k
            war_result += 1
        elif naomi_heavist_remaining < ken_dsc[i_k]:
            # print naomi_heavist_remaining, ken_dsc[i_k], i_k
            i_k += 1
            
    return deceitful_war_result, war_result

#input, solve and output:
input = open('foobar.in', 'r')
output = open('f.out', 'w')

n_cases = int(input.readline())
for case in range(1, n_cases+1):
    n_blocks = int(input.readline())
    naomi = [float(n) for n in input.readline().split()]
    ken   = [float(n) for n in input.readline().split()]
    deceitful_war, war = solve(n_blocks, naomi, ken)

    result_output = 'Case #%s: %s %s\n' %(case, deceitful_war, war)
    print(result_output)
    output.write(result_output)

input.close()
output.close()
