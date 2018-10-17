path_to_file='/home/suleman/Downloads/citation.txt'

def citation(path_to_file):
    f = open(path_to_file, 'r')
    file = f.read()
    ans=[]
    sublist=''
    i=0
    while i < len(file):
        if file[i]=='#' and file[i+1]=='*':
            if sublist:
                ans.append(sublist)
                sublist=''
            sublist+=file[i]
        else:
            sublist+=file[i]
        i+=1

    record=[]
    for i in ans:
        year_start=i.find('#t')
        year=i[year_start+2:year_start+6]

        name_start=i.find('#*')
        name_end=i.find('#@')
        name=i[name_start+2:name_end]

        author_start=i.find('#@')
        if i.find(' #t')!=-1:
            author_end = i.find(' #t')
        else:
            author_end = i.find('#t')
        author=i[author_start+2:author_end]

        index_id_start=i.find('#index')
        index_id=i[index_id_start+6:i.find('/n')-1]

        publication_venue_start=i.find('#c')
        if publication_venue_start!=-1:
            publication_venue=i[publication_venue_start+2:i.find('#index')]
        else:
            publication_venue=''


        record.append({index_id:{'name':name, 'author':author, 'publication_year':int(year), 'publication venue':publication_venue}})
    return record

def paper_check(year1, year2):
    number_of_papers=0
    record = citation(path_to_file)
    for dic in record:
        for key in dic:
            for i in dic[key]:
                if i=='publication_year':
                    if dic[key][i] in range(year1, year2+1):
                        number_of_papers+=1
    return number_of_papers

print(paper_check(1970, 1980))
print(paper_check(1981, 1990))
print(paper_check(1991, 2000))
print(paper_check(2001, 2010))
print(paper_check(2011, 2018))

def co_authors(author):
    record = citation(path_to_file)
    authors_list=[]
    for dic in record:
        for key in dic:
            for i in dic[key]:
                if i=='author':
                    if author in dic[key][i]:
                        if ',' in dic[key][i]:
                            authors_list+=(dic[key][i].split(','))
    authors_list.remove(author)
    return authors_list
print(co_authors('Marc Sturm'))


def author_contribution(author, year):
    record = citation(path_to_file)
    ans=0
    for dic in record:
        for key in dic:
            for i in dic[key]: #iterating keys
                if dic[key][i]==year:   #iterating values
                    if author in dic[key]['author']: #searching value
                        ans+=(1/100)*100
    ans=str(ans)+str('%')
    return ans
print(author_contribution('Hoon Hong', 2006))

def common_co_author(author1, author2):
    common_author1 = co_authors(author1)
    common_author2 = co_authors(author2)

    all_commont_authors=[]
    for i in common_author1:
        if i in common_author2:
            all_commont_authors.append(i)


    return all_commont_authors

print(common_co_author('David Eppstein', 'Christian Scheideler'))
