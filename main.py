import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()





def main():
    print('What would you like? (small/ medium/ large/ off/ report)')
    input_size = input()
    if input_size.strip() not in ['small', 'medium', 'large', 'off', 'report']:
        print('Invalid option, please try again.')
        main()
    elif input_size == 'off':
        print('Shutting down...')
        exit()
    elif input_size == 'report':
        print(f'Bread: {sandwich_maker_instance.machine_resources["bread"]} slices \nHam: {sandwich_maker_instance.machine_resources["ham"]} slices \nCheese: {sandwich_maker_instance.machine_resources["cheese"]} ounces')
        main()
    recipe = recipes.get(input_size, None)
    if not recipe:
        print('Invalid option, please try again.')
        main()
    if sandwich_maker_instance.check_resources(recipe['ingredients']):
        print(f'Sorry, there is not enough {sandwich_maker_instance.check_resources(recipe['ingredients'])}. Please try again later.')
        main()
    coins = cashier_instance.process_coins()
    if not cashier_instance.transaction_result(coins, recipe['cost']):
        print('Sorry, that is not enough money. Money refunded.')
        main()
    if coins > recipe['cost']:
        print(f'Here is your change: ${coins - recipe["cost"]:.2f}')
    sandwich_maker_instance.make_sandwich(recipe['ingredients'])
    print(f'Here is your {input_size.strip()} sandwich. Bon appetit!')
    main()


if __name__=="__main__":
    main()