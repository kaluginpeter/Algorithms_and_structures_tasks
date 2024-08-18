# In this kata we are going to mimic a software versioning system.
#
# You have to implement a VersionManager class.
#
# It should accept an optional parameter that represents the initial version. The input will be in one of the following formats: "{MAJOR}", "{MAJOR}.{MINOR}", or "{MAJOR}.{MINOR}.{PATCH}". More values may be provided after PATCH but they should be ignored. If these 3 parts are not decimal values, an exception with the message "Error occured while parsing version!" should be thrown. If the initial version is not provided or is an empty string, use "0.0.1" by default.
#
# This class should support the following methods, all of which should be chainable (except release):
#
# major() - increase MAJOR by 1, set MINOR and PATCH to 0
# minor() - increase MINOR by 1, set PATCH to 0
# patch() - increase PATCH by 1
# rollback() - return the MAJOR, MINOR, and PATCH to their values before the previous major/minor/patch call, or throw an exception with the message "Cannot rollback!" if there's no version to roll back to. Multiple calls to rollback() should be possible and restore the version history
# release() - return a string in the format "{MAJOR}.{MINOR}.{PATCH}"
# May the binary force be with you!
#
# ALGORITHMSARRAYSSTRINGSOBJECT-ORIENTED PROGRAMMING
# Solution
BACKUP = []
class VersionManager:
    def __init__(self, version='0.0.1'):
        vers: list = version.split('.')
        if vers == ['']:
            vers = '0.0.1'.split('.')
        for words in vers[:3]:
            for char in words:
                if char not in '01234567893.':
                    raise ValueError('Error occured while parsing version!')
        self.major_ = int(vers[0] if len(vers) >= 1 else '0')
        self.minor_ = int(vers[1] if len(vers) >= 2 else '0')
        self.patch_ = int(vers[2] if len(vers) >= 3 else '0')
        BACKUP.clear()
    def major(self):
        BACKUP.append(f"{self.major_}.{self.minor_}.{self.patch_}")
        self.major_ += 1
        self.minor_, self.patch_ = 0, 0
        return self
    def minor(self):
        BACKUP.append(f"{self.major_}.{self.minor_}.{self.patch_}")
        self.minor_ += 1
        self.patch_ = 0
        return self
    def patch(self):
        BACKUP.append(f"{self.major_}.{self.minor_}.{self.patch_}")
        self.patch_ += 1
        return self
    def rollback(self):
        if not BACKUP:
            raise ValueError('Cannot rollback!')
        self.major_, self.minor_, self.patch_ = [int(i) for i in BACKUP.pop().split('.')]
        return self
    def release(self):
        return f"{self.major_}.{self.minor_}.{self.patch_}"