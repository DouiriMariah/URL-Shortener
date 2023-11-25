import pyshorteners
import validators

def is_valid_url(url):
    return validators.url(url)

def get_url():
    try:
        url = input('Enter the url: ')
        while not is_valid_url(url):
            if not url:
                url = input('Please enter a url: ')
            elif url.lower() in ["exit", "quit"]:
                print("Exiting...")
                exit(0)
            else:
                print('Error: A valid URL is required')
                url = input('Please enter a valid URL: ')
        return url
    except EOFError:
        print("\nCtrl+D or Ctrl+Z detected. ")
    except KeyboardInterrupt:
        print('\nCtrl C')
    exit(0)

def shortenurl():
    url = get_url()
    try:
        s = pyshorteners.Shortener()
        final_url = s.tinyurl.short(url)
        print('Shortened URL:', final_url)
    except pyshorteners.exceptions.ShorteningErrorException as e:
        print('Error : The URL is already shortened')
    except Exception as e:
        print('Error:', e)

shortenurl()
