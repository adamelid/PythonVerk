def music_func(musicType = "Classic Rock", musicGroup = "The Beatles", vocalist = "Freddie Mercury"):
    print("The best kind of music is " + musicType)
    print("The best music group is " + musicGroup)
    print("The best lead vocalist is " + vocalist)
#definition for music_func goes here

def main():
    music, group, singer = input("Input music, group, singer: ").split(',')
    music_func(music, group, singer)
    music_func()

main()