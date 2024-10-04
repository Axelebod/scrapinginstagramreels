import instaloader
import os

def download_instagram_videos(username):
    # Créer un objet Instaloader
    L = instaloader.Instaloader()

    # Charger le profil
    try:
        profile = instaloader.Profile.from_username(L.context, username)
    except instaloader.exceptions.ProfileNotExistsException:
        print(f"Le profil {username} n'existe pas.")
        return

    # Télécharger toutes les vidéos du profil
    for post in profile.get_posts():
        if post.is_video:
            print(f"Téléchargement de la vidéo : {post.shortcode}")
            L.download_post(post, target=f"{username}_videos")

            # Supprimer les fichiers .json et .txt après le téléchargement
            json_file = f"{username}_videos/{post.shortcode}.json"
            text_file = f"{username}_videos/{post.shortcode}.txt"
            if os.path.exists(json_file):
                os.remove(json_file)
                print(f"Fichier supprimé : {json_file}")
            if os.path.exists(text_file):
                os.remove(text_file)
                print(f"Fichier supprimé : {text_file}")

if __name__ == "__main__":
    account_username = "funny_memes_funny_jokes"  # Remplace par le nom du compte
    download_instagram_videos(account_username)
