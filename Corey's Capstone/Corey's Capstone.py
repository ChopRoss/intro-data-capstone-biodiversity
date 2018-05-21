
# coding: utf-8

# In[1]:


from matplotlib import pyplot as plt
import pandas as pd


# In[2]:


species = pd.read_csv('species_info.csv')


# In[3]:


species.head()


# In[4]:


species.scientific_name.nunique()


# In[5]:


species.category.unique()


# In[6]:


species.conservation_status.unique()


# In[7]:


species.groupby('conservation_status').scientific_name.nunique().reset_index()


# In[8]:


species.fillna('No Intervention', inplace=True)


# In[9]:


species.groupby('conservation_status').scientific_name.nunique().reset_index()


# In[10]:


protection_counts = species.groupby('conservation_status')    .scientific_name.nunique().reset_index()    .sort_values(by='scientific_name')


# In[11]:


plt.figure(figsize=(10, 4))
ax = plt.subplot()
plt.bar(range(len(protection_counts)),
        protection_counts.scientific_name.values)
ax.set_xticks(range(len(protection_counts)))
ax.set_xticklabels(protection_counts.conservation_status.values)
plt.ylabel('Number of Species')
plt.title('Conservation Status by Species')
plt.show()


# In[12]:


species['is_protected'] = species.conservation_status != 'No Intervention'


# In[13]:


category_counts = species.groupby(['category', 'is_protected'])                         .scientific_name.nunique().reset_index()


# In[14]:


category_counts.head()


# In[15]:


category_pivot = category_counts.pivot(columns='is_protected',
                                      index='category',
                                      values='scientific_name')\
                                .reset_index()


# In[16]:


category_pivot


# In[17]:


category_pivot.columns = ['category', 'not_protected', 'protected']


# In[18]:


category_pivot['percent_protected'] = category_pivot.protected /                                       (category_pivot.protected + category_pivot.not_protected)


# In[19]:


category_pivot


# In[20]:


contingency = [[30, 146],
              [75, 413]]


# In[21]:


from scipy.stats import chi2_contingency


# In[22]:


chi2_contingency(contingency)


# In[23]:


contingency = [[30, 146],
               [5, 73]]
chi2_contingency(contingency)


# In[25]:


observations = pd.read_csv('observations.csv')
observations.head()


# In[26]:


# Does "Sheep" occur in this string?
str1 = 'This string contains Sheep'
'Sheep' in str1


# In[27]:


# Does "Sheep" occur in this string?
str2 = 'This string contains Cows'
'Sheep' in str2


# In[28]:


species['is_sheep'] = species.common_names.apply(lambda x: 'Sheep' in x)
species.head()


# In[29]:


species[species.is_sheep]


# In[30]:


sheep_species = species[(species.is_sheep) & (species.category == 'Mammal')]
sheep_species


# In[31]:


sheep_observations = observations.merge(sheep_species)
sheep_observations


# In[32]:


obs_by_park = sheep_observations.groupby('park_name').observations.sum().reset_index()
obs_by_park


# In[33]:


plt.figure(figsize=(16, 4))
ax = plt.subplot()
plt.bar(range(len(obs_by_park)),
        obs_by_park.observations.values)
ax.set_xticks(range(len(obs_by_park)))
ax.set_xticklabels(obs_by_park.park_name.values)
plt.ylabel('Number of Observations')
plt.title('Observations of Sheep per Week')
plt.show()


# In[34]:


minimum_detectable_effect = 100 * 0.05 / 0.15
minimum_detectable_effect


# In[35]:


baseline = 15


# In[36]:


sample_size = 520


# In[39]:


bryce = 520 / 250.
yellowstone = 520 / 507.

#About 2.5 weeks at Bryce and 1 week at Yellowstone

