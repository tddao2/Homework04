#Tri Dao
#1954347
#12.7 CIS 2348 LAB: Fat-burning heart rate

def get_age():
    age = int(input())
    # TODO: Raise excpetion for invalid ages
    if age not in range(18, 75):
        raise ValueError('Invalid age.')
    return age

# TODO: Complete fat_burning_heart_rate() function
def fat_burning_heart_rate(age):
    heart_rate = (220 - age) * 0.70
    return heart_rate

if __name__ == "__main__":
    # TODO: Modify to call get_age() and fat_burning_heart_rate()
    try:
        age = get_age()
        print('Fat burning heart rate for a {} year-old: {} bpm'.format(age, fat_burning_heart_rate(age)))
    #       and handle the exception
    except ValueError as excpt:
        print(excpt)
        print('Could not calculate heart rate info.\n')
