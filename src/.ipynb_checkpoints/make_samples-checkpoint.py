# takes as input parameters, spits out a dataframe with the requested data
def make_samples(df, freq, periods, fun):
    
    # first sample's index
    start_time = df.index.min()
    
    sample_idx = pd.date_range(start=start_time, freq=freq, periods=periods)
    output_idx = pd.date_range(start=sample_idx.max(), end=df.index.max(), freq=freq)
    output = pd.DataFrame(columns=['load'], index=output_idx)
                          
    for i in output_idx:
    
        # try to find samples in original df, if not, skip?
        try:
            output.loc[i] = get_value(df, sample_idx, fun)
            
        # if any of the sample_idx do not exist in df, skip and calculate next
        # this leaves the value as NaN in output
        except:
            pass
        
        # iterate time delta by one freq unit                  
        start_time = start_time + pd.Timedelta(1, freq)
        
        #update sample_idx
        sample_idx = pd.date_range(start=start_time, freq=freq, periods=periods)
    
    return output