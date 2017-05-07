import Movies_class_fun
import fresh_tomatoes

toy_story = Movies_class_fun.Movie("Toy Story", "A boy who has toys that talk","https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                                    "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print toy_story.title 


underworld = Movies_class_fun.Movie("Underworld", "vampires & werewolfs", "https://en.wikipedia.org/wiki/Underworld:_Blood_Wars#/media/File:Underworld_Blood_Wars.jpg",
                                    "https://www.youtube.com/watch?v=MqT-e44kIM8")
#underworld.show_trailer()


school_of_rock = Movies_class_fun.Movie("School of Rock", "Overly enthusiastic guitarist Dewey Finn (Jack Black) gets thrown out of his bar band and finds himself in desperate need of work.",
                                        "https://en.wikipedia.org/wiki/School_of_Rock#/media/File:School_of_Rock_Poster.jpg","https://www.youtube.com/watch?v=5afGGGsxvEA")


movies=[toy_story, underworld, school_of_rock]
fresh_tomatoes.open_movies_page(movies)