# High Level Analyzer
# For more information and documentation, please go to https://support.saleae.com/extensions/high-level-analyzer-extensions

from saleae.analyzers import HighLevelAnalyzer, AnalyzerFrame, StringSetting, NumberSetting, ChoicesSetting


# High level analyzers must subclass the HighLevelAnalyzer class.
class Hla(HighLevelAnalyzer):

    def __init__(self):
        '''
        Initialize HLA.

        Settings can be accessed using the same name used above.
        '''

    def decode(self, frame: AnalyzerFrame):
        '''
        Process a frame from the input analyzer, and optionally return a single `AnalyzerFrame` or a list of `AnalyzerFrame`s.

        The type and data values in `frame` will depend on the input analyzer.
        '''

        # check all keys. If any of them are byte arrays, convert them to integers.
        for key in frame.data:
            value = frame.data[key]
            if(isinstance(value, bytes)):
                int_val = int.from_bytes(value, "big") # Tested with the SPI analyzer, with 16 bit word size. This appears to be the correct endianness.
                frame.data[key] = int_val

        # Return the data frame itself
        return AnalyzerFrame(frame.type, frame.start_time, frame.end_time, frame.data)
