import pandas as pd

class out_formats:
    def get_output(self, data, output_type, outfile):
        if output_type=="meta":
            return data
        else:
            data=data['objs']
        if output_type=="dict":
            return data
        elif output_type=="pd":
            print(data)
            return self.as_pd(data)
        elif output_type=="np":
            return self.as_np(data)
        elif output_type=="csv":
            return self.as_csv(data, outfile)
        elif output_type=="tab":
            return self.as_tab(data, outfile)

    def as_pd(self, data):
        return pd.DataFrame(data)

    def as_np(self, data):
        return self.as_pd(data).to_numpy()

    def as_csv(self, data, outfile):
        self.as_pd(data).to_csv(outfile+'.csv', index=False)
        return data

    def as_tab(self, data, outfile):
        self.as_pd(data).to_csv(outfile+'.tab', sep='\t', index=False)
        return data
