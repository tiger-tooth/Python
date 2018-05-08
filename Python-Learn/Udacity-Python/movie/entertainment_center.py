import media
import fresh_tomatoes
toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life",
                        "https://en.wikipedia.org/wiki/File:Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=rNk1Wi8SvNc")
# print(toy_story.storyline)

avatar = media.Movie("Avatar", "A marine on an alien planet",
                     "https://en.wikipedia.org/wiki/File:Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
# print(avatar.storyline)
# avatar.show_trailer()


mammamia = media.Movie("Mamma Mia", "A music movie",
                       "https://en.wikipedia.org/wiki/File:MammaMiaTeaserPoster.JPG",
                       "https://www.youtube.com/watch?v=8RBNHdG35WY")
#print(mammamia.storyline)
#mammamia.show_trailer()

movie=[toy_story,avatar,mammamia]
#fresh_tomatoes.open_movies_page(movie)
#print(media.Movie.VALID_RATINGS)
print(media.Movie.__module__)