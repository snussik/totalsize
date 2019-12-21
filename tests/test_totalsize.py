import sys
import unittest

from totalsize.total import Playlist


class TestTotal(unittest.TestCase):
    def test_get_totalsize_yt_channel(self):
        playlist = Playlist("https://www.youtube.com/channel/UCvAUb8YbRyXz_l9CXptKoQA/", "18")
        playlist.accum_info()
        self.assertEqual(playlist.totals.size, 425674114)
        self.assertEqual(playlist.number_of_media, 4)
        self.assertEqual(playlist.number_of_media_inacc, 0)
        self.assertEqual(playlist.number_of_media_nosize, 0)

    def test_get_totalsize_yt_playlist(self):
        playlist = Playlist(
            "https://www.youtube.com/watch?v=KIHBpp34JkA&list=PLGx22rG4Cm6dEFvkjmdSRpulz6l0M-g2u", "18"
        )
        playlist.accum_info()
        self.assertEqual(playlist.totals.size, 197941592)
        self.assertEqual(playlist.number_of_media, 3)
        self.assertEqual(playlist.number_of_media_inacc, 0)
        self.assertEqual(playlist.number_of_media_nosize, 0)

    def test_get_totalsize_yt_video(self):
        playlist = Playlist("https://www.youtube.com/watch?v=KIHBpp34JkA", "18")
        playlist.accum_info()
        self.assertEqual(playlist.totals.size, 69574304)
        self.assertEqual(playlist.number_of_media, 1)
        self.assertEqual(playlist.number_of_media_inacc, 0)
        self.assertEqual(playlist.number_of_media_nosize, 0)


if __name__ == "__main__":
    sys.exit(unittest.main())
