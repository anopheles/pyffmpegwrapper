class FFMpegException(Exception):
    pass

class InputFileDoesNotExist(FFMpegException):
    pass


class CommandError(FFMpegException):
    pass


class UnknownFormat(FFMpegException):
    pass


class UnreadableFile(FFMpegException):
    pass


class CantOverwrite(FFMpegException):
    pass
