# BERTScore
BERTScore [1] is a reference-based evaluation metric based on calculating the similarity of two summaries' BERT embeddings.
The name for this metric is `bertscore`.

## Setting Up
BERTScore can be installed via pip:
```bash
pip install bert_score
```
The environment we used to successfully run the metric is provided in "environments/bertscore.yml".

To verify your installation, run:
```bash
pytest sacrerouge/tests/metrics/bertscore_test.py
```

## Correlations
Here are the correlations of BERTScore as implemented in SacreROUGE to the "overall responsiveness" human judgments on several datasets.

Summary-level, peers only:
<table>
<tr>
<th></th>
<th colspan="3">TAC2008</th>
<th colspan="3">TAC2009</th>
<th colspan="3">TAC2010</th>
<th colspan="3">TAC2011</th>
</tr>
<tr>
<th></th>
<th>r</th>
<th>p</th>
<th>k</th>
<th>r</th>
<th>p</th>
<th>k</th>
<th>r</th>
<th>p</th>
<th>k</th>
<th>r</th>
<th>p</th>
<th>k</th>
</tr>
<tr>
<td>BERTScore-P</td>
<td>0.43</td>
<td>0.43</td>
<td>0.34</td>
<td>0.49</td>
<td>0.50</td>
<td>0.40</td>
<td>0.57</td>
<td>0.58</td>
<td>0.47</td>
<td>0.46</td>
<td>0.47</td>
<td>0.38</td>
</tr>
<tr>
<td>BERTScore-R</td>
<td>0.50</td>
<td>0.50</td>
<td>0.40</td>
<td>0.51</td>
<td>0.54</td>
<td>0.43</td>
<td>0.63</td>
<td>0.63</td>
<td>0.52</td>
<td>0.45</td>
<td>0.53</td>
<td>0.43</td>
</tr>
<tr>
<td>BERTScore-F1</td>
<td>0.49</td>
<td>0.48</td>
<td>0.39</td>
<td>0.51</td>
<td>0.54</td>
<td>0.43</td>
<td>0.63</td>
<td>0.63</td>
<td>0.51</td>
<td>0.45</td>
<td>0.52</td>
<td>0.42</td>
</tr>
</table>

Summary-level, peers + references:
<table>
<tr>
<th></th>
<th colspan="3">TAC2008</th>
<th colspan="3">TAC2009</th>
<th colspan="3">TAC2010</th>
<th colspan="3">TAC2011</th>
</tr>
<tr>
<th></th>
<th>r</th>
<th>p</th>
<th>k</th>
<th>r</th>
<th>p</th>
<th>k</th>
<th>r</th>
<th>p</th>
<th>k</th>
<th>r</th>
<th>p</th>
<th>k</th>
</tr>
<tr>
<td>BERTScore-P</td>
<td>0.55</td>
<td>0.51</td>
<td>0.41</td>
<td>0.52</td>
<td>0.57</td>
<td>0.45</td>
<td>0.63</td>
<td>0.65</td>
<td>0.53</td>
<td>0.42</td>
<td>0.53</td>
<td>0.43</td>
</tr>
<tr>
<td>BERTScore-R</td>
<td>0.63</td>
<td>0.59</td>
<td>0.48</td>
<td>0.57</td>
<td>0.62</td>
<td>0.50</td>
<td>0.70</td>
<td>0.71</td>
<td>0.59</td>
<td>0.41</td>
<td>0.61</td>
<td>0.50</td>
</tr>
<tr>
<td>BERTScore-F1</td>
<td>0.62</td>
<td>0.57</td>
<td>0.46</td>
<td>0.56</td>
<td>0.62</td>
<td>0.50</td>
<td>0.69</td>
<td>0.70</td>
<td>0.58</td>
<td>0.41</td>
<td>0.58</td>
<td>0.48</td>
</tr>
</table>

System-level, peers only:
<table>
<tr>
<th></th>
<th colspan="3">TAC2008</th>
<th colspan="3">TAC2009</th>
<th colspan="3">TAC2010</th>
<th colspan="3">TAC2011</th>
</tr>
<tr>
<th></th>
<th>r</th>
<th>p</th>
<th>k</th>
<th>r</th>
<th>p</th>
<th>k</th>
<th>r</th>
<th>p</th>
<th>k</th>
<th>r</th>
<th>p</th>
<th>k</th>
</tr>
<tr>
<td>BERTScore-P</td>
<td>0.75</td>
<td>0.80</td>
<td>0.60</td>
<td>0.77</td>
<td>0.90</td>
<td>0.74</td>
<td>0.87</td>
<td>0.91</td>
<td>0.76</td>
<td>0.78</td>
<td>0.77</td>
<td>0.61</td>
</tr>
<tr>
<td>BERTScore-R</td>
<td>0.83</td>
<td>0.85</td>
<td>0.68</td>
<td>0.72</td>
<td>0.91</td>
<td>0.75</td>
<td>0.85</td>
<td>0.93</td>
<td>0.79</td>
<td>0.77</td>
<td>0.87</td>
<td>0.69</td>
</tr>
<tr>
<td>BERTScore-F1</td>
<td>0.82</td>
<td>0.86</td>
<td>0.66</td>
<td>0.75</td>
<td>0.92</td>
<td>0.76</td>
<td>0.88</td>
<td>0.93</td>
<td>0.79</td>
<td>0.78</td>
<td>0.85</td>
<td>0.69</td>
</tr>
</table>

System-level, peers + references:
<table>
<tr>
<th></th>
<th colspan="3">TAC2008</th>
<th colspan="3">TAC2009</th>
<th colspan="3">TAC2010</th>
<th colspan="3">TAC2011</th>
</tr>
<tr>
<th></th>
<th>r</th>
<th>p</th>
<th>k</th>
<th>r</th>
<th>p</th>
<th>k</th>
<th>r</th>
<th>p</th>
<th>k</th>
<th>r</th>
<th>p</th>
<th>k</th>
</tr>
<tr>
<td>BERTScore-P</td>
<td>0.88</td>
<td>0.86</td>
<td>0.67</td>
<td>0.70</td>
<td>0.93</td>
<td>0.77</td>
<td>0.86</td>
<td>0.94</td>
<td>0.80</td>
<td>0.50</td>
<td>0.85</td>
<td>0.70</td>
</tr>
<tr>
<td>BERTScore-R</td>
<td>0.93</td>
<td>0.89</td>
<td>0.74</td>
<td>0.68</td>
<td>0.94</td>
<td>0.80</td>
<td>0.87</td>
<td>0.95</td>
<td>0.83</td>
<td>0.49</td>
<td>0.92</td>
<td>0.76</td>
</tr>
<tr>
<td>BERTScore-F1</td>
<td>0.92</td>
<td>0.89</td>
<td>0.72</td>
<td>0.69</td>
<td>0.94</td>
<td>0.79</td>
<td>0.87</td>
<td>0.96</td>
<td>0.83</td>
<td>0.50</td>
<td>0.90</td>
<td>0.76</td>
</tr>
</table>

## References
[1] Tianyi Zhang, Varsha Kishore, Felix Wu, Kilian Q.Weinberger, and Yoav Artzi. [BERTScore: Evaluating Text Generation with BERT](https://arxiv.org/abs/1904.09675). ICLR 2020.