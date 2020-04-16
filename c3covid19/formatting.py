import pandas as pd

class out_formats:
    def get_output(self, data, output_type, outfile):
        """
        Takes in the following required kwargs:

        - data:
            - Type: List of Dictionaries
        - output_type:
            - Type: String
            - What: The output data or file type
            - Choices:
                - all: A dictionary with all returned data
                - objs: Python list of the returned `objs`
                - pd: Pandas DF of the returned `objs`
                - np: Numpy Array of the returned `objs`
                - csv: Writes a csv and returns python list of the returned `objs`
                - tab: Writes a tab and returns python list of the returned `objs`
        - outfile:
            - Type: String
            - What: The file path to output to
            - Example: "../my_output"
            - Note: Do not include the file extension
            - Note: Is only used in `csv` and `tab` `output_type`s


        Returns a pandas data frame of the input list
        """
        if output_type=="all":
            return data
        if 'result' in data:
            data=data['result']
        else:
            data=data['objs']
        if output_type=="objs":
            return data
        elif output_type=="pd":
            return self.as_pd(data)
        elif output_type=="np":
            return self.as_np(data)
        elif output_type=="csv":
            return self.as_csv(data, outfile)
        elif output_type=="tab":
            return self.as_tab(data, outfile)

    def as_pd(self, data):
        """
        Takes in the following required kwargs:

        - data:
            - Type: List of Dictionaries || Dictionary

        Returns a pandas data frame of the input list
        """
        return pd.DataFrame(data)

    def as_np(self, data):
        """
        Takes in the following required kwargs:

        - data:
            - Type: List of Dictionaries

        Returns a numpy array of the input list
        """
        return self.as_pd(data).to_numpy()

    def as_csv(self, data, outfile):
        """
        Takes in the following required kwargs:

        - data:
            - Type: List of Dictionaries
        - outfile:
            - Type: String
            - What: The file path to output a csv
            - Example: "../my_output"
            - Note: Do not include the .csv extension

        Generates the specified CSV

        Returns the input data
        """
        self.as_pd(data).to_csv(outfile+'.csv', index=False)
        return data

    def as_tab(self, data, outfile):
        """
        Takes in the following required kwargs:

        - data:
            - Type: List of Dictionaries
        - outfile:
            - Type: String
            - What: The file path to output a tab file
            - Example: "../my_output"
            - Note: Do not include the .tab extension

        Generates the specified TAB file

        Returns the input data
        """
        self.as_pd(data).to_csv(outfile+'.tab', sep='\t', index=False)
        return data
