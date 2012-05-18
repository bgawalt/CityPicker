# HEY HEY! This file starts by defining this big data structure
# in a hard-coded way. You should just jump to the end of the file,
# only the final hundred lines or so actually do anything.

zipdata = """Westwood, NJ (07675)	24083
Woodcliff Lake, NJ (07677)	5471
Wharton, NJ (07885)	8999
Whippany, NJ (07981)	8057
Whitehouse Station, NJ (08889)	8570
Woodbridge, NJ (07095)	17272
Wyckoff, NJ (07481)	15208
Bronx, NY (10451)	31477
Bronx, NY (10452)	56277
Bronx, NY (10453)	57691
Bronx, NY (10454)	22387
Bronx, NY (10455)	25139
Bronx, NY (10456)	58750
Bronx, NY (10457)	48779
Bronx, NY (10458)	50085
Bronx, NY (10459)	30434
Bronx, NY (10460)	39507
Bronx, NY (10461)	35421
Bronx, NY (10462)	57854
Bronx, NY (10463)	50313
Bronx, NY (10464)	3381
Bronx, NY (10465)	30798
Bronx, NY (10466)	47658
Bronx, NY (10467)	64907
Bronx, NY (10468)	55824
Bronx, NY (10469)	47625
Bronx, NY (10470)	10880
Bronx, NY (10471)	15606
Bronx, NY (10472)	43761
Bronx, NY (10473)	42812
Bronx, NY (10474)	7377
Bronx, NY (10475)	31659
New York, NY (10001)	16553
New York, NY (10002)	70604
New York, NY (10003)	36569
New York, NY (10004)	2909
New York, NY (10005)	6293
New York, NY (10006)	2849
New York, NY (10007)	5396
New York, NY (10009)	42731
New York, NY (10010)	22785
New York, NY (10011)	38784
New York, NY (10012)	17738
New York, NY (10013)	24199
New York, NY (10014)	24292
New York, NY (10016)	40683
New York, NY (10017)	19975
New York, NY (10018)	5928
New York, NY (10019)	31889
New York, NY (10020)	1926
New York, NY (10021)	42627
New York, NY (10022)	29014
New York, NY (10023)	48044
New York, NY (10024)	47261
New York, NY (10025)	70190
New York, NY (10026)	24221
New York, NY (10027)	37948
New York, NY (10028)	36525
New York, NY (10029)	48403
New York, NY (10030)	17771
New York, NY (10031)	40901
New York, NY (10032)	45758
New York, NY (10033)	45474
New York, NY (10034)	32614
Belmont, MA (02478)	21169
Brookline, MA (02445)	16149
Brookline, MA (02446)	21302
Lexington, MA (02420)	13148
Lexington, MA (02421)	15237
Needham, MA (02492)	17587
Needham Heights, MA (02494)	7910
Newton, MA (02458)	10355
Newton Center, MA (02459)	16153
Newtonville, MA (02460)	7764
Newton Highlands, MA (02461)	6253
Newton Lower Falls, MA (02462)	1184
Newton Upper Falls, MA (02464)	2480
West Newton, MA (02465)	10288
Auburndale, MA (02466)	5838
Chestnut Hill, MA (02467)	13071
Waban, MA (02468)	5140
Waltham, MA (02451)	14526
Waltham, MA (02452)	9731
Waltham, MA (02453)	20076
Watertown, MA (02472)	26221
Wellesley Hills, MA (02481)	13012
Wellesley, MA (02482)	8821
Weston, MA (02493)	9839
Braintree, MA (02184)	30406
Milton, MA (02186)	22628
Quincy, MA (02169)	43214
Quincy, MA (02170)	16193
Quincy, MA (02171)	15503
Weymouth, MA (02188)	12116
East Weymouth, MA (02189)	11769
South Weymouth, MA (02190)	13851
North Weymouth, MA (02191)	7287
Village Of Nagog Woods, MA (01718)	580
Boxborough, MA (01719)	4749
Acton, MA (01720)	19114
Arlington, MA (02474)	22275
Arlington, MA (02476)	14383
Chelsea, MA (02150)	23718
Everett, MA (02149)	30367
Winthrop, MA (02152)	14181
Revere, MA (02151)	38954
Malden, MA (02148)	47104
Melrose, MA (02176)	23311
Medford, MA (02155)	44783
Somerville, MA (02143)	18622
Somerville, MA (02144)	18051
Somerville, MA (02145)	18704
Stoneham, MA (02180)	19086
Amesbury, MA (01913)	14037
Andover, MA (01810)	30346
Millis, MA (02054)	7110
Millville, MA (01529)	2734
Nantucket, MA (02554)	7752
Natick, MA (01760)	28611
New Braintree, MA (01531)	865
Newburyport, MA (01950)	15198
Newbury, MA (01951)	3207
Salisbury, MA (01952)	6787
Norfolk, MA (02056)	8410
Abington, MA (02351)	13780
North Billerica, MA (01862)	8263
Northborough, MA (01532)	13113
Northbridge, MA (01534)	4939
North Brookfield, MA (01535)	3925
North Chatham, MA (02650)	861
North Chelmsford, MA (01863)	7753
North Easton, MA (02356)	10331
North Falmouth, MA (02556)	3327
North Grafton, MA (01536)	5828
North Oxford, MA (01537)	1951
North Reading, MA (01864)	13411
Ashburnham, MA (01430)	5364
Ashby, MA (01431)	2749
Ashland, MA (01721)	14769
Auburn, MA (01501)	14232
Avon, MA (02322)	3831
Ayer, MA (01432)	6017
Baldwinville, MA (01436)	2457
Barnstable, MA (02630)	1895
Bedford, MA (01730)	11940
Hanscom Afb, MA (01731)	1343
Bellingham, MA (02019)	14707
Berlin, MA (01503)	2462
Beverly, MA (01915)	31324
Billerica, MA (01821)	26961
Blackstone, MA (01504)	7808
Bolton, MA (01740)	4456
Boston, MA (02108)	3312
Boston, MA (02109)	4145
Boston, MA (02110)	4313
Boston, MA (02111)	4467
Boston, MA (02113)	4799
Boston, MA (02114)	8116
Boston, MA (02115)	9923
Boston, MA (02116)	13687
Boston, MA (02118)	16795
Roxbury, MA (02119)	17302
Roxbury Crossing, MA (02120)	7048
Dorchester, MA (02121)	16415
Dorchester, MA (02122)	16592
Dorchester Center, MA (02124)	33570
Dorchester, MA (02125)	22994
Mattapan, MA (02126)	19266
Boston, MA (02127)	24051
Boston, MA (02128)	27419
Charlestown, MA (02129)	13311
Jamaica Plain, MA (02130)	27060
Roslindale, MA (02131)	23881
West Roxbury, MA (02132)	21756
Allston, MA (02134)	12051
Brighton, MA (02135)	27370
Hyde Park, MA (02136)	23209
Boston, MA (02163)	723
Boston, MA (02199)	1239
Boston, MA (02210)	1495
Boston, MA (02215)	7098
Boxford, MA (01921)	7331
Boylston, MA (01505)	3993
Brewster, MA (02631)	8575
Bridgewater, MA (02324)	19223
Brockton, MA (02301)	44024
Brockton, MA (02302)	25132
Brookfield, MA (01506)	2920
Burlington, MA (01803)	22104
Buzzards Bay, MA (02532)	8780
Buzzards Bay, MA (02542)	581
Byfield, MA (01922)	2848
Cambridge, MA (02138)	21578
Cambridge, MA (02139)	25969
Cambridge, MA (02140)	14277
Cambridge, MA (02141)	8418
Cambridge, MA (02142)	2011
Canton, MA (02021)	18954
Carlisle, MA (01741)	4692
Carver, MA (02330)	9328
Centerville, MA (02632)	9476
Charlton, MA (01507)	10873
Chatham, MA (02633)	3482
Chelmsford, MA (01824)	23196
Chilmark, MA (02535)	1000
Clinton, MA (01510)	11365
Cohasset, MA (02025)	6515
Concord, MA (01742)	15042
Cotuit, MA (02635)	3159
Norwell, MA (02061)	9372
Norwood, MA (02062)	24326
Oak Bluffs, MA (02557)	2451
Orleans, MA (02653)	4418
Osterville, MA (02655)	3222
Oxford, MA (01540)	9660
Peabody, MA (01960)	43688
Pembroke, MA (02359)	15037
Pepperell, MA (01463)	10100
Plymouth, MA (02360)	44333
Plympton, MA (02367)	2488
Pocasset, MA (02559)	2864
Princeton, MA (01541)	3224
Provincetown, MA (02657)	3084
Randolph, MA (02368)	26599
Reading, MA (01867)	21499
Rochdale, MA (01542)	1907
Rockland, MA (02370)	14690
Rockport, MA (01966)	6287
Rowley, MA (01969)	5259
Rutland, MA (01543)	6893
Sagamore Beach, MA (02562)	2870
Salem, MA (01970)	32194
Sandwich, MA (02563)	9499
Scituate, MA (02066)	14992
Sharon, MA (02067)	16154
Sherborn, MA (01770)	3937
Shirley, MA (01464)	5028
Shrewsbury, MA (01545)	30759
Fayville, MA (01745)	430
Southborough, MA (01772)	8678
Southbridge, MA (01550)	13355
South Chatham, MA (02659)	985
South Dennis, MA (02660)	5219
South Easton, MA (02375)	8528
South Grafton, MA (01560)	3675
South Hamilton, MA (01982)	6501
South Walpole, MA (02071)	934
South Yarmouth, MA (02664)	8289
West Yarmouth, MA (02673)	6986
Spencer, MA (01562)	9747
Sterling, MA (01564)	7104
Stoughton, MA (02072)	23389
Stow, MA (01775)	6132
Fiskdale, MA (01518)	2639
Sturbridge, MA (01566)	5934
Sudbury, MA (01776)	16252
Sutton, MA (01590)	7702
Templeton, MA (01468)	3579
Tewksbury, MA (01876)	25645
Topsfield, MA (01983)	5449
Townsend, MA (01469)	6266
West Townsend, MA (01474)	1866
Tyngsboro, MA (01879)	10293
Uxbridge, MA (01569)	11159
Vineyard Haven, MA (02568)	5903
Wakefield, MA (01880)	22162
Walpole, MA (02081)	16471
Wareham, MA (02571)	8360
Wayland, MA (01778)	12273
Webster, MA (01570)	13308
Dudley, MA (01571)	9200
Wellfleet, MA (02667)	2145
Danvers, MA (01923)	23360
Dedham, MA (02026)	20528
Dennis, MA (02638)	2894
Dennis Port, MA (02639)	2683
Dover, MA (02030)	5123
Dracut, MA (01826)	26388
Dunstable, MA (01827)	2850
Duxbury, MA (02332)	11874
East Bridgewater, MA (02333)	11875
East Brookfield, MA (01515)	1985
Douglas, MA (01516)	7565
East Falmouth, MA (02536)	16726
Eastham, MA (02642)	3336
East Sandwich, MA (02537)	5529
East Walpole, MA (02032)	3705
East Wareham, MA (02538)	3657
Edgartown, MA (02539)	4236
Essex, MA (01929)	2928
Falmouth, MA (02540)	5909
Woods Hole, MA (02543)	834
Holland, MA (01521)	2069
Fitchburg, MA (01420)	28652
Forestdale, MA (02644)	3812
Foxboro, MA (02035)	14783
Framingham, MA (01701)	27821
Framingham, MA (01702)	23402
Franklin, MA (02038)	27220
Gardner, MA (01440)	15067
Gloucester, MA (01930)	23856
Grafton, MA (01519)	6093
Groton, MA (01450)	9198
Halifax, MA (02338)	6682
Hanover, MA (02339)	12397
Hanson, MA (02341)	8504
Harvard, MA (01451)	4672
Harwich, MA (02645)	8325
Harwich Port, MA (02646)	1742
Haverhill, MA (01830)	19190
Haverhill, MA (01832)	17585
Georgetown, MA (01833)	7314
Groveland, MA (01834)	5915
Haverhill, MA (01835)	11875
Hingham, MA (02043)	19512
Holbrook, MA (02343)	9085
Holden, MA (01520)	12865
Holliston, MA (01746)	12696
Hopedale, MA (01747)	5323
Hopkinton, MA (01748)	13078
Hubbardston, MA (01452)	3932
Hudson, MA (01749)	16503
Hull, MA (02045)	8990
Hyannis, MA (02601)	10685
Ipswich, MA (01938)	11683
Jefferson, MA (01522)	2984
Lancaster, MA (01523)	4777
Lawrence, MA (01840)	3383
Lawrence, MA (01841)	33432
Lawrence, MA (01843)	18352
Methuen, MA (01844)	40836
North Andover, MA (01845)	24329
Leicester, MA (01524)	5678
Leominster, MA (01453)	34034
Lincoln, MA (01773)	4870
Littleton, MA (01460)	8001
Lowell, MA (01850)	11001
Lowell, MA (01851)	23694
Lowell, MA (01852)	23950
Lowell, MA (01854)	17446
Lunenburg, MA (01462)	9073
Lynn, MA (01901)	1155
Lynn, MA (01902)	30268
Lynn, MA (01904)	15967
Lynn, MA (01905)	18244
Saugus, MA (01906)	23413
Swampscott, MA (01907)	12470
Nahant, MA (01908)	3119
Lynnfield, MA (01940)	10993
Manchester, MA (01944)	4620
Mansfield, MA (02048)	20294
Marblehead, MA (01945)	18127
Marlborough, MA (01752)	31660
Marshfield, MA (02050)	19432
Marstons Mills, MA (02648)	6749
Mashpee, MA (02649)	12354
Maynard, MA (01754)	8873
Medfield, MA (02052)	11150
Medway, MA (02053)	11358
Mendon, MA (01756)	5234
Merrimac, MA (01860)	5611
Middleboro, MA (02346)	19462
Middleton, MA (01949)	6965
Milford, MA (01757)	22801
Millbury, MA (01527)	11467
Wenham, MA (01984)	3350
West Barnstable, MA (02668)	2937
Westborough, MA (01581)	16691
West Boylston, MA (01583)	5947
West Bridgewater, MA (02379)	6030
West Brookfield, MA (01585)	3585
West Dennis, MA (02670)	1294
Westford, MA (01886)	20376
West Harwich, MA (02671)	971
Westminster, MA (01473)	6741
West Newbury, MA (01985)	3927
Upton, MA (01568)	6440
West Wareham, MA (02576)	3479
Westwood, MA (02090)	13095
Whitinsville, MA (01588)	7937
Whitman, MA (02382)	12411
Wilmington, MA (01887)	20129
Winchendon, MA (01475)	7879
Winchester, MA (01890)	19213
Woburn, MA (01801)	33608
Worcester, MA (01602)	18196
Worcester, MA (01603)	14610
Worcester, MA (01604)	26294
Worcester, MA (01605)	18175
Worcester, MA (01606)	16439
Worcester, MA (01607)	6146
Worcester, MA (01608)	2396
Worcester, MA (01609)	11815
Worcester, MA (01610)	12571
Cherry Valley, MA (01611)	1777
Paxton, MA (01612)	3934
Wrentham, MA (02093)	9499
Yarmouth Port, MA (02675)	5862
Kingston, MA (02364)	10556
Lakeville, MA (02347)	9319
Abbot, ME (04406)	563
Acton, ME (04001)	1934
Addison, ME (04606)	907
Albion, ME (04910)	1695
Alfred, ME (04002)	6087
Alna, ME (04535)	660
Andover, ME (04216)	560
Anson, ME (04911)	1529
Ashland, ME (04732)	1375
Athens, ME (04912)	749
Auburn, ME (04210)	17123
Augusta, ME (04330)	19658
Bangor, ME (04401)	32132
Bar Harbor, ME (04609)	3867
Bass Harbor, ME (04653)	473
Bath, ME (04530)	9208
Belfast, ME (04915)	6997
Belgrade, ME (04917)	2621
Berwick, ME (03901)	6250
Bethel, ME (04217)	2781
Biddeford, ME (04005)	17466
Bingham, ME (04920)	1204
Blue Hill, ME (04614)	2393
Boothbay, ME (04537)	1894
Boothbay Harbor, ME (04538)	1709
Bowdoinham, ME (04008)	2627
Bradford, ME (04410)	932
Bradley, ME (04411)	1240
Brewer, ME (04412)	8103
Bridgewater, ME (04735)	463
Bridgton, ME (04009)	3643
Bristol, ME (04539)	909
Brooklin, ME (04616)	717
Brooks, ME (04921)	1240
Brooksville, ME (04617)	698
Brownfield, ME (04010)	1171
Brownville, ME (04414)	875
Brunswick, ME (04011)	16573
Bryant Pond, ME (04219)	1131
Buckfield, ME (04220)	2457
Bucksport, ME (04416)	4629
Burnham, ME (04922)	849
Calais, ME (04619)	2726
Camden, ME (04843)	4295
Hope, ME (04847)	1253
Canaan, ME (04924)	1708
Canton, ME (04221)	686
Cape Neddick, ME (03902)	2032
Greenbush, ME (04418)	1257
Caribou, ME (04736)	7868
Carmel, ME (04419)	2343
Casco, ME (04015)	2620
Castine, ME (04421)	647
Charleston, ME (04422)	928
Cherryfield, ME (04622)	956
Clinton, ME (04927)	2755
Columbia Falls, ME (04623)	788
Corinna, ME (04928)	1648
Cornish, ME (04020)	1211
Cumberland Center, ME (04021)	5630
Cushing, ME (04563)	1132
Damariscotta, ME (04543)	1996
Danforth, ME (04424)	584
Deer Isle, ME (04627)	1267
Denmark, ME (04022)	913
Dennysville, ME (04628)	472
Detroit, ME (04929)	687
Dexter, ME (04930)	3161
Dixfield, ME (04224)	2314
Dixmont, ME (04932)	994
Dover Foxcroft, ME (04426)	3592
Dresden, ME (04342)	1392
Eagle Lake, ME (04739)	737
East Baldwin, ME (04024)	522
East Boothbay, ME (04544)	702
Corinth, ME (04427)	2287
Eddington, ME (04428)	2514
Holden, ME (04429)	4302
Lebanon, ME (04027)	4853
East Machias, ME (04630)	1265
East Millinocket, ME (04430)	1351
Easton, ME (04740)	1028
Eastport, ME (04631)	991
Sebago, ME (04029)	1421
East Waterboro, ME (04030)	1767
Eliot, ME (03903)	5703
Ellsworth, ME (04605)	10831
Etna, ME (04434)	1001
Exeter, ME (04435)	808
Fairfield, ME (04937)	5223
Farmington, ME (04938)	5726
Fort Fairfield, ME (04742)	2739
Fort Kent, ME (04743)	3621
Frankfort, ME (04438)	913
Franklin, ME (04634)	1427
Freedom, ME (04941)	1303
Freeport, ME (04032)	6497
Friendship, ME (04547)	940
Fryeburg, ME (04037)	2994
Farmingdale, ME (04344)	2379
Gardiner, ME (04345)	9500
Randolph, ME (04346)	1405
Garland, ME (04939)	847
Georgetown, ME (04548)	896
Gorham, ME (04038)	13280
Gouldsboro, ME (04607)	964
Gray, ME (04039)	6622
Greene, ME (04236)	3669
Greenville, ME (04441)	1328
Guilford, ME (04443)	1899
Hallowell, ME (04347)	2107
Hampden, ME (04444)	7780
Hancock, ME (04640)	1902
Harmony, ME (04942)	791
Harrington, ME (04643)	839
Harrison, ME (04040)	2409
Hartland, ME (04943)	1461
Hebron, ME (04238)	1090
Hiram, ME (04041)	1069
Hollis Center, ME (04042)	3657
Houlton, ME (04730)	7648
Howland, ME (04448)	1044
Hudson, ME (04449)	1200
Island Falls, ME (04747)	934
Islesboro, ME (04848)	514
Jackman, ME (04945)	981
Jay, ME (04239)	3759
Jefferson, ME (04348)	2279
Jonesboro, ME (04648)	499
Jonesport, ME (04649)	1012
Kenduskeag, ME (04450)	1042
Kennebunk, ME (04043)	9435
Kennebunkport, ME (04046)	6397
Kents Hill, ME (04349)	1108
Parsonsfield, ME (04047)	1573
Kingfield, ME (04947)	1429
Kittery, ME (03904)	6326
Kittery Point, ME (03905)	1725
Lagrange, ME (04453)	542
Lee, ME (04455)	704
Leeds, ME (04263)	1835
Levant, ME (04456)	2357
Lewiston, ME (04240)	24211
Liberty, ME (04949)	824
Limerick, ME (04048)	2364
Limestone, ME (04750)	1634
Limington, ME (04049)	2908
Lincoln, ME (04457)	4656
Lincolnville, ME (04849)	2902
Durham, ME (04222)	3415
Lisbon, ME (04250)	3509
Lisbon Falls, ME (04252)	4079
Litchfield, ME (04350)	2964
Livermore, ME (04253)	1754
Livermore Falls, ME (04254)	2249
Greenwood, ME (04255)	574
Lovell, ME (04051)	854
Lubec, ME (04652)	1284
Machias, ME (04654)	2410
Machiasport, ME (04655)	732
Madawaska, ME (04756)	3053
Madison, ME (04950)	3268
Manchester, ME (04351)	2445
Mapleton, ME (04757)	2246
Mars Hill, ME (04758)	1323
Mattawamkeag, ME (04459)	553
Mechanic Falls, ME (04256)	2470
Bremen, ME (04551)	604
Medway, ME (04460)	1135
Mexico, ME (04257)	1891
Milbridge, ME (04658)	1100
Milford, ME (04461)	2575
Millinocket, ME (04462)	3895
Milo, ME (04463)	2019
Minot, ME (04258)	2325
Monmouth, ME (04259)	2764
Monroe, ME (04951)	697
Monson, ME (04464)	524
Monticello, ME (04760)	624
Morrill, ME (04952)	1473
Mount Desert, ME (04660)	1327
Mount Vernon, ME (04352)	1307
Naples, ME (04055)	3239
Newcastle, ME (04553)	1700
New Gloucester, ME (04260)	4743
New Harbor, ME (04554)	688
Newport, ME (04953)	2465
New Sharon, ME (04955)	1139
New Sweden, ME (04762)	480
New Vineyard, ME (04956)	546
Nobleboro, ME (04555)	1468
Norridgewock, ME (04957)	3228
North Anson, ME (04958)	1359
North Berwick, ME (03906)	4111
Edgecomb, ME (04556)	1099
North Monmouth, ME (04265)	805
New Portland, ME (04961)	620
Sullivan, ME (04664)	965
North Waterboro, ME (04061)	2715
Whitefield, ME (04353)	1935
Windham, ME (04062)	14364
Norway, ME (04268)	3720
Oakfield, ME (04763)	639
Oakland, ME (04963)	6062
Ogunquit, ME (03907)	1331
Old Orchard Beach, ME (04064)	6985
Old Town, ME (04468)	6739
Orland, ME (04472)	1530
Orono, ME (04473)	3986
Orrington, ME (04474)	3305
Orrs Island, ME (04066)	517
Owls Head, ME (04854)	1296
Oxford, ME (04270)	4732
Palermo, ME (04354)	1214
Palmyra, ME (04965)	1479
Patten, ME (04765)	987
Pembroke, ME (04666)	938
Penobscot, ME (04476)	979
Perry, ME (04667)	1078
Phillips, ME (04966)	1247
Phippsburg, ME (04562)	1772
Pittsfield, ME (04967)	3306
Plymouth, ME (04969)	1021
Poland, ME (04274)	4297
Porter, ME (04068)	930
Portland, ME (04101)	10260
Portland, ME (04102)	12801
Portland, ME (04103)	24317
Falmouth, ME (04105)	9991
South Portland, ME (04106)	20593
Cape Elizabeth, ME (04107)	8393
Peaks Island, ME (04108)	759
Cumberland Foreside, ME (04110)	1257
Pownal, ME (04069)	1289
Presque Isle, ME (04769)	7779
Princeton, ME (04668)	1151
Rangeley, ME (04970)	1328
Raymond, ME (04071)	4331
Readfield, ME (04355)	2235
Richmond, ME (04357)	2834
Rockland, ME (04841)	5832
Rockport, ME (04856)	2928
Round Pond, ME (04564)	422
Rumford, ME (04276)	4235
Sabattus, ME (04280)	5668
Saco, ME (04072)	15839
Saint Agatha, ME (04772)	639
Saint Albans, ME (04971)	1444
Saint David, ME (04773)	581
Saint Francis, ME (04774)	519
Sanford, ME (04073)	13098
Sangerville, ME (04479)	999
Scarborough, ME (04074)	15910
Searsmont, ME (04973)	1125
Searsport, ME (04974)	2180
Sedgwick, ME (04676)	833
Shapleigh, ME (04076)	2175
Sherman, ME (04776)	719
Skowhegan, ME (04976)	7550
Smithfield, ME (04978)	849
Smyrna Mills, ME (04780)	573
Wallagrass, ME (04781)	451
Solon, ME (04979)	781
South Berwick, ME (03908)	6298
South China, ME (04358)	3382
Harpswell, ME (04079)	3440
South Paris, ME (04281)	3737
South Thomaston, ME (04858)	1256
Southwest Harbor, ME (04679)	1735
Springfield, ME (04487)	628
Springvale, ME (04083)	3911
Spruce Head, ME (04859)	679
Standish, ME (04084)	6504
Steep Falls, ME (04085)	1600
Stetson, ME (04488)	944
Steuben, ME (04680)	857
Stockton Springs, ME (04981)	1822
Stonington, ME (04681)	992
Stratton, ME (04982)	509
Strong, ME (04983)	1338
Surry, ME (04684)	1252
Temple, ME (04984)	450
Tenants Harbor, ME (04860)	1361
Thomaston, ME (04861)	2417
Thorndike, ME (04986)	1251
Topsham, ME (04086)	8014
Troy, ME (04987)	735
Turner, ME (04282)	4579
Union, ME (04862)	3128
Unity, ME (04988)	1315
Frenchville, ME (04745)	882
Van Buren, ME (04785)	1796
Vassalboro, ME (04989)	3155
Vinalhaven, ME (04863)	1016
Waldoboro, ME (04572)	4157
Warren, ME (04864)	3229
Washburn, ME (04786)	1370
Washington, ME (04574)	1240
Waterboro, ME (04087)	1989
Waterford, ME (04088)	1155
Waterville, ME (04901)	18306
Wayne, ME (04284)	1002
Wells, ME (04090)	8068
West Baldwin, ME (04091)	746
Bowdoin, ME (04287)	2575
Westbrook, ME (04092)	13620
Buxton, ME (04093)	6701
West Enfield, ME (04493)	1455
West Newfield, ME (04095)	967
West Paris, ME (04289)	1415
Peru, ME (04290)	1337
Southport, ME (04576)	556
Sumner, ME (04292)	678
Wilton, ME (04294)	2806
Windsor, ME (04363)	2013
Winter Harbor, ME (04693)	415
Winterport, ME (04496)	3247
Winthrop, ME (04364)	5014
Wiscasset, ME (04578)	3806
Baileyville, ME (04694)	2014
Woolwich, ME (04579)	2830
Yarmouth, ME (04096)	7622
North Yarmouth, ME (04097)	3254
York, ME (03909)	7886
Alstead, NH (03602)	2282
Alton, NH (03809)	3288
Alton Bay, NH (03810)	1460
Amherst, NH (03031)	10851
Andover, NH (03216)	1775
Antrim, NH (03440)	2376
Ashland, NH (03217)	1929
Atkinson, NH (03811)	6432
Auburn, NH (03032)	4763
Barnstead, NH (03218)	1040
Barrington, NH (03825)	7780
Bartlett, NH (03812)	518
Bath, NH (03740)	868
Belmont, NH (03220)	6141
Bennington, NH (03442)	1189
Berlin, NH (03570)	7523
Bethlehem, NH (03574)	2199
Bradford, NH (03221)	1901
Bristol, NH (03222)	4689
Brookline, NH (03033)	4472
Campton, NH (03223)	3750
Thornton, NH (03285)	1035
Canaan, NH (03741)	3514
Candia, NH (03034)	3789
Canterbury, NH (03224)	2165
Center Barnstead, NH (03225)	3042
Center Conway, NH (03813)	2619
Center Harbor, NH (03226)	2204
Center Ossipee, NH (03814)	1929
Center Sandwich, NH (03227)	881
Charlestown, NH (03603)	4511
Chester, NH (03036)	4295
Chesterfield, NH (03443)	635
Chocorua, NH (03817)	593
Claremont, NH (03743)	11223
Colebrook, NH (03576)	2776
Concord, NH (03301)	25391
Concord, NH (03303)	12766
Bow, NH (03304)	7129
Loudon, NH (03307)	4664
Contoocook, NH (03229)	5355
Conway, NH (03818)	3551
Cornish, NH (03745)	1083
Danbury, NH (03230)	985
Danville, NH (03819)	3663
Deerfield, NH (03037)	3869
Derry, NH (03038)	29572
Dover, NH (03820)	24060
Madbury, NH (03823)	1578
Dublin, NH (03444)	1417
Durham, NH (03824)	6150
Lee, NH (03861)	3124
East Hampstead, NH (03826)	2837
East Kingston, NH (03827)	2860
Lempster, NH (03605)	837
Sullivan, NH (03445)	655
Nelson, NH (03457)	628
Swanzey, NH (03446)	5037
East Wakefield, NH (03830)	1181
Enfield, NH (03748)	4101
Epping, NH (03042)	5578
Epsom, NH (03234)	4174
Chichester, NH (03258)	2183
Errol, NH (03579)	418
Etna, NH (03750)	1061
Exeter, NH (03833)	18286
Farmington, NH (03835)	5843
Fitzwilliam, NH (03447)	2092
Francestown, NH (03043)	1463
Franconia, NH (03580)	1362
Franklin, NH (03235)	6820
Freedom, NH (03836)	1205
Fremont, NH (03044)	3744
Gilmanton, NH (03237)	2180
Gilmanton Iron Works, NH (03837)	1175
Gilsum, NH (03448)	701
Glen, NH (03838)	1241
Goffstown, NH (03045)	11820
Dunbarton, NH (03046)	2440
Gorham, NH (03581)	2901
Goshen, NH (03752)	727
Grafton, NH (03240)	1038
Grantham, NH (03753)	3044
Greenfield, NH (03047)	1441
Greenland, NH (03840)	3475
Greenville, NH (03048)	2853
Groveton, NH (03582)	2139
Hampstead, NH (03841)	5727
Hampton, NH (03842)	13085
Hampton Falls, NH (03844)	2143
Hancock, NH (03449)	1626
Hanover, NH (03755)	6375
Harrisville, NH (03450)	908
Hebron, NH (03241)	721
Henniker, NH (03242)	3693
Hill, NH (03243)	938
Hillsborough, NH (03244)	6896
Hinsdale, NH (03451)	3489
Holderness, NH (03245)	1676
Hollis, NH (03049)	7556
Hudson, NH (03051)	22261
Litchfield, NH (03052)	7558
Intervale, NH (03845)	1226
Jackson, NH (03846)	867
Jaffrey, NH (03452)	4742
Jefferson, NH (03583)	969
Keene, NH (03431)	18682
Kingston, NH (03848)	5457
Laconia, NH (03246)	12852
Gilford, NH (03249)	6003
Lancaster, NH (03584)	3051
Lebanon, NH (03766)	7995
West Lebanon, NH (03784)	3344
Lincoln, NH (03251)	1455
Lisbon, NH (03585)	2280
Littleton, NH (03561)	5340
Londonderry, NH (03053)	22127
Lyme, NH (03768)	1480
Madison, NH (03849)	1144
Manchester, NH (03101)	2104
Manchester, NH (03102)	23532
Manchester, NH (03103)	28024
Manchester, NH (03104)	26506
Hooksett, NH (03106)	11789
Manchester, NH (03109)	9076
Bedford, NH (03110)	19184
Marlborough, NH (03455)	1895
Marlow, NH (03456)	711
Stoddard, NH (03464)	877
Meredith, NH (03253)	5790
Meriden, NH (03770)	662
Merrimack, NH (03054)	24084
Milan, NH (03588)	1560
Milford, NH (03055)	13156
Milton, NH (03851)	3495
Milton Mills, NH (03852)	526
Mirror Lake, NH (03853)	514
Monroe, NH (03771)	734
Mont Vernon, NH (03057)	2220
Moultonborough, NH (03254)	3190
Nashua, NH (03060)	22531
Nashua, NH (03062)	24132
Nashua, NH (03063)	14547
Nashua, NH (03064)	11911
New Boston, NH (03070)	4693
Newbury, NH (03255)	1702
New Durham, NH (03855)	2431
Newfields, NH (03856)	1636
New Hampton, NH (03256)	1819
New Ipswich, NH (03071)	4132
New London, NH (03257)	3804
Newmarket, NH (03857)	7523
Newport, NH (03773)	6469
Newton, NH (03858)	4002
North Conway, NH (03860)	3702
North Hampton, NH (03862)	4254
North Haverhill, NH (03774)	1497
North Stratford, NH (03590)	817
Northwood, NH (03261)	3887
North Woodstock, NH (03262)	1012
Nottingham, NH (03290)	4061
Orford, NH (03777)	1064
Ossipee, NH (03864)	1353
Pelham, NH (03076)	11839
Peterborough, NH (03458)	5705
Piermont, NH (03779)	675
Pittsburg, NH (03592)	1003
Pittsfield, NH (03263)	3366
Plainfield, NH (03781)	1532
Plaistow, NH (03865)	7051
Plymouth, NH (03264)	3990
Portsmouth, NH (03801)	18209
Raymond, NH (03077)	9270
Rindge, NH (03461)	4443
Rochester, NH (03839)	3330
Rochester, NH (03867)	16679
Rochester, NH (03868)	4918
Rollinsford, NH (03869)	2161
Rumney, NH (03266)	1886
Rye, NH (03870)	4505
Salem, NH (03079)	26049
Salisbury, NH (03268)	1116
Sanbornton, NH (03269)	2620
Sanbornville, NH (03872)	3405
Sandown, NH (03873)	5363
Seabrook, NH (03874)	7725
Silver Lake, NH (03875)	706
Somersworth, NH (03878)	10059
Effingham, NH (03882)	998
Lyndeborough, NH (03082)	1394
Spofford, NH (03462)	1539
Strafford, NH (03884)	3653
Stratham, NH (03885)	6872
Sunapee, NH (03782)	2498
Suncook, NH (03275)	10177
Tamworth, NH (03886)	1273
Temple, NH (03084)	1219
Tilton, NH (03276)	6892
Troy, NH (03465)	1881
Union, NH (03887)	1818
Walpole, NH (03608)	2572
North Walpole, NH (03609)	638
Warner, NH (03278)	2640
Warren, NH (03279)	652
Washington, NH (03280)	902
Weare, NH (03281)	7854
Wentworth, NH (03282)	806
West Chesterfield, NH (03466)	1208
Westmoreland, NH (03467)	1539
West Ossipee, NH (03890)	857
Springfield, NH (03284)	676
Whitefield, NH (03598)	2810
Wilmot, NH (03287)	1056
Wilton, NH (03086)	3655
Winchester, NH (03470)	4090
Windham, NH (03087)	12419
Center Tuftonboro, NH (03816)	911
Wolfeboro, NH (03894)	5312
Woodsville, NH (03785)	1755
Alburgh, VT (05440)	1781
Arlington, VT (05250)	2911
Bakersfield, VT (05441)	602
Barnet, VT (05821)	1004
Barre, VT (05641)	13551
Barton, VT (05822)	1747
Glover, VT (05839)	613
Bellows Falls, VT (05101)	3543
Bennington, VT (05201)	12180
Bethel, VT (05032)	2051
Bomoseen, VT (05732)	1003
Bondville, VT (05340)	720
Bradford, VT (05033)	2569
Brandon, VT (05733)	4770
Brattleboro, VT (05301)	12127
Bridgewater Corners, VT (05035)	527
Bridport, VT (05734)	1087
Bristol, VT (05443)	5546
Brookfield, VT (05036)	802
Brownsville, VT (05037)	717
Burlington, VT (05401)	16845
South Burlington, VT (05403)	15655
Winooski, VT (05404)	5309
Burlington, VT (05408)	8454
Cabot, VT (05647)	853
Calais, VT (05648)	451
Cambridge, VT (05444)	1600
Canaan, VT (05903)	738
Castleton, VT (05735)	2370
Cavendish, VT (05142)	601
Charlotte, VT (05445)	3516
Chelsea, VT (05038)	1172
Chester, VT (05143)	4032
Chittenden, VT (05737)	665
Colchester, VT (05446)	13766
Concord, VT (05824)	938
Corinth, VT (05039)	718
Craftsbury, VT (05826)	628
Cuttingsville, VT (05738)	1058
Danby, VT (05739)	1194
Danville, VT (05828)	1672
Derby, VT (05829)	2224
Derby Line, VT (05830)	1332
Dorset, VT (05251)	1236
East Barre, VT (05649)	959
East Burke, VT (05832)	814
East Calais, VT (05650)	906
East Corinth, VT (05040)	506
East Dorset, VT (05253)	559
East Fairfield, VT (05448)	962
East Hardwick, VT (05836)	880
East Montpelier, VT (05651)	1465
East Ryegate, VT (05042)	510
East Thetford, VT (05043)	769
Eden, VT (05652)	651
Enosburg Falls, VT (05450)	4192
Essex Junction, VT (05452)	17705
Fairfax, VT (05454)	4130
Fairfield, VT (05455)	1037
Fair Haven, VT (05743)	3514
Fairlee, VT (05045)	1270
Ferrisburgh, VT (05456)	1108
Florence, VT (05744)	507
Franklin, VT (05457)	1336
Grafton, VT (05146)	516
Grand Isle, VT (05458)	1905
Graniteville, VT (05654)	1050
Greensboro Bend, VT (05842)	498
Groton, VT (05046)	1054
Guildhall, VT (05905)	584
Hardwick, VT (05843)	2254
Hartland, VT (05048)	2161
Highgate Center, VT (05459)	1704
Hinesburg, VT (05461)	4309
Huntington, VT (05462)	1733
Hyde Park, VT (05655)	2465
Irasburg, VT (05845)	1030
Island Pond, VT (05846)	1053
Isle La Motte, VT (05463)	452
Jacksonville, VT (05342)	572
Jamaica, VT (05343)	697
Jeffersonville, VT (05464)	2441
Jericho, VT (05465)	5143
Johnson, VT (05656)	2331
Killington, VT (05751)	1157
Londonderry, VT (05148)	1210
Lowell, VT (05847)	636
Ludlow, VT (05149)	2103
Lunenburg, VT (05906)	1005
Lyndon Center, VT (05850)	575
Lyndonville, VT (05851)	4536
Manchester Center, VT (05255)	3743
Marshfield, VT (05658)	1228
Middlebury, VT (05753)	6966
Middletown Springs, VT (05757)	782
Milton, VT (05468)	11914
Montgomery Center, VT (05471)	653
Montpelier, VT (05602)	10117
Moretown, VT (05660)	1642
Morgan, VT (05853)	453
Morrisville, VT (05661)	5006
Mount Holly, VT (05758)	646
Newbury, VT (05051)	828
Newfane, VT (05345)	1416
New Haven, VT (05472)	1669
Newport, VT (05855)	5570
Newport Center, VT (05857)	1218
North Bennington, VT (05257)	2155
North Clarendon, VT (05759)	1856
North Ferrisburgh, VT (05473)	1242
Northfield, VT (05663)	3880
North Hero, VT (05474)	757
North Springfield, VT (05150)	925
North Troy, VT (05859)	1422
Norwich, VT (05055)	3317
Orleans, VT (05860)	2073
Orwell, VT (05760)	1038
Pawlet, VT (05761)	932
Perkinsville, VT (05151)	1126
Pittsfield, VT (05762)	432
Pittsford, VT (05763)	2481
Plainfield, VT (05667)	1957
Poultney, VT (05764)	2481
Pownal, VT (05261)	2087
Proctor, VT (05765)	1566
Proctorsville, VT (05153)	670
Putney, VT (05346)	4067
Randolph, VT (05060)	3991
Randolph Center, VT (05061)	1100
Reading, VT (05062)	623
Readsboro, VT (05350)	636
Stamford, VT (05352)	757
Richford, VT (05476)	2173
Richmond, VT (05477)	4027
Rochester, VT (05767)	1033
Roxbury, VT (05669)	462
Rutland, VT (05701)	16970
Saint Albans, VT (05478)	12191
Saint Johnsbury, VT (05819)	6872
Salisbury, VT (05769)	951
Saxtons River, VT (05154)	849
Shaftsbury, VT (05262)	2236
Sharon, VT (05065)	1078
Sheffield, VT (05866)	573
Shelburne, VT (05482)	6810
Sheldon, VT (05483)	1194
Shoreham, VT (05770)	1014
South Hero, VT (05486)	1619
South Londonderry, VT (05155)	860
South Royalton, VT (05068)	2458
South Ryegate, VT (05069)	581
South Strafford, VT (05070)	495
Springfield, VT (05156)	7482
Starksboro, VT (05487)	1323
Stowe, VT (05672)	4344
Swanton, VT (05488)	6347
Thetford Center, VT (05075)	1118
Townshend, VT (05353)	857
West Townshend, VT (05359)	447
Westfield, VT (05874)	464
Tunbridge, VT (05077)	914
Underhill, VT (05489)	2816
Vergennes, VT (05491)	5045
Vernon, VT (05354)	1940
Vershire, VT (05079)	538
Waitsfield, VT (05673)	2719
Wallingford, VT (05773)	1949
Warren, VT (05674)	1263
Washington, VT (05675)	817
Waterbury, VT (05676)	4322
Waterbury Center, VT (05677)	1994
Waterville, VT (05492)	688
Wells, VT (05774)	1047
Wells River, VT (05081)	747
Sutton, VT (05867)	547
West Burke, VT (05871)	1264
West Charleston, VT (05872)	583
West Danville, VT (05873)	636
West Dover, VT (05356)	1043
Westford, VT (05494)	1555
Westminster, VT (05158)	965
Weston, VT (05161)	552
West Pawlet, VT (05775)	488
Center Rutland, VT (05736)	536
West Rutland, VT (05777)	3132
West Topsham, VT (05086)	664
White River Junction, VT (05001)	6028
Whiting, VT (05778)	667
Whitingham, VT (05361)	601
Williamstown, VT (05679)	2786
Williston, VT (05495)	9087
Wilmington, VT (05363)	1949
Windsor, VT (05089)	3525
Wolcott, VT (05680)	1662
Woodstock, VT (05091)	3089
Worcester, VT (05682)	1110
Amston, CT (06231)	3495
Andover, CT (06232)	2914
Ansonia, CT (06401)	15455
Ashford, CT (06278)	3875
Avon, CT (06001)	16788
Baltic, CT (06330)	2420
Bantam, CT (06750)	1166
Beacon Falls, CT (06403)	5256
Bethel, CT (06801)	16312
Bethlehem, CT (06751)	3217
Bloomfield, CT (06002)	18034
Branford, CT (06405)	24804
Bridgeport, CT (06604)	17228
Bridgeport, CT (06605)	15128
Bridgeport, CT (06606)	34905
Bridgeport, CT (06607)	5251
Bridgeport, CT (06608)	8867
Bridgeport, CT (06610)	16983
Trumbull, CT (06611)	31966
Easton, CT (06612)	6798
Stratford, CT (06614)	28948
Stratford, CT (06615)	15405
Bridgewater, CT (06752)	1631
Bristol, CT (06010)	50388
Broad Brook, CT (06016)	5434
Brookfield, CT (06804)	14886
Brooklyn, CT (06234)	6516
Canaan, CT (06018)	2308
Canterbury, CT (06331)	4503
Canton, CT (06019)	8702
Centerbrook, CT (06409)	559
Chaplin, CT (06235)	1952
Cheshire, CT (06410)	24428
Chester, CT (06412)	3382
Clinton, CT (06413)	11725
Colchester, CT (06415)	14589
Salem, CT (06420)	3806
Colebrook, CT (06021)	588
Columbia, CT (06237)	4991
Cornwall Bridge, CT (06754)	1348
Cos Cob, CT (06807)	6107
Coventry, CT (06238)	10876
Cromwell, CT (06416)	12477
Danbury, CT (06810)	35694
Danbury, CT (06811)	24956
New Fairfield, CT (06812)	12686
Danielson, CT (06239)	8642
Darien, CT (06820)	18239
Dayville, CT (06241)	5026
Deep River, CT (06417)	4028
Killingworth, CT (06419)	5878
Derby, CT (06418)	10248
Durham, CT (06422)	6778
East Berlin, CT (06023)	1204
East Canaan, CT (06024)	491
Eastford, CT (06242)	1360
East Granby, CT (06026)	4698
East Haddam, CT (06423)	4462
East Hampton, CT (06424)	11243
Marlborough, CT (06447)	5825
East Hartland, CT (06027)	1332
East Lyme, CT (06333)	6255
East Windsor, CT (06088)	4088
Ellington, CT (06029)	13436
Enfield, CT (06082)	35610
Essex, CT (06426)	3055
Fairfield, CT (06824)	26855
Fairfield, CT (06825)	16768
Falls Village, CT (06031)	1062
Farmington, CT (06032)	16183
Gales Ferry, CT (06335)	6197
Ledyard, CT (06339)	7346
Gaylordsville, CT (06755)	1053
Glastonbury, CT (06033)	25927
Goshen, CT (06756)	2576
Granby, CT (06035)	6864
Greenwich, CT (06830)	19812
Greenwich, CT (06831)	12950
Groton, CT (06340)	22778
Guilford, CT (06437)	19859
Haddam, CT (06438)	2338
Hampton, CT (06247)	2112
Hartford, CT (06103)	1087
Hartford, CT (06105)	12164
Hartford, CT (06106)	24425
West Hartford, CT (06107)	17031
East Hartford, CT (06108)	18429
Wethersfield, CT (06109)	23881
West Hartford, CT (06110)	10680
Newington, CT (06111)	27167
Hartford, CT (06112)	14548
Hartford, CT (06114)	18603
West Hartford, CT (06117)	13211
East Hartford, CT (06118)	22839
West Hartford, CT (06119)	12133
Hartford, CT (06120)	6580
Hebron, CT (06248)	5191
Higganum, CT (06441)	4936
Ivoryton, CT (06442)	2513
Jewett City, CT (06351)	13771
Berlin, CT (06037)	17190
Kent, CT (06757)	1917
Lakeville, CT (06039)	1893
Lebanon, CT (06249)	6338
Litchfield, CT (06759)	5166
Madison, CT (06443)	16636
Manchester, CT (06040)	29298
Manchester, CT (06042)	18594
Bolton, CT (06043)	4713
Mansfield Center, CT (06250)	4307
Meriden, CT (06450)	29435
Meriden, CT (06451)	19143
Middlebury, CT (06762)	6856
Middlefield, CT (06455)	3042
Middletown, CT (06457)	36168
Milford, CT (06460)	34070
Milford, CT (06461)	12602
Monroe, CT (06468)	17424
Montville, CT (06353)	407
Moodus, CT (06469)	2768
Moosup, CT (06354)	4561
Morris, CT (06763)	1862
Mystic, CT (06355)	11444
Naugatuck, CT (06770)	26868
New Britain, CT (06051)	20529
New Britain, CT (06052)	6445
New Britain, CT (06053)	24752
New Canaan, CT (06840)	17448
New Hartford, CT (06057)	6239
New Haven, CT (06510)	1404
New Haven, CT (06511)	31415
East Haven, CT (06512)	24262
New Haven, CT (06513)	25270
Hamden, CT (06514)	20719
New Haven, CT (06515)	10815
West Haven, CT (06516)	42606
Hamden, CT (06517)	12658
Hamden, CT (06518)	13044
New Haven, CT (06519)	9594
Bethany, CT (06524)	5070
Woodbridge, CT (06525)	8587
New London, CT (06320)	19438
New Milford, CT (06776)	22771
Newtown, CT (06470)	14030
Sandy Hook, CT (06482)	9509
Niantic, CT (06357)	9545
Norfolk, CT (06058)	1485
North Branford, CT (06471)	6874
Northford, CT (06472)	6231
North Franklin, CT (06254)	1711
North Granby, CT (06060)	2317
North Grosvenordale, CT (06255)	3685
North Haven, CT (06473)	21685
North Stonington, CT (06359)	4802
North Windham, CT (06256)	1930
Norwalk, CT (06850)	15241
Norwalk, CT (06851)	22550
Norwalk, CT (06853)	3224
Norwalk, CT (06854)	21479
Norwalk, CT (06855)	6256
Norwich, CT (06360)	29516
Preston, CT (06365)	4233
Oakdale, CT (06370)	6678
Old Greenwich, CT (06870)	6308
Old Lyme, CT (06371)	8646
Old Saybrook, CT (06475)	9324
Orange, CT (06477)	13053
Plainfield, CT (06374)	6454
Plainville, CT (06062)	15474
Plantsville, CT (06479)	8677
Barkhamsted, CT (06063)	2978
Plymouth, CT (06782)	2160
Pomfret Center, CT (06259)	3170
Portland, CT (06480)	8392
Putnam, CT (06260)	7299
Quaker Hill, CT (06375)	3297
Quinebaug, CT (06262)	595
Ridgefield, CT (06877)	21748
Riverside, CT (06878)	7019
Riverton, CT (06065)	746
Rockfall, CT (06481)	909
Rocky Hill, CT (06067)	17166
Roxbury, CT (06783)	2017
Salisbury, CT (06068)	1191
Scotland, CT (06264)	627
Oxford, CT (06478)	11216
Seymour, CT (06483)	14118
Sharon, CT (06069)	2013
Shelton, CT (06484)	35618
Sherman, CT (06784)	3283
Simsbury, CT (06070)	13868
Somers, CT (06071)	8215
Southbury, CT (06488)	17282
South Glastonbury, CT (06073)	5078
Southington, CT (06489)	28496
South Kent, CT (06785)	585
Southport, CT (06890)	3874
South Windham, CT (06266)	511
South Windsor, CT (06074)	23622
Stafford Springs, CT (06076)	10627
Stamford, CT (06901)	5368
Stamford, CT (06902)	47130
Stamford, CT (06903)	13113
Stamford, CT (06905)	17913
Stamford, CT (06906)	7923
Stamford, CT (06907)	8014
Sterling, CT (06377)	2279
Stonington, CT (06378)	4885
Pawcatuck, CT (06379)	7620
Storrs Mansfield, CT (06268)	5888
Suffield, CT (06078)	8852
Taftville, CT (06380)	2072
Tariffville, CT (06081)	1163
Terryville, CT (06786)	8443
Northfield, CT (06778)	1164
Thomaston, CT (06787)	6903
Thompson, CT (06277)	3680
Tolland, CT (06084)	13549
Torrington, CT (06790)	30090
Harwinton, CT (06791)	5110
Uncasville, CT (06382)	8952
Burlington, CT (06013)	8379
Unionville, CT (06085)	6187
Vernon Rockville, CT (06066)	24424
Voluntown, CT (06384)	2429
Wallingford, CT (06492)	39797
New Preston Marble Dale, CT (06777)	1494
Washington, CT (06793)	998
Washington Depot, CT (06794)	1102
Waterbury, CT (06702)	1545
Waterbury, CT (06704)	17963
Waterbury, CT (06705)	20413
Waterbury, CT (06706)	10326
Waterbury, CT (06708)	22350
Waterbury, CT (06710)	6891
Prospect, CT (06712)	8427
Wolcott, CT (06716)	14506
Waterford, CT (06385)	14516
Oakville, CT (06779)	6985
Watertown, CT (06795)	12552
Weatogue, CT (06089)	2654
Westbrook, CT (06498)	5947
West Cornwall, CT (06796)	779
West Granby, CT (06090)	1117
Westport, CT (06880)	23735
Weston, CT (06883)	9143
Redding, CT (06896)	7867
West Simsbury, CT (06092)	4014
West Suffield, CT (06093)	3130
Willington, CT (06279)	4823
Willimantic, CT (06226)	11822
Wilton, CT (06897)	16501
Windham, CT (06280)	2640
Windsor, CT (06095)	26020
Windsor Locks, CT (06096)	11081
Winsted, CT (06098)	9551
Woodbury, CT (06798)	8844
Woodstock, CT (06281)	5695
Woodstock Valley, CT (06282)	1018
Adams, MA (01220)	6993
Savoy, MA (01256)	574
Agawam, MA (01001)	14021
Amherst, MA (01002)	16532
Ashfield, MA (01330)	1345
Ashley Falls, MA (01222)	681
Assonet, MA (02702)	3833
Athol, MA (01331)	10562
Royalston, MA (01368)	1081
Attleboro, MA (02703)	36164
Barre, MA (01005)	3935
Becket, MA (01223)	1964
Belchertown, MA (01007)	12895
Bernardston, MA (01337)	2438
Blandford, MA (01008)	1153
Brimfield, MA (01010)	3312
Charlemont, MA (01339)	1250
Cheshire, MA (01225)	2990
Chester, MA (01011)	1012
Chesterfield, MA (01012)	639
Chicopee, MA (01013)	16669
Chicopee, MA (01020)	24570
Chicopee, MA (01022)	1713
Colrain, MA (01340)	1581
Conway, MA (01341)	1541
Cummington, MA (01026)	865
Dalton, MA (01226)	5793
Deerfield, MA (01342)	1238
Dighton, MA (02715)	2622
East Freetown, MA (02717)	4357
Easthampton, MA (01027)	15525
Florence, MA (01062)	9483
East Longmeadow, MA (01028)	14024
Longmeadow, MA (01106)	14332
Erving, MA (01344)	1247
Fairhaven, MA (02719)	13392
Fall River, MA (02720)	22304
Fall River, MA (02721)	18264
Fall River, MA (02723)	10441
Fall River, MA (02724)	11903
Somerset, MA (02725)	2190
Somerset, MA (02726)	13724
Feeding Hills, MA (01030)	10449
Gilbertville, MA (01031)	932
Goshen, MA (01032)	489
Granby, MA (01033)	5647
Granville, MA (01034)	1787
Great Barrington, MA (01230)	5873
Greenfield, MA (01301)	13381
Hadley, MA (01035)	4327
Hampden, MA (01036)	4700
Hatfield, MA (01038)	2161
West Hatfield, MA (01088)	458
Haydenville, MA (01039)	1228
Hinsdale, MA (01235)	2476
Holyoke, MA (01040)	26316
Housatonic, MA (01236)	1486
Huntington, MA (01050)	2282
Lanesboro, MA (01237)	2606
Lee, MA (01238)	5056
Leeds, MA (01053)	1407
Lenox, MA (01240)	4020
Leverett, MA (01054)	1620
Ludlow, MA (01056)	17529
Marion, MA (02738)	4357
Mattapoisett, MA (02739)	5697
Monson, MA (01057)	7429
Montague, MA (01351)	2016
Monterey, MA (01245)	682
New Bedford, MA (02740)	28944
Acushnet, MA (02743)	9079
New Bedford, MA (02744)	8050
New Bedford, MA (02745)	19536
New Bedford, MA (02746)	8919
North Dartmouth, MA (02747)	15533
South Dartmouth, MA (02748)	10032
North Adams, MA (01247)	11730
Northampton, MA (01060)	10304
North Attleboro, MA (02760)	22964
Plainville, MA (02762)	7456
Attleboro Falls, MA (02763)	1856
North Dighton, MA (02764)	3638
Northfield, MA (01360)	2627
Norton, MA (02766)	15129
Oakham, MA (01068)	1807
New Salem, MA (01355)	803
Orange, MA (01364)	6044
Warwick, MA (01378)	611
Otis, MA (01253)	778
Palmer, MA (01069)	6950
Petersham, MA (01366)	1104
Pittsfield, MA (01201)	36002
Plainfield, MA (01070)	467
Raynham, MA (02767)	11607
Rehoboth, MA (02769)	10452
Richmond, MA (01254)	1068
Rochester, MA (02770)	4715
Rowe, MA (01367)	444
Russell, MA (01071)	1376
Sandisfield, MA (01255)	572
Seekonk, MA (02771)	12579
Sheffield, MA (01257)	2018
Shelburne Falls, MA (01370)	3439
Shutesbury, MA (01072)	1269
Southampton, MA (01073)	5385
South Deerfield, MA (01373)	4019
South Egremont, MA (01258)	591
Southfield, MA (01259)	438
South Hadley, MA (01075)	14184
Southwick, MA (01077)	8567
Springfield, MA (01103)	1533
Springfield, MA (01104)	15795
Springfield, MA (01105)	6054
Springfield, MA (01107)	6360
Springfield, MA (01108)	17151
Springfield, MA (01109)	17988
Springfield, MA (01118)	11858
Springfield, MA (01119)	9915
Springfield, MA (01128)	2510
Springfield, MA (01129)	5884
Indian Orchard, MA (01151)	6080
Sunderland, MA (01375)	2777
Swansea, MA (02777)	14102
East Taunton, MA (02718)	5968
Berkley, MA (02779)	5580
Taunton, MA (02780)	39589
Three Rivers, MA (01080)	1888
Millers Falls, MA (01349)	697
Gill, MA (01354)	1338
Turners Falls, MA (01376)	3968
Wales, MA (01081)	1491
Ware, MA (01082)	8509
Wendell, MA (01379)	625
Westfield, MA (01085)	32344
Westport, MA (02790)	13765
West Springfield, MA (01089)	23043
West Stockbridge, MA (01266)	1182
Wilbraham, MA (01095)	13107
Williamsburg, MA (01096)	2266
Williamstown, MA (01267)	5277
Windsor, MA (01270)	694
Worthington, MA (01098)	1076
Ashaway, RI (02804)	2518
Barrington, RI (02806)	15163
Bradford, RI (02808)	2043
Bristol, RI (02809)	16829
Carolina, RI (02812)	1368
Charlestown, RI (02813)	6822
Chepachet, RI (02814)	6606
Coventry, RI (02816)	27787
West Greenwich, RI (02817)	5436
Greene, RI (02827)	2027
East Greenwich, RI (02818)	16723
Exeter, RI (02822)	5183
Foster, RI (02825)	4719
Greenville, RI (02828)	6569
Harrisville, RI (02830)	5420
Hope, RI (02831)	3532
Hope Valley, RI (02832)	4094
Hopkinton, RI (02833)	559
Jamestown, RI (02835)	5079
Little Compton, RI (02837)	3047
Manville, RI (02838)	2736
Mapleville, RI (02839)	1601
Newport, RI (02840)	17022
Middletown, RI (02842)	13797
North Kingstown, RI (02852)	20118
North Scituate, RI (02857)	7729
Pascoag, RI (02859)	5307
Pawtucket, RI (02860)	32700
Pawtucket, RI (02861)	22037
Central Falls, RI (02863)	12807
Cumberland, RI (02864)	29895
Lincoln, RI (02865)	15355
Portsmouth, RI (02871)	15498
Providence, RI (02903)	5160
Providence, RI (02904)	22164
Providence, RI (02905)	19006
Providence, RI (02906)	17860
Providence, RI (02907)	20468
Providence, RI (02908)	24468
Providence, RI (02909)	27797
Cranston, RI (02910)	18350
North Providence, RI (02911)	12324
Smithfield, RI (02917)	10133
Cranston, RI (02920)	28279
Cranston, RI (02921)	10886
Saunderstown, RI (02874)	5257
Slatersville, RI (02876)	1211
Tiverton, RI (02878)	13961
Wakefield, RI (02879)	17248
Kingston, RI (02881)	2040
Narragansett, RI (02882)	10236
Warren, RI (02885)	8830
Warwick, RI (02886)	25122
Warwick, RI (02888)	17491
Warwick, RI (02889)	24614
Westerly, RI (02891)	18883
West Kingston, RI (02892)	4536
West Warwick, RI (02893)	24077
Wood River Junction, RI (02894)	706
Woonsocket, RI (02895)	30278
North Smithfield, RI (02896)	8477
Wyoming, RI (02898)	1900
Johnston, RI (02919)	23966
East Providence, RI (02914)	17218
Riverside, RI (02915)	14348
Rumford, RI (02916)	7268
Allendale, NJ (07401)	5823
Andover, NJ (07821)	8046
Annandale, NJ (08801)	7033
Asbury, NJ (08802)	3833
Augusta, NJ (07822)	1034
Avenel, NJ (07001)	11573
Basking Ridge, NJ (07920)	24379
Bayonne, NJ (07002)	49850
Bedminster, NJ (07921)	6958
Belvidere, NJ (07823)	6372
Bergenfield, NJ (07621)	22950
Berkeley Heights, NJ (07922)	11230
Bernardsville, NJ (07924)	6545
Blairstown, NJ (07825)	8003
Bloomfield, NJ (07003)	40014
Bloomingdale, NJ (07403)	6373
Bloomsbury, NJ (08804)	2745
Boonton, NJ (07005)	13492
Bound Brook, NJ (08805)	10018
Branchville, NJ (07826)	5528
Montague, NJ (07827)	3383
Bridgewater, NJ (08807)	33977
Budd Lake, NJ (07828)	11080
Butler, NJ (07405)	16050
Fairfield, NJ (07004)	7094
Caldwell, NJ (07006)	22600
Califon, NJ (07830)	5979
Carteret, NJ (07008)	18300
Cedar Grove, NJ (07009)	10730
Cedar Knolls, NJ (07927)	3204
Chatham, NJ (07928)	16921
Chester, NJ (07930)	7622
Cliffside Park, NJ (07010)	18008
Clifton, NJ (07011)	32734
Clifton, NJ (07012)	10729
Clifton, NJ (07013)	23975
Clifton, NJ (07014)	4646
Clinton, NJ (08809)	4772
Closter, NJ (07624)	7464
Columbia, NJ (07832)	3322
Cranford, NJ (07016)	20361
Cresskill, NJ (07626)	7423
Dayton, NJ (08810)	7524
Demarest, NJ (07627)	4545
Denville, NJ (07834)	16065
Dover, NJ (07801)	20418
Mine Hill, NJ (07803)	3197
Randolph, NJ (07869)	23006
Dumont, NJ (07628)	15212
Dunellen, NJ (08812)	12136
East Brunswick, NJ (08816)	42868
East Hanover, NJ (07936)	10659
East Orange, NJ (07017)	25182
East Orange, NJ (07018)	19385
Edgewater, NJ (07020)	8894
Edison, NJ (08817)	39684
Edison, NJ (08820)	35691
Edison, NJ (08837)	13761
Elizabeth, NJ (07201)	19403
Elizabeth, NJ (07202)	29174
Roselle, NJ (07203)	17452
Roselle Park, NJ (07204)	11435
Hillside, NJ (07205)	18782
Elizabethport, NJ (07206)	18980
Elizabeth, NJ (07208)	24374
Elmwood Park, NJ (07407)	17030
Emerson, NJ (07630)	6374
Englewood, NJ (07631)	21826
Englewood Cliffs, NJ (07632)	5088
Essex Fells, NJ (07021)	2007
Fair Lawn, NJ (07410)	29095
Fairview, NJ (07022)	9349
Fanwood, NJ (07023)	6663
Far Hills, NJ (07931)	3060
Flanders, NJ (07836)	10541
Flemington, NJ (08822)	27375
Florham Park, NJ (07932)	9267
Fort Lee, NJ (07024)	29968
Franklin, NJ (07416)	4804
Franklin Lakes, NJ (07417)	9986
Franklin Park, NJ (08823)	8014
Frenchtown, NJ (08825)	3829
Garfield, NJ (07026)	25066
Garwood, NJ (07027)	3694
Gillette, NJ (07933)	2952
Gladstone, NJ (07934)	1371
Glen Gardner, NJ (08826)	4916
Glen Ridge, NJ (07028)	6868
Glenwood, NJ (07418)	2288
Great Meadows, NJ (07838)	3106
Green Village, NJ (07935)	529
Hackensack, NJ (07601)	34232
Bogota, NJ (07603)	6889
Hasbrouck Heights, NJ (07604)	10360
Leonia, NJ (07605)	7589
South Hackensack, NJ (07606)	2270
Maywood, NJ (07607)	8372
Hackettstown, NJ (07840)	24882
Hamburg, NJ (07419)	7852
Hampton, NJ (08827)	4096
Harrington Park, NJ (07640)	4361
Harrison, NJ (07029)	13420
Haskell, NJ (07420)	4023
Haworth, NJ (07641)	3115
Helmetta, NJ (08828)	1927
Hewitt, NJ (07421)	6615
High Bridge, NJ (08829)	3328
Highland Lakes, NJ (07422)	6178
Hillsborough, NJ (08844)	34693
Hillsdale, NJ (07642)	9206
Township Of Washington, NJ (07676)	8290
Hoboken, NJ (07030)	37267
Ho Ho Kus, NJ (07423)	3722
Hopatcong, NJ (07843)	10538
Iselin, NJ (08830)	17210
Monroe Township, NJ (08831)	41128
Jersey City, NJ (07302)	28393
Jersey City, NJ (07304)	31180
Jersey City, NJ (07305)	46569
Jersey City, NJ (07306)	39173
Jersey City, NJ (07307)	34041
Jersey City, NJ (07310)	9640
Jersey City, NJ (07311)	430
North Arlington, NJ (07031)	13771
Kearny, NJ (07032)	31241
Keasbey, NJ (08832)	2437
Kendall Park, NJ (08824)	11637
Kenilworth, NJ (07033)	7022
Kenvil, NJ (07847)	1520
Lafayette, NJ (07848)	3917
Lake Hiawatha, NJ (07034)	8365
Lake Hopatcong, NJ (07849)	7845
Landing, NJ (07850)	5877
Lebanon, NJ (08833)	8101
Ledgewood, NJ (07852)	3257
Lincoln Park, NJ (07035)	9191
Linden, NJ (07036)	35142
Little Falls, NJ (07424)	20128
Little Ferry, NJ (07643)	8899
Livingston, NJ (07039)	27160
Lodi, NJ (07644)	19903
Long Valley, NJ (07853)	11904
Madison, NJ (07940)	12693
Mahwah, NJ (07430)	21442
Manville, NJ (08835)	8927
Maplewood, NJ (07040)	20973
Martinsville, NJ (08836)	3670
Mendham, NJ (07945)	9193
Metuchen, NJ (08840)	15163
Middlesex, NJ (08846)	12094
Midland Park, NJ (07432)	6264
Milford, NJ (08848)	7470
Millburn, NJ (07041)	6225
Millington, NJ (07946)	2970
Milltown, NJ (08850)	7643
Monmouth Junction, NJ (08852)	14675
Montclair, NJ (07042)	21177
Montclair, NJ (07043)	10966
Verona, NJ (07044)	11979
Montvale, NJ (07645)	7226
Montville, NJ (07045)	9442
Morris Plains, NJ (07950)	17593
Morristown, NJ (07960)	33647
Mountain Lakes, NJ (07046)	3888
Mount Arlington, NJ (07856)	3426
Neshanic Station, NJ (08853)	4879
Netcong, NJ (07857)	2788
Newark, NJ (07102)	5503
Newark, NJ (07103)	20135
Newark, NJ (07104)	35277
Newark, NJ (07105)	29429
Newark, NJ (07106)	22439
Newark, NJ (07107)	25902
Newark, NJ (07108)	15957
Belleville, NJ (07109)	30299
Nutley, NJ (07110)	25001
Irvington, NJ (07111)	41875
Newark, NJ (07112)	19082
Newark, NJ (07114)	6170
New Brunswick, NJ (08901)	28187
North Brunswick, NJ (08902)	34952
Highland Park, NJ (08904)	11275
Newfoundland, NJ (07435)	2314
New Milford, NJ (07646)	14165
New Providence, NJ (07974)	10648
Newton, NJ (07860)	21086
New Vernon, NJ (07976)	1310
North Bergen, NJ (07047)	45454
Northvale, NJ (07647)	4171
Norwood, NJ (07648)	5033
Oakland, NJ (07436)	11508
Oak Ridge, NJ (07438)	10328
Ogdensburg, NJ (07439)	2250
Old Bridge, NJ (08857)	34538
Oradell, NJ (07649)	7355
Orange, NJ (07050)	22984
West Orange, NJ (07052)	39097
Oxford, NJ (07863)	3674
Palisades Park, NJ (07650)	13274
Paramus, NJ (07652)	22875
Park Ridge, NJ (07656)	7922
Parlin, NJ (08859)	20576
Parsippany, NJ (07054)	26016
Passaic, NJ (07055)	51244
Wallington, NJ (07057)	9893
Paterson, NJ (07501)	22824
Paterson, NJ (07502)	12805
Paterson, NJ (07503)	14649
Paterson, NJ (07504)	10707
Paterson, NJ (07505)	1388
Hawthorne, NJ (07506)	16150
Haledon, NJ (07508)	19084
Totowa, NJ (07512)	9063
Paterson, NJ (07513)	9915
Paterson, NJ (07514)	14312
Paterson, NJ (07522)	15644
Paterson, NJ (07524)	9948
Pequannock, NJ (07440)	4127
Perth Amboy, NJ (08861)	41825
Fords, NJ (08863)	11015
Phillipsburg, NJ (08865)	24138
Pine Brook, NJ (07058)	5037
Piscataway, NJ (08854)	43472
Pittstown, NJ (08867)	4651
Warren, NJ (07059)	14590
Plainfield, NJ (07060)	32363
Plainfield, NJ (07062)	10678
Plainfield, NJ (07063)	10226
Watchung, NJ (07069)	5361
Pompton Lakes, NJ (07442)	9786
Pompton Plains, NJ (07444)	10193
Port Murray, NJ (07865)	2430
Port Reading, NJ (07064)	3342
Rahway, NJ (07065)	22711
Clark, NJ (07066)	13402
Colonia, NJ (07067)	16467
Ramsey, NJ (07446)	13317
Raritan, NJ (08869)	5803
Ridgefield, NJ (07657)	9186
Ridgefield Park, NJ (07660)	10825
Ridgewood, NJ (07450)	21805
Glen Rock, NJ (07452)	10630
Ringwood, NJ (07456)	11161
Riverdale, NJ (07457)	3259
River Edge, NJ (07661)	10002
Rochelle Park, NJ (07662)	5133
Saddle Brook, NJ (07663)	12144
Rockaway, NJ (07866)	20639
Roseland, NJ (07068)	5568
Rutherford, NJ (07070)	15695
Lyndhurst, NJ (07071)	17397
Carlstadt, NJ (07072)	5244
East Rutherford, NJ (07073)	7669
Moonachie, NJ (07074)	2419
Wood Ridge, NJ (07075)	6891
Saddle River, NJ (07458)	10410
Sayreville, NJ (08872)	16564
Scotch Plains, NJ (07076)	21342
Secaucus, NJ (07094)	14192
Sewaren, NJ (07077)	2427
Short Hills, NJ (07078)	12661
Somerset, NJ (08873)	42921
Somerville, NJ (08876)	19420
South Amboy, NJ (08879)	18878
South Bound Brook, NJ (08880)	3957
South Orange, NJ (07079)	13008
South Plainfield, NJ (07080)	20808
South River, NJ (08882)	13440
Sparta, NJ (07871)	18457
Spotswood, NJ (08884)	7032
Springfield, NJ (07081)	14082
Stanhope, NJ (07874)	8305
Stewartsville, NJ (08886)	6042
Stirling, NJ (07980)	2093
Stockholm, NJ (07460)	3178
Succasunna, NJ (07876)	9849
Summit, NJ (07901)	19255
Sussex, NJ (07461)	16853
Teaneck, NJ (07666)	33593
Tenafly, NJ (07670)	12590
Three Bridges, NJ (08887)	978
Towaco, NJ (07082)	5229
Union, NJ (07083)	45808
Weehawken, NJ (07086)	9749
Union City, NJ (07087)	47868
Vauxhall, NJ (07088)	2775
Vernon, NJ (07462)	5696
Waldwick, NJ (07463)	8512
Wanaque, NJ (07465)	5544
Washington, NJ (07882)	12451
Wayne, NJ (07470)	46902
Westfield, NJ (07090)	26906
Mountainside, NJ (07092)	5963
West Milford, NJ (07480)	14392
West New York, NJ (07093)	42640
New York, NY (10035)	20395
New York, NY (10036)	21944
New York, NY (10037)	13151
New York, NY (10038)	15088
New York, NY (10039)	17839
New York, NY (10040)	33218
New York, NY (10044)	6218
New York, NY (10065)	18690
New York, NY (10069)	3509
New York, NY (10075)	16912
New York, NY (10105)	381
New York, NY (10107)	598
New York, NY (10111)	1302
New York, NY (10112)	395
New York, NY (10118)	391
New York, NY (10123)	445
New York, NY (10128)	47627
New York, NY (10162)	1243
New York, NY (10165)	444
New York, NY (10168)	427
New York, NY (10170)	504
New York, NY (10172)	602
New York, NY (10280)	5755
New York, NY (10281)	2180
New York, NY (10282)	3575
Accord, NY (12404)	2879
Acra, NY (12405)	548
Amawalk, NY (10501)	1186
Amenia, NY (12501)	1765
Ancram, NY (12502)	832
Ancramdale, NY (12503)	560
Ardsley, NY (10502)	5344
Arkville, NY (12406)	519
Armonk, NY (10504)	10689
Baldwin Place, NY (10505)	1113
Barryville, NY (12719)	741
Beacon, NY (12508)	13589
Bearsville, NY (12409)	836
Bedford, NY (10506)	5515
Bedford Hills, NY (10507)	4470
Blauvelt, NY (10913)	4717
Bloomingburg, NY (12721)	5354
Bloomington, NY (12411)	455
Boiceville, NY (12412)	551
Brewster, NY (10509)	16797
Briarcliff Manor, NY (10510)	9491
Buchanan, NY (10511)	1934
Cairo, NY (12413)	2425
Callicoon, NY (12723)	1209
Campbell Hall, NY (10916)	3925
Carmel, NY (10512)	21610
Catskill, NY (12414)	7717
Central Valley, NY (10917)	1795
Chappaqua, NY (10514)	11356
Chester, NY (10918)	9445
Circleville, NY (10919)	1027
Claverack, NY (12513)	1083
Clinton Corners, NY (12514)	2470
Clintondale, NY (12515)	1419
Cochecton, NY (12726)	871
Cold Spring, NY (10516)	4515
Congers, NY (10920)	7748
Copake, NY (12516)	1346
Cornwall, NY (12518)	5063
Cornwall On Hudson, NY (12520)	2843
Cottekill, NY (12419)	621
Craryville, NY (12521)	1295
Cross River, NY (10518)	1336
Croton On Hudson, NY (10520)	10857
Cuddebackville, NY (12729)	1473
Dobbs Ferry, NY (10522)	8950
Dover Plains, NY (12522)	4008
East Durham, NY (12423)	849
Eldred, NY (12732)	649
Elizaville, NY (12523)	1476
Ellenville, NY (12428)	4494
Elmsford, NY (10523)	6748
Ferndale, NY (12734)	981
Fishkill, NY (12524)	12215
Fleischmanns, NY (12430)	765
Florida, NY (10921)	3677
Freehold, NY (12431)	1188
Gardiner, NY (12525)	3067
Garnerville, NY (10923)	7608
Garrison, NY (10524)	3723
Germantown, NY (12526)	3079
Glen Spey, NY (12737)	1516
Goldens Bridge, NY (10526)	1845
Goshen, NY (10924)	10360
Grahamsville, NY (12740)	1723
Grand Gorge, NY (12434)	547
Granite Springs, NY (10527)	901
Greenwood Lake, NY (10925)	4306
Harriman, NY (10926)	3202
Harrison, NY (10528)	10036
Hartsdale, NY (10530)	11513
Haverstraw, NY (10927)	9010
Hawthorne, NY (10532)	4643
High Falls, NY (12440)	1589
Highland, NY (12528)	10839
Highland Falls, NY (10928)	3618
Highland Mills, NY (10930)	7893
Hillburn, NY (10931)	780
Hillsdale, NY (12529)	1976
Holmes, NY (12531)	2800
Hopewell Junction, NY (12533)	22054
Hudson, NY (12534)	12083
Huguenot, NY (12746)	1041
Hunter, NY (12442)	772
Hurley, NY (12443)	3582
Hurleyville, NY (12747)	1416
Hyde Park, NY (12538)	11224
Irvington, NY (10533)	6867
Jefferson Valley, NY (10535)	638
Jeffersonville, NY (12748)	1629
Katonah, NY (10536)	9794
Kerhonkson, NY (12446)	3920
Kiamesha Lake, NY (12751)	719
Kingston, NY (12401)	25786
Lagrangeville, NY (12540)	6900
Lake Katrine, NY (12449)	2895
Lake Peekskill, NY (10537)	2112
Larchmont, NY (10538)	15315
Leeds, NY (12451)	1419
Liberty, NY (12754)	4684
Livingston Manor, NY (12758)	3075
Loch Sheldrake, NY (12759)	1080
Mahopac, NY (10541)	21933
Mamaroneck, NY (10543)	16242
Margaretville, NY (12455)	1398
Marlboro, NY (12542)	5193
Maybrook, NY (12543)	2531
Middletown, NY (10940)	36707
Middletown, NY (10941)	11451
Millbrook, NY (12545)	3767
Millerton, NY (12546)	2454
Millwood, NY (10546)	1370
Milton, NY (12547)	2371
Modena, NY (12548)	1397
Mohegan Lake, NY (10547)	6139
Mongaup Valley, NY (12762)	460
Monroe, NY (10950)	31099
Monsey, NY (10952)	23954
Montgomery, NY (12549)	8716
Monticello, NY (12701)	7784
Forestburgh, NY (12777)	613
Montrose, NY (10548)	2607
Mountain Dale, NY (12763)	666
Mount Kisco, NY (10549)	13969
Mount Marion, NY (12456)	734
Mount Tremper, NY (12457)	564
Mount Vernon, NY (10550)	26875
Mount Vernon, NY (10552)	16046
Mount Vernon, NY (10553)	8512
Nanuet, NY (10954)	20221
Napanoch, NY (12458)	1907
Narrowsburg, NY (12764)	1300
Neversink, NY (12765)	818
Newburgh, NY (12550)	41479
New Windsor, NY (12553)	20131
New City, NY (10956)	28938
New Hampton, NY (10958)	2845
New Paltz, NY (12561)	11547
New Rochelle, NY (10801)	29299
Pelham, NY (10803)	11015
New Rochelle, NY (10804)	13257
New Rochelle, NY (10805)	13977
North Salem, NY (10560)	3819
Nyack, NY (10960)	11889
Olivebridge, NY (12461)	1374
Orangeburg, NY (10962)	4396
Ossining, NY (10562)	24284
Otisville, NY (10963)	2227
Palenville, NY (12463)	1231
Palisades, NY (10964)	1300
Parksville, NY (12768)	763
Patterson, NY (12563)	6286
Pawling, NY (12564)	5933
Pearl River, NY (10965)	13258
Peekskill, NY (10566)	18979
Cortlandt Manor, NY (10567)	17127
Philmont, NY (12565)	1474
Phoenicia, NY (12464)	816
Piermont, NY (10968)	1945
Pine Bush, NY (12566)	8638
Pine Island, NY (10969)	1106
Pine Plains, NY (12567)	2338
Pleasant Valley, NY (12569)	8610
Pleasantville, NY (10570)	10970
Pomona, NY (10970)	8344
Port Chester, NY (10573)	30334
Port Ewen, NY (12466)	2628
Port Jervis, NY (12771)	11021
Poughkeepsie, NY (12601)	27784
Poughkeepsie, NY (12603)	35770
Poughquag, NY (12570)	6359
Pound Ridge, NY (10576)	4719
Prattsville, NY (12468)	881
Preston Hollow, NY (12469)	526
Purchase, NY (10577)	3132
Purdys, NY (10578)	775
Putnam Valley, NY (10579)	7683
Red Hook, NY (12571)	8103
Rhinebeck, NY (12572)	7502
Rock Hill, NY (12775)	2162
Rock Tavern, NY (12575)	2009
Roscoe, NY (12776)	1600
Rosendale, NY (12472)	1409
Round Top, NY (12473)	741
Roxbury, NY (12474)	985
Rye, NY (10580)	14988
Salisbury Mills, NY (12577)	1799
Salt Point, NY (12578)	2043
Saugerties, NY (12477)	14990
Scarsdale, NY (10583)	36163
Shandaken, NY (12480)	458
Shokan, NY (12481)	1200
Shrub Oak, NY (10588)	2133
Slate Hill, NY (10973)	2034
Sloatsburg, NY (10974)	2747
Somers, NY (10589)	7704
South Cairo, NY (12482)	691
South Fallsburg, NY (12779)	1551
South Salem, NY (10590)	6110
Sparkill, NY (10976)	1343
Sparrow Bush, NY (12780)	2008
Spring Valley, NY (10977)	39075
Staatsburg, NY (12580)	3379
Stanfordville, NY (12581)	1786
Stone Ridge, NY (12484)	2600
Stony Point, NY (10980)	12001
Stormville, NY (12582)	4205
Suffern, NY (10901)	19926
Swan Lake, NY (12783)	1079
Tannersville, NY (12485)	811
Tappan, NY (10983)	5218
Tarrytown, NY (10591)	18812
Thiells, NY (10984)	2563
Thornwood, NY (10594)	4416
Tillson, NY (12486)	1336
Tivoli, NY (12583)	1776
Tomkins Cove, NY (10986)	1596
Tuxedo Park, NY (10987)	2987
Ulster Park, NY (12487)	2415
Valhalla, NY (10595)	5730
Valley Cottage, NY (10989)	8400
Verbank, NY (12585)	833
Waccabuc, NY (10597)	976
Walden, NY (12586)	10376
Wallkill, NY (12589)	11510
Wappingers Falls, NY (12590)	30481
Warwick, NY (10990)	17206
Washingtonville, NY (10992)	8545
Wassaic, NY (12592)	1042
West Haverstraw, NY (10993)	3858
West Hurley, NY (12491)	1770
West Nyack, NY (10994)	6663
West Point, NY (10996)	2389
West Shokan, NY (12494)	600
Westtown, NY (10998)	2808
White Lake, NY (12786)	524
White Plains, NY (10601)	8255
White Plains, NY (10603)	14937
West Harrison, NY (10604)	9286
White Plains, NY (10605)	16733
White Plains, NY (10606)	12643
White Plains, NY (10607)	6475
White Sulphur Springs, NY (12787)	493
Windham, NY (12496)	1153
Wingdale, NY (12594)	3531
Woodbourne, NY (12788)	1608
Woodridge, NY (12789)	1290
Woodstock, NY (12498)	4117
Wurtsboro, NY (12790)	3663
Yonkers, NY (10701)	43733
Yonkers, NY (10702)	530
Yonkers, NY (10703)	16271
Yonkers, NY (10704)	25409
Yonkers, NY (10705)	28216
Hastings On Hudson, NY (10706)	7877
Tuckahoe, NY (10707)	8325
Bronxville, NY (10708)	18761
Eastchester, NY (10709)	8242
Yonkers, NY (10710)	22379
Yorktown Heights, NY (10598)	25981
Youngsville, NY (12791)	563
Brooklyn, NY (11201)	37285
Brooklyn, NY (11203)	55405
Brooklyn, NY (11204)	54898
Brooklyn, NY (11205)	22852
Brooklyn, NY (11206)	50200
Brooklyn, NY (11207)	61265
Brooklyn, NY (11208)	65751
Brooklyn, NY (11209)	51567
Brooklyn, NY (11210)	46104
Brooklyn, NY (11211)	57386
Brooklyn, NY (11212)	56806
Brooklyn, NY (11213)	42622
Brooklyn, NY (11214)	62973
Brooklyn, NY (11215)	51113
Brooklyn, NY (11216)	34873
Brooklyn, NY (11217)	25348
Brooklyn, NY (11218)	51742
Brooklyn, NY (11219)	56627
Brooklyn, NY (11220)	73470
Brooklyn, NY (11221)	50075
Brooklyn, NY (11222)	29492
Brooklyn, NY (11223)	51878
Brooklyn, NY (11224)	31619
Brooklyn, NY (11225)	42923
Brooklyn, NY (11226)	74527
Brooklyn, NY (11228)	30673
Brooklyn, NY (11229)	58851
Brooklyn, NY (11230)	56454
Brooklyn, NY (11231)	25202
Brooklyn, NY (11232)	17338
Brooklyn, NY (11233)	41642
Brooklyn, NY (11234)	67156
Brooklyn, NY (11235)	59131
Brooklyn, NY (11236)	71345
Brooklyn, NY (11237)	31061
Brooklyn, NY (11238)	37151
Brooklyn, NY (11239)	10182
Inwood, NY (11096)	6063
Far Rockaway, NY (11691)	35386
Arverne, NY (11692)	12619
Far Rockaway, NY (11693)	8984
Rockaway Park, NY (11694)	14148
Breezy Point, NY (11697)	3632
Floral Park, NY (11001)	23250
Elmont, NY (11003)	35663
Glen Oaks, NY (11004)	11118
Floral Park, NY (11005)	1772
Flushing, NY (11354)	40706
Flushing, NY (11355)	67548
College Point, NY (11356)	18183
Whitestone, NY (11357)	32492
Flushing, NY (11358)	29599
Bayside, NY (11360)	16104
Bayside, NY (11361)	22958
Little Neck, NY (11362)	14936
Little Neck, NY (11363)	6048
Oakland Gardens, NY (11364)	29752
Fresh Meadows, NY (11365)	33762
Fresh Meadows, NY (11366)	11462
Flushing, NY (11367)	30463
Corona, NY (11368)	67717
East Elmhurst, NY (11369)	25709
East Elmhurst, NY (11370)	20338
Jackson Heights, NY (11372)	53879
Elmhurst, NY (11373)	75771
Rego Park, NY (11374)	35181
Forest Hills, NY (11375)	56345
Woodside, NY (11377)	66214
Maspeth, NY (11378)	27038
Middle Village, NY (11379)	28507
Ridgewood, NY (11385)	75737
Franklin Square, NY (11010)	20788
Great Neck, NY (11020)	5513
Great Neck, NY (11021)	15695
Great Neck, NY (11023)	7517
Great Neck, NY (11024)	6037
Cambria Heights, NY (11411)	15695
Saint Albans, NY (11412)	26508
Springfield Gardens, NY (11413)	30686
Howard Beach, NY (11414)	21425
Kew Gardens, NY (11415)	14541
Ozone Park, NY (11416)	18651
Ozone Park, NY (11417)	23069
Richmond Hill, NY (11418)	26725
South Richmond Hill, NY (11419)	35160
South Ozone Park, NY (11420)	34717
Woodhaven, NY (11421)	31446
Rosedale, NY (11422)	23615
Hollis, NY (11423)	23449
Bellerose, NY (11426)	14806
Queens Village, NY (11427)	18925
Queens Village, NY (11428)	16017
Queens Village, NY (11429)	19295
Jamaica, NY (11432)	41968
Jamaica, NY (11433)	21603
Jamaica, NY (11434)	44414
Jamaica, NY (11435)	38992
Jamaica, NY (11436)	13320
Long Island City, NY (11101)	18466
Astoria, NY (11102)	25440
Astoria, NY (11103)	28705
Sunnyside, NY (11104)	22394
Astoria, NY (11105)	28457
Astoria, NY (11106)	30268
Long Island City, NY (11109)	2570
Manhasset, NY (11030)	16946
New Hyde Park, NY (11040)	36932
New Hyde Park, NY (11042)	514
Port Washington, NY (11050)	25840
Staten Island, NY (10301)	26662
Staten Island, NY (10302)	12355
Staten Island, NY (10303)	18615
Staten Island, NY (10304)	31225
Staten Island, NY (10305)	31760
Staten Island, NY (10306)	45786
Staten Island, NY (10307)	10873
Staten Island, NY (10308)	23052
Staten Island, NY (10309)	25371
Staten Island, NY (10310)	17604
Staten Island, NY (10312)	50774
Staten Island, NY (10314)	68561
Albertson, NY (11507)	6679
Amityville, NY (11701)	21463
Atlantic Beach, NY (11509)	2407
Babylon, NY (11702)	12983
North Babylon, NY (11703)	15215
West Babylon, NY (11704)	32867
Baldwin, NY (11510)	28565
Bayport, NY (11705)	7048
Bay Shore, NY (11706)	50386
Bayville, NY (11709)	5995
Bellmore, NY (11710)	30778
Bellport, NY (11713)	8292
Bethpage, NY (11714)	20782
Blue Point, NY (11715)	4069
Bohemia, NY (11716)	9356
Brentwood, NY (11717)	48090
Brightwaters, NY (11718)	2966
Brookhaven, NY (11719)	2746
Calverton, NY (11933)	5527
Carle Place, NY (11514)	4202
Cedarhurst, NY (11516)	6033
Centereach, NY (11720)	25056
Center Moriches, NY (11934)	6565
Centerport, NY (11721)	5663
Central Islip, NY (11722)	27814
Islandia, NY (11749)	2667
Cold Spring Harbor, NY (11724)	3232
Commack, NY (11725)	26411
Copiague, NY (11726)	17101
Coram, NY (11727)	23345
Cutchogue, NY (11935)	3154
Deer Park, NY (11729)	23876
East Hampton, NY (11937)	13646
East Islip, NY (11730)	12627
East Marion, NY (11939)	907
East Meadow, NY (11554)	32480
East Moriches, NY (11940)	4636
East Northport, NY (11731)	26703
East Norwich, NY (11732)	3168
Eastport, NY (11941)	2190
East Quogue, NY (11942)	4125
East Rockaway, NY (11518)	9543
East Setauket, NY (11733)	16262
Farmingdale, NY (11735)	27845
Farmingville, NY (11738)	14404
Freeport, NY (11520)	35818
Garden City, NY (11530)	24839
Glen Cove, NY (11542)	21656
Glen Head, NY (11545)	11138
Greenlawn, NY (11740)	8014
Greenport, NY (11944)	3484
Greenvale, NY (11548)	1283
Hampton Bays, NY (11946)	11209
Hempstead, NY (11550)	40113
Hewlett, NY (11557)	7435
Hicksville, NY (11801)	35460
Plainview, NY (11803)	26533
Old Bethpage, NY (11804)	4648
Holbrook, NY (11741)	24709
Holtsville, NY (11742)	11646
Huntington, NY (11743)	37726
Huntington Station, NY (11746)	56971
Melville, NY (11747)	18428
Island Park, NY (11558)	6963
Islip, NY (11751)	12779
Islip Terrace, NY (11752)	8508
Jericho, NY (11753)	12072
Kings Park, NY (11754)	16276
Lake Grove, NY (11755)	10779
Laurel, NY (11948)	998
Lawrence, NY (11559)	6762
Levittown, NY (11756)	38330
Lindenhurst, NY (11757)	39467
Locust Valley, NY (11560)	6072
Long Beach, NY (11561)	29905
Lynbrook, NY (11563)	19016
Malverne, NY (11565)	8167
Manorville, NY (11949)	11993
Massapequa, NY (11758)	49089
Massapequa Park, NY (11762)	20692
Mastic, NY (11950)	12942
Mastic Beach, NY (11951)	10520
Mattituck, NY (11952)	4432
Medford, NY (11763)	23711
Merrick, NY (11566)	32903
Middle Island, NY (11953)	10735
Miller Place, NY (11764)	11529
Mill Neck, NY (11765)	609
Mineola, NY (11501)	16972
Montauk, NY (11954)	3976
Moriches, NY (11955)	2780
Mount Sinai, NY (11766)	11102
Nesconset, NY (11767)	12745
Northport, NY (11768)	19381
Oakdale, NY (11769)	8287
Orient, NY (11957)	803
Oyster Bay, NY (11771)	8639
Patchogue, NY (11772)	35623
Peconic, NY (11958)	846
Port Jefferson Station, NY (11776)	20409
Port Jefferson, NY (11777)	7921
Ridge, NY (11961)	10813
Riverhead, NY (11901)	18288
Rockville Centre, NY (11570)	23850
Oceanside, NY (11572)	27962
Rocky Point, NY (11778)	10703
Ronkonkoma, NY (11779)	32911
Roosevelt, NY (11575)	13013
Roslyn, NY (11576)	11797
Roslyn Heights, NY (11577)	10881
Sag Harbor, NY (11963)	6438
Saint James, NY (11780)	13135
Sayville, NY (11782)	13703
Sea Cliff, NY (11579)	4384
Seaford, NY (11783)	19289
Selden, NY (11784)	20687
Shirley, NY (11967)	21343
Shoreham, NY (11786)	5684
Smithtown, NY (11787)	30670
Hauppauge, NY (11788)	14999
Sound Beach, NY (11789)	6415
Southampton, NY (11968)	8237
Southold, NY (11971)	5443
Stony Brook, NY (11790)	12887
Syosset, NY (11791)	22997
Uniondale, NY (11553)	20800
Valley Stream, NY (11580)	33773
Valley Stream, NY (11581)	18314
Wading River, NY (11792)	7530
Wantagh, NY (11793)	29209
Water Mill, NY (11976)	2079
Old Westbury, NY (11568)	3254
Westbury, NY (11590)	38259
Westhampton, NY (11977)	2110
Westhampton Beach, NY (11978)	3007
West Hempstead, NY (11552)	20840
West Islip, NY (11795)	22905
West Sayville, NY (11796)	3248
Williston Park, NY (11596)	9478
Woodbury, NY (11797)	8301
Woodmere, NY (11598)	11226
Wyandanch, NY (11798)	12181
Yaphank, NY (11980)	3573
Adams, NY (13605)	3684
Adams Center, NY (13606)	2328
Afton, NY (13730)	2321
Albany, NY (12202)	6316
Albany, NY (12203)	20438
Albany, NY (12204)	5912
Albany, NY (12205)	23888
Albany, NY (12206)	10549
Albany, NY (12207)	984
Albany, NY (12208)	14663
Albany, NY (12209)	8069
Albany, NY (12210)	6363
Albany, NY (12211)	10624
Alexandria Bay, NY (13607)	1759
Altamont, NY (12009)	6187
Altmar, NY (13302)	1196
Altona, NY (12910)	1436
Amsterdam, NY (12010)	22566
Andes, NY (13731)	853
Antwerp, NY (13608)	1275
Apalachin, NY (13732)	7253
Argyle, NY (12809)	2994
Athens, NY (12015)	2840
Athol, NY (12810)	541
Auburn, NY (13021)	31058
Aurora, NY (13026)	1098
Au Sable Forks, NY (12912)	1778
Ava, NY (13303)	977
Averill Park, NY (12018)	6808
Bainbridge, NY (13733)	4218
Baldwinsville, NY (13027)	27650
Ballston Spa, NY (12020)	26539
Barneveld, NY (13304)	1556
Barton, NY (13734)	1739
Berkshire, NY (13736)	2030
Berlin, NY (12022)	817
Berne, NY (12023)	1790
Bernhards Bay, NY (13028)	1020
Binghamton, NY (13901)	14798
Binghamton, NY (13903)	14883
Binghamton, NY (13904)	7084
Binghamton, NY (13905)	18513
Black River, NY (13612)	2343
Bloomingdale, NY (12913)	931
Bloomville, NY (13739)	777
Blossvale, NY (13308)	2681
Bolton Landing, NY (12814)	1449
Bombay, NY (12914)	616
Boonville, NY (13309)	4869
Bouckville, NY (13310)	548
Brant Lake, NY (12815)	889
Brasher Falls, NY (13613)	1777
Brewerton, NY (13029)	6090
Bridgeport, NY (13030)	3553
Broadalbin, NY (12025)	4771
Brookfield, NY (13314)	454
Brushton, NY (12916)	1630
Burke, NY (12917)	1128
Burlington Flats, NY (13315)	1068
Ballston Lake, NY (12019)	13129
Burnt Hills, NY (12027)	3731
Cadyville, NY (12918)	2062
Calcium, NY (13616)	1340
Cambridge, NY (12816)	3769
Camden, NY (13316)	5208
Camillus, NY (13031)	14099
Canaan, NY (12029)	903
Canajoharie, NY (13317)	2925
Canastota, NY (13032)	10386
Candor, NY (13743)	3127
Canton, NY (13617)	6890
Cape Vincent, NY (13618)	1612
Caroga Lake, NY (12032)	878
Carthage, NY (13619)	7939
Cassville, NY (13318)	1047
Castle Creek, NY (13744)	1008
Castleton On Hudson, NY (12033)	6953
Castorland, NY (13620)	1612
Cato, NY (13033)	3115
Cayuga, NY (13034)	1505
Cazenovia, NY (13035)	6634
Central Bridge, NY (12035)	785
Central Square, NY (13036)	7311
Chadwicks, NY (13319)	805
Champlain, NY (12919)	2916
Chase Mills, NY (13621)	512
Chateaugay, NY (12920)	1918
Chatham, NY (12037)	3004
Chaumont, NY (13622)	1856
Chazy, NY (12921)	2125
Chenango Forks, NY (13746)	2348
Cherry Valley, NY (13320)	1642
Chestertown, NY (12817)	1974
Chittenango, NY (13037)	7640
Cincinnatus, NY (13040)	2228
Clarksville, NY (12041)	511
Cicero, NY (13039)	15407
Clay, NY (13041)	9355
Clayton, NY (13624)	3954
Clayville, NY (13322)	1023
Cleveland, NY (13042)	1823
Clifton Park, NY (12065)	37357
Clinton, NY (13323)	8049
Cobleskill, NY (12043)	5489
Coeymans Hollow, NY (12046)	626
Cohoes, NY (12047)	15353
Cold Brook, NY (13324)	1634
Colton, NY (13625)	1560
Conklin, NY (13748)	3378
Constable, NY (12926)	1653
Constableville, NY (13325)	758
Constantia, NY (13044)	2224
Cooperstown, NY (13326)	4529
Copenhagen, NY (13626)	1753
Corinth, NY (12822)	5024
Cortland, NY (13045)	19439
Coxsackie, NY (12051)	2955
West Coxsackie, NY (12192)	1254
Croghan, NY (13327)	1744
Cropseyville, NY (12052)	1252
Crown Point, NY (12928)	1627
Davenport, NY (13750)	869
Deansboro, NY (13328)	1010
De Kalb Junction, NY (13630)	1010
Delanson, NY (12053)	3842
Delancey, NY (13752)	616
Delhi, NY (13753)	3344
Delmar, NY (12054)	15544
Deposit, NY (13754)	2640
De Ruyter, NY (13052)	1563
Dexter, NY (13634)	3229
Diamond Point, NY (12824)	757
Dickinson Center, NY (12930)	454
Dolgeville, NY (13329)	2911
Downsville, NY (13755)	1069
Dryden, NY (13053)	3793
Duanesburg, NY (12056)	2123
Durhamville, NY (13054)	1312
Buskirk, NY (12028)	1039
Eagle Bridge, NY (12057)	1434
Earlton, NY (12058)	1194
Earlville, NY (13332)	1995
East Berne, NY (12059)	1447
East Chatham, NY (12060)	1167
East Greenbush, NY (12061)	8215
East Meredith, NY (13757)	798
East Nassau, NY (12062)	1465
East Schodack, NY (12063)	563
East Syracuse, NY (13057)	13212
Eaton, NY (13334)	1036
Edmeston, NY (13335)	1249
Edwards, NY (13635)	804
Elbridge, NY (13060)	2521
Elizabethtown, NY (12932)	1086
Ellenburg Center, NY (12934)	735
Ellenburg Depot, NY (12935)	1259
Endicott, NY (13760)	36643
Erieville, NY (13061)	921
Esperance, NY (12066)	1819
Essex, NY (12936)	538
Evans Mills, NY (13637)	3206
Fabius, NY (13063)	1634
Fayetteville, NY (13066)	11455
Feura Bush, NY (12067)	1314
Fly Creek, NY (13337)	741
Fonda, NY (12068)	2499
Forestport, NY (13338)	1091
Fort Ann, NY (12827)	3320
Fort Covington, NY (12937)	1201
Fort Edward, NY (12828)	7917
Fort Johnson, NY (12070)	1214
Fort Plain, NY (13339)	4853
Frankfort, NY (13340)	6645
Franklin, NY (13775)	1340
Freeville, NY (13068)	4276
Fulton, NY (13069)	19739
Fultonville, NY (12072)	2216
Galway, NY (12074)	2603
Gansevoort, NY (12831)	14655
Genoa, NY (13071)	897
Georgetown, NY (13072)	633
Ghent, NY (12075)	2679
Gilbertsville, NY (13776)	593
Gilboa, NY (12076)	1012
Glen Aubrey, NY (13777)	763
Glenfield, NY (13343)	1373
Glenmont, NY (12077)	5577
Glens Falls, NY (12801)	12364
South Glens Falls, NY (12803)	6658
Queensbury, NY (12804)	23153
Gloversville, NY (12078)	17802
Gouverneur, NY (13642)	6605
Granville, NY (12832)	4864
Greene, NY (13778)	4736
Greenfield Center, NY (12833)	3878
Greenville, NY (12083)	3257
Greenwich, NY (12834)	5642
Groton, NY (13073)	5355
Guilderland, NY (12084)	3678
Guilderland Center, NY (12085)	421
Guilford, NY (13780)	869
Hadley, NY (12835)	2210
Hagaman, NY (12086)	1715
Hague, NY (12836)	538
Hamden, NY (13782)	577
Hamilton, NY (13346)	3336
Hammond, NY (13646)	1689
Hampton, NY (12837)	632
Hancock, NY (13783)	1972
Hannacroix, NY (12087)	1085
Hannibal, NY (13074)	3504
Harpursville, NY (13787)	2851
Harrisville, NY (13648)	1831
Hartford, NY (12838)	629
Hartwick, NY (13348)	1126
Hastings, NY (13076)	1981
Henderson, NY (13650)	993
Herkimer, NY (13350)	6793
Hermon, NY (13652)	1353
Heuvelton, NY (13654)	1560
Hobart, NY (13788)	776
Hogansburg, NY (13655)	2150
Holland Patent, NY (13354)	2857
Homer, NY (13077)	5647
Hoosick Falls, NY (12090)	4771
Howes Cave, NY (12092)	1009
Hubbardsville, NY (13355)	662
Hudson Falls, NY (12839)	10569
Ilion, NY (13357)	8684
Indian Lake, NY (12842)	1047
Jamesville, NY (13078)	8134
Jay, NY (12941)	1076
Jefferson, NY (12093)	1210
Johnsburg, NY (12843)	465
Johnson City, NY (13790)	14367
Johnsonville, NY (12094)	1984
Johnstown, NY (12095)	9856
Jordan, NY (13080)	3149
Jordanville, NY (13361)	514
Keene, NY (12942)	531
Keeseville, NY (12944)	3187
Kinderhook, NY (12106)	2236
King Ferry, NY (13081)	987
Kirkville, NY (13082)	4083
Kirkwood, NY (13795)	3219
Lacona, NY (13083)	1470
La Fargeville, NY (13656)	2118
La Fayette, NY (13084)	3979
Lake Clear, NY (12945)	589
Lake George, NY (12845)	4377
Lake Luzerne, NY (12846)	2848
Lake Placid, NY (12946)	4566
Latham, NY (12110)	17260
Laurens, NY (13796)	1048
Lee Center, NY (13363)	2027
Lewis, NY (12950)	670
Lisbon, NY (13658)	1950
Lisle, NY (13797)	1735
Little Falls, NY (13365)	6606
Liverpool, NY (13088)	18946
Liverpool, NY (13090)	26337
Locke, NY (13092)	2015
Long Lake, NY (12847)	601
Lowville, NY (13367)	6623
Lyon Mountain, NY (12952)	468
Lyons Falls, NY (13368)	967
Mc Donough, NY (13801)	916
Mc Graw, NY (13101)	2131
Madison, NY (13402)	1191
Madrid, NY (13660)	1536
Maine, NY (13802)	869
Malone, NY (12953)	8697
Manlius, NY (13104)	14081
Mannsville, NY (13661)	1185
Marathon, NY (13803)	3296
Marcellus, NY (13108)	5576
Marcy, NY (13403)	3831
Marietta, NY (13110)	2062
Martville, NY (13111)	1307
Maryland, NY (12116)	1456
Massena, NY (13662)	12957
Mayfield, NY (12117)	2805
Mechanicville, NY (12118)	11777
Medusa, NY (12120)	476
Melrose, NY (12121)	1764
Memphis, NY (13112)	1647
Mexico, NY (13114)	5422
Middleburgh, NY (12122)	3493
Middle Granville, NY (12849)	601
Middle Grove, NY (12850)	2376
Middleville, NY (13406)	688
Milford, NY (13807)	1056
Mineville, NY (12956)	913
Minoa, NY (13116)	2992
Mohawk, NY (13407)	4325
Moira, NY (12957)	1332
Mooers, NY (12958)	1602
Mooers Forks, NY (12959)	1160
Moravia, NY (13118)	4404
Moriah, NY (12960)	905
Morris, NY (13808)	1411
Morrisonville, NY (12962)	4812
Morristown, NY (13664)	481
Morrisville, NY (13408)	1954
Mount Upton, NY (13809)	1318
Mount Vision, NY (13810)	906
Munnsville, NY (13409)	1917
Nassau, NY (12123)	4397
Natural Bridge, NY (13665)	739
Nedrow, NY (13120)	1890
Newark Valley, NY (13811)	3675
New Berlin, NY (13411)	2513
New Hartford, NY (13413)	13611
New Lebanon, NY (12125)	1227
Newport, NY (13416)	1733
New Woodstock, NY (13122)	911
New York Mills, NY (13417)	2653
Nichols, NY (13812)	1895
Nineveh, NY (13813)	766
Niverville, NY (12130)	995
Norfolk, NY (13667)	2539
North Bangor, NY (12966)	2234
North Creek, NY (12853)	1136
North Lawrence, NY (12967)	857
Northville, NY (12134)	3112
Norwich, NY (13815)	10438
Norwood, NY (13668)	2591
Ogdensburg, NY (13669)	11813
Old Chatham, NY (12136)	776
Old Forge, NY (13420)	1361
Olmstedville, NY (12857)	512
Oneida, NY (13421)	10880
Oneonta, NY (13820)	13019
Oriskany, NY (13424)	1939
Oriskany Falls, NY (13425)	1497
Oswego, NY (13126)	25103
Otego, NY (13825)	2810
Owego, NY (13827)	9721
Oxford, NY (13830)	3854
Palatine Bridge, NY (13428)	1105
Parish, NY (13131)	3092
Parishville, NY (13672)	625
Pattersonville, NY (12137)	1611
Pennellville, NY (13132)	3516
Peru, NY (12972)	5527
Petersburg, NY (12138)	2425
Philadelphia, NY (13673)	1866
Phoenix, NY (13135)	5559
Plattsburgh, NY (12901)	23334
Plattsburgh, NY (12903)	1025
Plymouth, NY (13832)	549
Poestenkill, NY (12140)	1561
Poland, NY (13431)	1641
Port Byron, NY (13140)	3556
Port Crane, NY (13833)	3541
Porter Corners, NY (12859)	1819
Port Henry, NY (12974)	1235
Port Leyden, NY (13433)	1261
Potsdam, NY (13676)	8585
Pottersville, NY (12860)	664
Preble, NY (13141)	596
Pulaski, NY (13142)	5052
Putnam Station, NY (12861)	496
Ravena, NY (12143)	4366
Red Creek, NY (13143)	2244
Redwood, NY (13679)	1510
Remsen, NY (13438)	2899
Rensselaer, NY (12144)	16674
Rensselaer Falls, NY (13680)	838
Rensselaerville, NY (12147)	513
Rexford, NY (12148)	4162
Richfield Springs, NY (13439)	3180
Richford, NY (13835)	1129
Richland, NY (13144)	991
Richmondville, NY (12149)	1687
Richville, NY (13681)	725
Rock City Falls, NY (12863)	529
Rodman, NY (13682)	771
Rome, NY (13440)	31499
Rotterdam Junction, NY (12150)	812
Round Lake, NY (12151)	731
Rouses Point, NY (12979)	2045
Russell, NY (13684)	879
Sackets Harbor, NY (13685)	1889
Saint Johnsville, NY (13452)	3503
Saint Regis Falls, NY (12980)	1047
Salem, NY (12865)	2966
Salisbury Center, NY (13454)	676
Sand Lake, NY (12153)	896
Sandy Creek, NY (13145)	1493
Saranac, NY (12981)	1955
Saranac Lake, NY (12983)	5950
Saratoga Springs, NY (12866)	29758
Sauquoit, NY (13456)	3560
Savannah, NY (13146)	1756
Schaghticoke, NY (12154)	2549
Schenectady, NY (12302)	24396
Schenectady, NY (12303)	25053
Schenectady, NY (12304)	16525
Schenectady, NY (12305)	2473
Schenectady, NY (12306)	22412
Schenectady, NY (12307)	4565
Schenectady, NY (12308)	10086
Schenectady, NY (12309)	26897
Schenevus, NY (12155)	1378
Schodack Landing, NY (12156)	729
Schoharie, NY (12157)	3363
Schroon Lake, NY (12870)	1459
Schuyler Falls, NY (12985)	931
Schuylerville, NY (12871)	3391
Scipio Center, NY (13147)	955
Selkirk, NY (12158)	5434
Seneca Falls, NY (13148)	8643
Sharon Springs, NY (13459)	1759
Sherburne, NY (13460)	3658
Sherrill, NY (13461)	2789
Shushan, NY (12873)	639
Sidney, NY (13838)	3464
Sidney Center, NY (13839)	1088
Skaneateles, NY (13152)	7233
Slingerlands, NY (12159)	7475
Sloansville, NY (12160)	783
Smyrna, NY (13464)	851
South Colton, NY (13687)	461
South New Berlin, NY (13843)	1424
South Otselic, NY (13155)	505
South Plymouth, NY (13844)	617
Speculator, NY (12164)	503
Sprakers, NY (12166)	1156
Springfield Center, NY (13468)	436
Stamford, NY (12167)	1982
Star Lake, NY (13690)	726
Stephentown, NY (12168)	1639
Sterling, NY (13156)	1413
Stillwater, NY (12170)	4428
Stittville, NY (13469)	656
Stony Creek, NY (12878)	553
Stratford, NY (13470)	541
Stuyvesant, NY (12173)	1386
Summit, NY (12175)	618
Syracuse, NY (13202)	2520
Syracuse, NY (13203)	9714
Syracuse, NY (13204)	12137
Syracuse, NY (13205)	12129
Syracuse, NY (13206)	13046
Syracuse, NY (13207)	10405
Syracuse, NY (13208)	14769
Syracuse, NY (13209)	11191
Syracuse, NY (13210)	9948
Syracuse, NY (13211)	5382
Syracuse, NY (13212)	17382
Syracuse, NY (13214)	6484
Syracuse, NY (13215)	12897
Syracuse, NY (13219)	13675
Syracuse, NY (13224)	6872
Taberg, NY (13471)	2629
Theresa, NY (13691)	2395
Three Mile Bay, NY (13693)	496
Ticonderoga, NY (12883)	4050
Troy, NY (12180)	36062
Troy, NY (12182)	11529
Troy, NY (12183)	2200
Truxton, NY (13158)	1174
Tully, NY (13159)	4590
Tupper Lake, NY (12986)	4768
Turin, NY (13473)	592
Unadilla, NY (13849)	3682
Union Springs, NY (13160)	1726
Utica, NY (13501)	24772
Utica, NY (13502)	23498
Valatie, NY (12184)	5688
Valley Falls, NY (12185)	1709
Vermontville, NY (12989)	784
Vernon, NY (13476)	2767
Vernon Center, NY (13477)	1084
Verona, NY (13478)	2632
Vestal, NY (13850)	18401
Voorheesville, NY (12186)	5935
Waddington, NY (13694)	1255
Walton, NY (13856)	5084
Warners, NY (13164)	2078
Warnerville, NY (12187)	691
Warrensburg, NY (12885)	3783
Waterford, NY (12188)	9784
Waterloo, NY (13165)	8844
Watertown, NY (13601)	28475
Fort Drum, NY (13602)	2867
Watertown, NY (13603)	7685
Waterville, NY (13480)	2737
Watervliet, NY (12189)	13561
Weedsport, NY (13166)	4703
Wells, NY (12190)	618
West Chazy, NY (12992)	4156
West Edmeston, NY (13485)	734
Westerlo, NY (12193)	1820
Westernville, NY (13486)	727
West Leyden, NY (13489)	593
West Monroe, NY (13167)	2825
Westmoreland, NY (13490)	1241
West Oneonta, NY (13861)	556
Westport, NY (12993)	1364
West Sand Lake, NY (12196)	2861
West Winfield, NY (13491)	2989
Whitehall, NY (12887)	3822
Whitesboro, NY (13492)	10302
Whitney Point, NY (13862)	3454
Williamstown, NY (13493)	1602
Willsboro, NY (12996)	1671
Willseyville, NY (13864)	883
Wilmington, NY (12997)	1005
Windsor, NY (13865)	5164
Winthrop, NY (13697)	1587
Worcester, NY (12197)	1746
Wynantskill, NY (12198)	6973
Yorkville, NY (13495)	1732
Bear, DE (19701)	34541
Bethany Beach, DE (19930)	2321
Bridgeville, DE (19933)	6704
Camden Wyoming, DE (19934)	10884
Claymont, DE (19703)	11662
Clayton, DE (19938)	6886
Dagsboro, DE (19939)	5123
Delmar, DE (19940)	4493
Dover, DE (19901)	24829
Dover Afb, DE (19902)	342
Dover, DE (19904)	25911
Ellendale, DE (19941)	1916
Felton, DE (19943)	9612
Frankford, DE (19945)	5338
Frederica, DE (19946)	3517
Georgetown, DE (19947)	12253
Greenwood, DE (19950)	5315
Harbeson, DE (19951)	1447
Harrington, DE (19952)	8258
Hartly, DE (19953)	3609
Hockessin, DE (19707)	15507
Houston, DE (19954)	1320
Laurel, DE (19956)	12111
Lewes, DE (19958)	15994
Lincoln, DE (19960)	4918
Magnolia, DE (19962)	8138
Middletown, DE (19709)	29310
Milford, DE (19963)	14990
Millsboro, DE (19966)	18512
Milton, DE (19968)	8225
Newark, DE (19702)	41451
Newark, DE (19711)	37619
Newark, DE (19713)	25300
New Castle, DE (19720)	47355
Ocean View, DE (19970)	5126
Rehoboth Beach, DE (19971)	9925
Seaford, DE (19973)	19117
Fenwick Island, DE (19944)	441
Selbyville, DE (19975)	6459
Smyrna, DE (19977)	16165
Townsend, DE (19734)	8648
Viola, DE (19979)	646
Wilmington, DE (19801)	9225
Wilmington, DE (19802)	17453
Wilmington, DE (19803)	19593
Wilmington, DE (19804)	15157
Wilmington, DE (19805)	30434
Wilmington, DE (19806)	7007
Wilmington, DE (19807)	7193
Wilmington, DE (19808)	33228
Wilmington, DE (19809)	12162
Wilmington, DE (19810)	22602
Marydel, DE (19964)	1082
Absecon, NJ (08201)	9186
Absecon, NJ (08205)	24427
Allenhurst, NJ (07711)	1496
Allentown, NJ (08501)	5901
Asbury Park, NJ (07712)	31680
Atco, NJ (08004)	10625
Atlantic City, NJ (08401)	29186
Margate City, NJ (08402)	5596
Longport, NJ (08403)	849
Ventnor City, NJ (08406)	9419
Atlantic Highlands, NJ (07716)	7144
Avalon, NJ (08202)	1508
Avon By The Sea, NJ (07717)	1687
Barnegat, NJ (08005)	19593
Barrington, NJ (08007)	4458
Bayville, NJ (08721)	17550
Beach Haven, NJ (08008)	6743
Beachwood, NJ (08722)	9570
Belford, NJ (07718)	5572
Belle Mead, NJ (08502)	10011
Belmar, NJ (07719)	18512
Berlin, NJ (08009)	11467
Beverly, NJ (08010)	9089
Blackwood, NJ (08012)	33128
Bordentown, NJ (08505)	15332
Bradley Beach, NJ (07720)	3588
Brick, NJ (08723)	27903
Brick, NJ (08724)	37268
Bridgeport, NJ (08014)	467
Bridgeton, NJ (08302)	32331
Brielle, NJ (08730)	4502
Brigantine, NJ (08203)	8255
Browns Mills, NJ (08015)	17598
Buena, NJ (08310)	1546
Burlington, NJ (08016)	27446
Camden, NJ (08102)	4388
Camden, NJ (08103)	8064
Camden, NJ (08104)	14926
Camden, NJ (08105)	20084
Audubon, NJ (08106)	8646
Oaklyn, NJ (08107)	10754
Collingswood, NJ (08108)	15534
Merchantville, NJ (08109)	19052
Pennsauken, NJ (08110)	15836
Cape May, NJ (08204)	15523
Cape May Court House, NJ (08210)	13739
Cedarville, NJ (08311)	1831
Chatsworth, NJ (08019)	871
Cherry Hill, NJ (08002)	18807
Cherry Hill, NJ (08003)	27889
Cherry Hill, NJ (08034)	16356
Clarksboro, NJ (08020)	1925
Millstone Township, NJ (08510)	4375
Clayton, NJ (08312)	6392
Clementon, NJ (08021)	37348
Cliffwood, NJ (07721)	2549
Colts Neck, NJ (07722)	9440
Columbus, NJ (08022)	8335
Cookstown, NJ (08511)	897
Cranbury, NJ (08512)	9761
Cream Ridge, NJ (08514)	4004
Chesterfield, NJ (08515)	4172
Deal, NJ (07723)	875
Dorothy, NJ (08317)	1120
Eatontown, NJ (07724)	18937
Egg Harbor City, NJ (08215)	11254
Elmer, NJ (08318)	10908
Englishtown, NJ (07726)	39570
Estell Manor, NJ (08319)	1187
Farmingdale, NJ (07727)	6073
Florence, NJ (08518)	4285
Forked River, NJ (08731)	17395
Franklinville, NJ (08322)	9278
Freehold, NJ (07728)	46233
Gibbsboro, NJ (08026)	2097
Gibbstown, NJ (08027)	4419
Glassboro, NJ (08028)	13452
Glendora, NJ (08029)	4040
Gloucester City, NJ (08030)	10400
Greenwich, NJ (08323)	690
Haddonfield, NJ (08033)	14871
Haddon Heights, NJ (08035)	6656
Hainesport, NJ (08036)	5464
Hammonton, NJ (08037)	20771
Hazlet, NJ (07730)	15325
Highlands, NJ (07732)	4081
Hightstown, NJ (08520)	24186
Holmdel, NJ (07733)	15555
Hopewell, NJ (08525)	4389
Howell, NJ (07731)	35010
Jackson, NJ (08527)	47406
Jobstown, NJ (08041)	897
Keansburg, NJ (07734)	10496
Keyport, NJ (07735)	16520
Kingston, NJ (08528)	431
Voorhees, NJ (08043)	24732
Lakehurst, NJ (08733)	2437
Manchester Township, NJ (08759)	27892
Lakewood, NJ (08701)	52778
Lambertville, NJ (08530)	6511
Landisville, NJ (08326)	1399
Lanoka Harbor, NJ (08734)	6888
Lavallette, NJ (08735)	2840
Lawnside, NJ (08045)	2342
Leesburg, NJ (08327)	695
Leonardo, NJ (07737)	3808
Lincroft, NJ (07738)	5508
Linwood, NJ (08221)	6768
Little Silver, NJ (07739)	5587
Long Branch, NJ (07740)	20885
Lumberton, NJ (08048)	10599
Magnolia, NJ (08049)	4500
Malaga, NJ (08328)	1263
Manahawkin, NJ (08050)	20931
Manasquan, NJ (08736)	11328
Mantoloking, NJ (08738)	831
Mantua, NJ (08051)	9204
Maple Shade, NJ (08052)	15607
Marlboro, NJ (07746)	17313
Marlton, NJ (08053)	40939
Marmora, NJ (08223)	3924
Matawan, NJ (07747)	26986
Mays Landing, NJ (08330)	23573
Medford, NJ (08055)	24851
Mickleton, NJ (08056)	4070
Middletown, NJ (07748)	25426
Millville, NJ (08332)	29211
Milmay, NJ (08340)	794
Minotola, NJ (08341)	1436
Monmouth Beach, NJ (07750)	3013
Monroeville, NJ (08343)	4132
Moorestown, NJ (08057)	18385
Morganville, NJ (07751)	18058
Mount Ephraim, NJ (08059)	4835
Mount Holly, NJ (08060)	21570
Mount Laurel, NJ (08054)	38300
Mount Royal, NJ (08061)	2344
Mullica Hill, NJ (08062)	13484
National Park, NJ (08063)	2747
Neptune, NJ (07753)	30970
New Egypt, NJ (08533)	6225
Newfield, NJ (08344)	5101
Newport, NJ (08345)	646
Newtonville, NJ (08346)	717
Northfield, NJ (08225)	7758
Oakhurst, NJ (07755)	6022
Ocean City, NJ (08226)	10270
Ocean Grove, NJ (07756)	2503
Oceanport, NJ (07757)	5116
Ocean View, NJ (08230)	5385
Palmyra, NJ (08065)	6356
Paulsboro, NJ (08066)	6356
Pedricktown, NJ (08067)	1451
Pemberton, NJ (08068)	5490
Pennington, NJ (08534)	11939
Penns Grove, NJ (08069)	10482
Pennsville, NJ (08070)	11154
Millstone Township, NJ (08535)	4550
Pine Beach, NJ (08741)	2458
Pitman, NJ (08071)	8346
Plainsboro, NJ (08536)	17344
Pleasantville, NJ (08232)	16127
Egg Harbor Township, NJ (08234)	37623
Point Pleasant Beach, NJ (08742)	22127
Port Monmouth, NJ (07758)	4455
Port Norris, NJ (08349)	1575
Port Republic, NJ (08241)	1125
Princeton, NJ (08540)	38222
Princeton, NJ (08542)	2592
Princeton Junction, NJ (08550)	18383
Red Bank, NJ (07701)	19393
Shrewsbury, NJ (07702)	3546
Fort Monmouth, NJ (07703)	664
Fair Haven, NJ (07704)	5437
Richland, NJ (08350)	690
Ringoes, NJ (08551)	5321
Rio Grande, NJ (08242)	2795
Riverside, NJ (08075)	24711
Riverton, NJ (08077)	16482
Rocky Hill, NJ (08553)	654
Roebling, NJ (08554)	3341
Rumson, NJ (07760)	8555
Runnemede, NJ (08078)	7017
Salem, NJ (08079)	8679
Sea Girt, NJ (08750)	3480
Sea Isle City, NJ (08243)	2047
Seaside Heights, NJ (08751)	3094
Seaside Park, NJ (08752)	1913
Sewell, NJ (08080)	33729
Sicklerville, NJ (08081)	41753
Skillman, NJ (08558)	6048
Somerdale, NJ (08083)	8321
Somers Point, NJ (08244)	9358
Bellmawr, NJ (08031)	9879
Spring Lake, NJ (07762)	7512
Stockton, NJ (08559)	4355
Stone Harbor, NJ (08247)	915
Stratford, NJ (08084)	6077
Swedesboro, NJ (08085)	15563
Thorofare, NJ (08086)	7031
Titusville, NJ (08560)	3249
Toms River, NJ (08753)	55159
Toms River, NJ (08755)	21432
Toms River, NJ (08757)	26967
Trenton, NJ (08608)	522
Trenton, NJ (08609)	8578
Trenton, NJ (08610)	25618
Trenton, NJ (08611)	14996
Trenton, NJ (08618)	24531
Trenton, NJ (08619)	19382
Trenton, NJ (08620)	10800
Trenton, NJ (08628)	7650
Trenton, NJ (08629)	9859
Trenton, NJ (08638)	17200
Fort Dix, NJ (08640)	1941
Trenton, NJ (08641)	2070
Lawrence Township, NJ (08648)	25629
Trenton, NJ (08690)	18316
Trenton, NJ (08691)	13091
Tuckerton, NJ (08087)	20609
Villas, NJ (08251)	8038
Vincentown, NJ (08088)	22028
Vineland, NJ (08360)	35585
Vineland, NJ (08361)	14832
Waretown, NJ (08758)	6336
Waterford Works, NJ (08089)	3545
Wenonah, NJ (08090)	7368
West Berlin, NJ (08091)	4550
West Creek, NJ (08092)	3158
West Long Branch, NJ (07764)	5838
Westville, NJ (08093)	7971
Wildwood, NJ (08260)	11807
Williamstown, NJ (08094)	33155
Willingboro, NJ (08046)	27170
Woodbine, NJ (08270)	6102
West Deptford, NJ (08096)	29504
Woodbury Heights, NJ (08097)	2916
Woodstown, NJ (08098)	7744
Wrightstown, NJ (08562)	4380
Addison, NY (14801)	4062
Akron, NY (14001)	8276
Albion, NY (14411)	9630
Alden, NY (14004)	9396
Alexander, NY (14005)	1640
Alfred, NY (14802)	655
Alfred Station, NY (14803)	950
Allegany, NY (14706)	5156
Almond, NY (14804)	1244
Alpine, NY (14805)	924
Andover, NY (14806)	1819
Angelica, NY (14709)	1220
Angola, NY (14006)	8348
Appleton, NY (14008)	1312
Arcade, NY (14009)	4463
Arkport, NY (14807)	2496
Ashville, NY (14710)	3023
Atlanta, NY (14808)	479
Attica, NY (14011)	5024
Cowlesville, NY (14037)	1059
Avoca, NY (14809)	2016
Avon, NY (14414)	6007
Barker, NY (14012)	1965
Basom, NY (14013)	1367
Batavia, NY (14020)	17176
Bath, NY (14810)	9174
Beaver Dams, NY (14812)	2712
Belfast, NY (14711)	1362
Belmont, NY (14813)	1857
Bemus Point, NY (14712)	2789
Bergen, NY (14416)	3504
Big Flats, NY (14814)	1841
Bliss, NY (14024)	1309
Bolivar, NY (14715)	2139
Boston, NY (14025)	2713
Bowmansville, NY (14026)	701
Bradford, NY (14815)	721
Breesport, NY (14816)	592
Brockport, NY (14420)	13210
Brocton, NY (14716)	1834
Brooktondale, NY (14817)	2007
Buffalo, NY (14201)	6563
Buffalo, NY (14202)	2208
Buffalo, NY (14203)	822
Buffalo, NY (14204)	5302
Buffalo, NY (14206)	14988
Buffalo, NY (14207)	14755
Buffalo, NY (14208)	5551
Buffalo, NY (14209)	4984
Buffalo, NY (14210)	10360
Buffalo, NY (14211)	13645
Buffalo, NY (14212)	6607
Buffalo, NY (14213)	13261
Buffalo, NY (14214)	11826
Buffalo, NY (14215)	26790
Buffalo, NY (14216)	17262
Buffalo, NY (14217)	19132
Buffalo, NY (14218)	14210
Buffalo, NY (14219)	9751
Buffalo, NY (14220)	19047
Buffalo, NY (14221)	46526
Buffalo, NY (14222)	8292
Buffalo, NY (14223)	20327
Buffalo, NY (14224)	36062
Buffalo, NY (14225)	28366
Buffalo, NY (14226)	24584
Buffalo, NY (14227)	19784
Buffalo, NY (14228)	14965
Burdett, NY (14818)	1522
Byron, NY (14422)	1892
Caledonia, NY (14423)	4133
Cameron, NY (14819)	521
Cameron Mills, NY (14820)	543
Campbell, NY (14821)	2821
Canandaigua, NY (14424)	22261
Farmington, NY (14425)	9107
Canaseraga, NY (14822)	933
Caneadea, NY (14717)	499
Canisteo, NY (14823)	3137
Cassadaga, NY (14718)	1740
Castile, NY (14427)	1737
Cattaraugus, NY (14719)	2574
Cayuta, NY (14824)	594
Chaffee, NY (14030)	1342
Chemung, NY (14825)	723
Cherry Creek, NY (14723)	1015
Churchville, NY (14428)	7548
Clarence, NY (14031)	8352
Clarence Center, NY (14032)	6906
Clifton Springs, NY (14432)	4537
Clyde, NY (14433)	3546
Clymer, NY (14724)	1837
Cohocton, NY (14826)	1711
Colden, NY (14033)	2051
Collins, NY (14034)	1554
Conesus, NY (14435)	2628
Conewango Valley, NY (14726)	731
Corfu, NY (14036)	4216
Corning, NY (14830)	16367
Cuba, NY (14727)	4239
Dalton, NY (14836)	838
Dansville, NY (14437)	7679
Darien Center, NY (14040)	1945
Delevan, NY (14042)	3060
Depew, NY (14043)	21518
Derby, NY (14047)	5577
Dewittville, NY (14728)	867
Dundee, NY (14837)	3837
Dunkirk, NY (14048)	11192
East Amherst, NY (14051)	18084
East Aurora, NY (14052)	15612
East Bethany, NY (14054)	1165
East Concord, NY (14055)	1229
East Otto, NY (14729)	713
East Rochester, NY (14445)	6390
Eden, NY (14057)	7171
Elba, NY (14058)	1966
Ellicottville, NY (14731)	1241
Elma, NY (14059)	8299
Elmira, NY (14901)	9440
Elmira, NY (14903)	6479
Elmira, NY (14904)	12349
Elmira, NY (14905)	7665
Erin, NY (14838)	1624
Fairport, NY (14450)	37619
Falconer, NY (14733)	3246
Fillmore, NY (14735)	1917
Findley Lake, NY (14736)	498
Forestville, NY (14062)	2791
Franklinville, NY (14737)	3248
Fredonia, NY (14063)	9209
Freedom, NY (14065)	1467
Frewsburg, NY (14738)	3092
Friendship, NY (14739)	2026
Gainesville, NY (14066)	881
Gasport, NY (14067)	4368
Geneseo, NY (14454)	5180
Geneva, NY (14456)	14446
Gerry, NY (14740)	979
Getzville, NY (14068)	6245
Glenwood, NY (14069)	755
Gowanda, NY (14070)	4008
Grand Island, NY (14072)	18204
Great Valley, NY (14741)	1573
Greenwood, NY (14839)	588
Groveland, NY (14462)	582
Hamburg, NY (14075)	37102
Hamlin, NY (14464)	6229
Hammondsport, NY (14840)	2645
Hector, NY (14841)	784
Hemlock, NY (14466)	1557
Henrietta, NY (14467)	8141
Hilton, NY (14468)	16219
Himrod, NY (14842)	634
Hinsdale, NY (14743)	1526
Bloomfield, NY (14469)	5114
Holland, NY (14080)	3863
Holley, NY (14470)	6664
Honeoye, NY (14471)	2559
Honeoye Falls, NY (14472)	7839
Hornell, NY (14843)	9824
Horseheads, NY (14845)	17593
Houghton, NY (14744)	878
Hunt, NY (14846)	573
Interlaken, NY (14847)	1900
Irving, NY (14081)	2123
Ithaca, NY (14850)	37136
Ithaca, NY (14853)	342
Lansing, NY (14882)	3354
Jamestown, NY (14701)	29436
Jasper, NY (14855)	725
Java Center, NY (14082)	442
Kendall, NY (14476)	1905
Kennedy, NY (14747)	1827
Kent, NY (14477)	1443
Branchport, NY (14418)	1028
Keuka Park, NY (14478)	820
Kill Buck, NY (14748)	603
Lake View, NY (14085)	6645
Lakeville, NY (14480)	786
Lakewood, NY (14750)	3950
Lancaster, NY (14086)	28598
Lawtons, NY (14091)	1071
Leicester, NY (14481)	1647
Le Roy, NY (14482)	7139
Lewiston, NY (14092)	9643
Lima, NY (14485)	3549
Limestone, NY (14753)	946
Lindley, NY (14858)	1319
Little Genesee, NY (14754)	512
Little Valley, NY (14755)	2136
Livonia, NY (14487)	5126
Lockport, NY (14094)	41705
Lockwood, NY (14859)	900
Lodi, NY (14860)	852
Lowman, NY (14861)	1167
Lyndonville, NY (14098)	2495
Lyons, NY (14489)	5559
Macedon, NY (14502)	9241
Machias, NY (14101)	1467
Manchester, NY (14504)	1417
Marilla, NY (14102)	1173
Marion, NY (14505)	4769
Mayville, NY (14757)	2590
Medina, NY (14103)	8683
Mendon, NY (14506)	1262
Middleport, NY (14105)	3850
Middlesex, NY (14507)	1189
Millport, NY (14864)	972
Montour Falls, NY (14865)	1974
Mount Morris, NY (14510)	3851
Naples, NY (14512)	4035
Newark, NY (14513)	11286
Burt, NY (14028)	1315
Newfane, NY (14108)	4926
Newfield, NY (14867)	4576
Niagara Falls, NY (14301)	8416
Niagara Falls, NY (14303)	3890
Niagara Falls, NY (14304)	25293
Niagara Falls, NY (14305)	12128
North Chili, NY (14514)	4933
North Collins, NY (14111)	2725
North Java, NY (14113)	724
North Rose, NY (14516)	1936
North Tonawanda, NY (14120)	38248
Nunda, NY (14517)	2352
Oakfield, NY (14125)	3241
Odessa, NY (14869)	1151
Olean, NY (14760)	14511
Ontario, NY (14519)	10651
Orchard Park, NY (14127)	27004
Ovid, NY (14521)	2158
Painted Post, NY (14870)	8080
Palmyra, NY (14522)	7892
Panama, NY (14767)	1415
Pavilion, NY (14525)	2349
Penfield, NY (14526)	18588
Penn Yan, NY (14527)	9984
Perry, NY (14530)	4485
Perrysburg, NY (14129)	1056
Phelps, NY (14532)	3841
Piffard, NY (14533)	1317
Pine City, NY (14871)	3990
Pine Valley, NY (14872)	506
Pittsford, NY (14534)	30109
Portageville, NY (14536)	552
Portland, NY (14769)	743
Portville, NY (14770)	2483
Prattsburgh, NY (14873)	1971
Randolph, NY (14772)	2991
Ransomville, NY (14131)	4606
Ripley, NY (14775)	2012
Rochester, NY (14603)	525
Rochester, NY (14604)	1054
Rochester, NY (14605)	6470
Rochester, NY (14606)	21877
Rochester, NY (14607)	9704
Rochester, NY (14608)	6785
Rochester, NY (14609)	31863
Rochester, NY (14610)	11955
Rochester, NY (14611)	10429
Rochester, NY (14612)	30282
Rochester, NY (14613)	8911
Rochester, NY (14615)	12569
Rochester, NY (14616)	24464
Rochester, NY (14617)	21894
Rochester, NY (14618)	18664
Rochester, NY (14619)	10647
Rochester, NY (14620)	15338
Rochester, NY (14621)	20021
Rochester, NY (14622)	10834
Rochester, NY (14623)	15370
Rochester, NY (14624)	33179
Rochester, NY (14625)	9516
Rochester, NY (14626)	26777
Rock Stream, NY (14878)	555
Romulus, NY (14541)	1933
Rush, NY (14543)	2968
Rushford, NY (14777)	571
Rushville, NY (14544)	1675
Salamanca, NY (14779)	5147
Sanborn, NY (14132)	5028
Savona, NY (14879)	1736
Scio, NY (14880)	1339
Scottsville, NY (14546)	4100
Sherman, NY (14781)	1727
Shortsville, NY (14548)	3340
Silver Creek, NY (14136)	4115
Silver Springs, NY (14550)	1369
Sinclairville, NY (14782)	1912
Sodus, NY (14551)	4479
Sodus Point, NY (14555)	904
South Dayton, NY (14138)	1571
South Wales, NY (14139)	2114
Spencer, NY (14883)	3271
Spencerport, NY (14559)	15998
Springville, NY (14141)	6474
Springwater, NY (14560)	1819
Stafford, NY (14143)	1196
Stanley, NY (14561)	2174
Stockton, NY (14784)	780
Strykersville, NY (14145)	1399
Tonawanda, NY (14150)	35414
Troupsburg, NY (14885)	641
Trumansburg, NY (14886)	5786
Van Etten, NY (14889)	1180
Varysburg, NY (14167)	1383
Victor, NY (14564)	12648
Walworth, NY (14568)	5452
Warsaw, NY (14569)	4857
Waterport, NY (14571)	1035
Watkins Glen, NY (14891)	3508
Waverly, NY (14892)	6498
Wayland, NY (14572)	4137
Webster, NY (14580)	45392
Wellsburg, NY (14894)	1160
Wellsville, NY (14895)	7288
West Falls, NY (14170)	2168
Westfield, NY (14787)	4181
West Henrietta, NY (14586)	7811
West Valley, NY (14171)	1801
Whitesville, NY (14897)	739
Williamson, NY (14589)	6424
Wilson, NY (14172)	2825
Wolcott, NY (14590)	4077
Woodhull, NY (14898)	1147
Wyoming, NY (14591)	1513
Youngstown, NY (14174)	5187
Aaronsburg, PA (16820)	867
Acme, PA (15610)	3265
Adamsburg, PA (15611)	461
Addison, PA (15411)	581
Adrian, PA (16210)	843
Albion, PA (16401)	3601
Alexandria, PA (16611)	2046
Aliquippa, PA (15001)	27848
Allison Park, PA (15101)	22275
Altoona, PA (16601)	25207
Altoona, PA (16602)	23325
Alum Bank, PA (15521)	1495
Ambridge, PA (15003)	9334
Amity, PA (15311)	1207
Apollo, PA (15613)	12154
Armagh, PA (15920)	872
Ashville, PA (16613)	1347
Atlantic, PA (16111)	961
Austin, PA (16720)	1137
Avella, PA (15312)	3128
Avonmore, PA (15618)	2262
Baden, PA (15005)	8526
Northern Cambria, PA (15714)	5096
Bear Lake, PA (16402)	642
Beaver, PA (15009)	13047
Beaver Falls, PA (15010)	22923
Bedford, PA (15522)	10108
Beech Creek, PA (16822)	1958
Bellefonte, PA (16823)	19473
Belle Vernon, PA (15012)	13790
Bellwood, PA (16617)	2311
Bentleyville, PA (15314)	2953
Berlin, PA (15530)	4344
Bessemer, PA (16112)	1367
Bethel Park, PA (15102)	27708
Blairsville, PA (15717)	8385
Boalsburg, PA (16827)	3952
Bolivar, PA (15923)	1396
Boswell, PA (15531)	3112
Boyers, PA (16020)	1039
Brackenridge, PA (15014)	2648
Braddock, PA (15104)	6149
Bradenville, PA (15620)	739
Bradford, PA (16701)	13447
Bradfordwoods, PA (15015)	1237
Breezewood, PA (15533)	1159
Bridgeville, PA (15017)	13426
Broad Top, PA (16621)	571
Brockport, PA (15823)	1310
Brockway, PA (15824)	4522
Brookville, PA (15825)	8168
Brownsville, PA (15417)	6084
Buena Vista, PA (15018)	798
Buffalo Mills, PA (15534)	713
Bulger, PA (15019)	1386
Burgettstown, PA (15021)	6125
Butler, PA (16001)	34251
Butler, PA (16002)	13895
Cabot, PA (16023)	3674
Cairnbrook, PA (15924)	862
California, PA (15419)	1479
Cambridge Springs, PA (16403)	4788
Canonsburg, PA (15317)	33096
Carmichaels, PA (15320)	4119
Carnegie, PA (15106)	15580
Carrolltown, PA (15722)	1907
Cecil, PA (15321)	1670
Centerville, PA (16404)	2570
Central City, PA (15926)	2266
Centre Hall, PA (16828)	3930
Champion, PA (15622)	1126
Charleroi, PA (15022)	8570
Cherry Tree, PA (15724)	1910
Cheswick, PA (15024)	7465
Chicora, PA (16025)	4891
Clairton, PA (15025)	13396
Clarence, PA (16829)	597
Clarendon, PA (16313)	1596
Claridge, PA (15623)	681
Clarion, PA (16214)	5416
Clarksburg, PA (15725)	1225
Clarks Mills, PA (16114)	540
Clarksville, PA (15322)	1633
Claysburg, PA (16625)	2928
Claysville, PA (15323)	3862
Clearfield, PA (16830)	10880
Clearville, PA (15535)	1808
Clinton, PA (15026)	3195
Clymer, PA (15728)	2988
Coal Center, PA (15423)	1525
Coalport, PA (16627)	1654
Cochranton, PA (16314)	4950
Columbus, PA (16405)	670
Colver, PA (15927)	987
Commodore, PA (15729)	1187
Confluence, PA (15424)	1889
Conneaut Lake, PA (16316)	4694
Conneautville, PA (16406)	2770
Connellsville, PA (15425)	15435
Conway, PA (15027)	1918
Cooperstown, PA (16317)	1425
Coraopolis, PA (15108)	33662
Corry, PA (16407)	8581
Corsica, PA (15829)	1115
Cowansville, PA (16218)	936
Cranesville, PA (16410)	1680
Creekside, PA (15732)	1434
Creighton, PA (15030)	872
Cresson, PA (16630)	3731
Cuddy, PA (15031)	475
Curwensville, PA (16833)	4315
Cyclone, PA (16726)	453
Daisytown, PA (15427)	922
Darlington, PA (16115)	2980
Davidsville, PA (15928)	1745
Dawson, PA (15428)	1501
Dayton, PA (16222)	2019
Delmont, PA (15626)	4563
Derry, PA (15627)	5635
Dilliner, PA (15327)	1098
Donegal, PA (15628)	492
Donora, PA (15033)	3756
Dravosburg, PA (15034)	1505
Du Bois, PA (15801)	16630
Duke Center, PA (16729)	667
Dunbar, PA (15431)	3794
Duncansville, PA (16635)	10059
Duquesne, PA (15110)	3560
Dysart, PA (16636)	675
East Brady, PA (16028)	1533
East Freedom, PA (16637)	2042
East Mc Keesport, PA (15035)	1807
East Millsboro, PA (15433)	599
East Pittsburgh, PA (15112)	2523
East Springfield, PA (16411)	1254
Ebensburg, PA (15931)	7336
Edinboro, PA (16412)	7672
Edinburg, PA (16116)	2411
Eighty Four, PA (15330)	4900
Eldred, PA (16731)	2396
Elizabeth, PA (15037)	9677
Ellwood City, PA (16117)	14648
Emlenton, PA (16373)	2821
Emporium, PA (15834)	3962
Enon Valley, PA (16120)	2005
Erie, PA (16501)	778
Erie, PA (16502)	11048
Erie, PA (16503)	9687
Erie, PA (16504)	12965
Erie, PA (16505)	15563
Erie, PA (16506)	21081
Erie, PA (16507)	6232
Erie, PA (16508)	13574
Erie, PA (16509)	23284
Erie, PA (16510)	21150
Erie, PA (16511)	9286
Evans City, PA (16033)	5421
Everett, PA (15537)	6610
Export, PA (15632)	8364
Fairchance, PA (15436)	2180
Fairhope, PA (15538)	613
Fairmount City, PA (16224)	958
Fairview, PA (16415)	7961
Fallentimber, PA (16639)	818
Falls Creek, PA (15840)	1691
Farmington, PA (15437)	2042
Farrell, PA (16121)	3587
Fayette City, PA (15438)	1905
Fenelton, PA (16034)	1736
Finleyville, PA (15332)	7209
Fishertown, PA (15539)	504
Flinton, PA (16640)	792
Fombell, PA (16123)	2023
Ford City, PA (16226)	7049
Franklin, PA (16323)	13449
Fredericktown, PA (15333)	1659
Fredonia, PA (16124)	1688
Freedom, PA (15042)	7463
Freeport, PA (16229)	4681
Frenchville, PA (16836)	944
Friedens, PA (15541)	3264
Gallitzin, PA (16641)	2222
Garrett, PA (15542)	1015
Georgetown, PA (15043)	1992
Gibsonia, PA (15044)	25135
Girard, PA (16417)	7289
Glassport, PA (15045)	3570
Glen Campbell, PA (15742)	779
Glenshaw, PA (15116)	13658
Crescent, PA (15046)	2311
Grampian, PA (16838)	1628
Grand Valley, PA (16420)	522
Grapeville, PA (15634)	513
Graysville, PA (15337)	654
Greensboro, PA (15338)	1360
Greensburg, PA (15601)	49297
Greenville, PA (16125)	14194
Grindstone, PA (15442)	1752
Grove City, PA (16127)	11684
Guys Mills, PA (16327)	2356
Hadley, PA (16130)	1726
Harborcreek, PA (16421)	2147
Harmony, PA (16037)	4098
Harrison City, PA (15636)	3578
Harrisville, PA (16038)	2839
Hartstown, PA (16131)	804
Harwick, PA (15049)	911
Hastings, PA (16646)	2154
Herminie, PA (15637)	1674
Hesston, PA (16647)	664
Hickory, PA (15340)	1335
Hiller, PA (15444)	475
Hilliards, PA (16040)	781
Holbrook, PA (15341)	668
Hollidaysburg, PA (16648)	13559
Hollsopple, PA (15935)	2372
Home, PA (15747)	1727
Homer City, PA (15748)	6055
Homestead, PA (15120)	15584
Hookstown, PA (15050)	2333
Hooversville, PA (15936)	1308
Hopewell, PA (16650)	1522
Hopwood, PA (15445)	2562
Houston, PA (15342)	4211
Houtzdale, PA (16651)	2781
Howard, PA (16841)	4357
Hunker, PA (15639)	1723
Huntingdon, PA (16652)	11322
Hyndman, PA (15545)	2333
Imler, PA (16655)	1368
Imperial, PA (15126)	6190
Indiana, PA (15701)	21441
Indian Head, PA (15446)	527
Indianola, PA (15051)	385
Industry, PA (15052)	3134
Irvona, PA (16656)	1051
Irwin, PA (15642)	41036
Jackson Center, PA (16133)	1440
James Creek, PA (16657)	1147
Jamestown, PA (16134)	3261
Jeannette, PA (15644)	15775
Jefferson, PA (15344)	1383
Johnsonburg, PA (15845)	2861
Johnstown, PA (15901)	2473
Johnstown, PA (15902)	9511
Johnstown, PA (15904)	12978
Johnstown, PA (15905)	18374
Johnstown, PA (15906)	8524
Johnstown, PA (15909)	4728
Julian, PA (16844)	2236
Kane, PA (16735)	5119
Karns City, PA (16041)	1650
Karthaus, PA (16845)	593
Kennerdell, PA (16374)	1523
Kersey, PA (15846)	2950
Kittanning, PA (16201)	14742
Knox, PA (16232)	3667
Lake City, PA (16423)	3595
Lake Lynn, PA (15451)	654
Latrobe, PA (15650)	22781
Laughlintown, PA (15655)	602
Lawrence, PA (15055)	1317
Leechburg, PA (15656)	8922
Leeper, PA (16233)	953
Leetsdale, PA (15056)	964
Lemont Furnace, PA (15456)	2078
Lewis Run, PA (16738)	1079
South Park, PA (15129)	9928
Ligonier, PA (15658)	7512
Lilly, PA (15938)	2149
Linesville, PA (16424)	3809
Loretto, PA (15940)	1494
Loyalhanna, PA (15661)	509
Lucinda, PA (16235)	1177
Luthersburg, PA (15848)	904
Lyndora, PA (16045)	989
Mc Clellandtown, PA (15458)	1920
Mc Donald, PA (15057)	11992
Mc Kean, PA (16426)	3419
Mckeesport, PA (15131)	7359
Mckeesport, PA (15132)	14701
Mckeesport, PA (15133)	5683
Mckeesport, PA (15135)	4498
Mc Kees Rocks, PA (15136)	18467
Madera, PA (16661)	783
Mahaffey, PA (15757)	1347
Manns Choice, PA (15550)	1426
Manor, PA (15665)	1403
Marianna, PA (15345)	1342
Marienville, PA (16239)	1345
Marion Center, PA (15759)	2203
Markleton, PA (15551)	658
Markleysburg, PA (15459)	1304
Mars, PA (16046)	11992
Cranberry Twp, PA (16066)	25181
Martinsburg, PA (16662)	4714
Adah, PA (15410)	594
Masontown, PA (15461)	3308
Mayport, PA (16240)	1268
Meadville, PA (16335)	21460
Mercer, PA (16137)	9933
Meyersdale, PA (15552)	4992
Midland, PA (15059)	3186
Millheim, PA (16854)	848
Mill Run, PA (15464)	1180
Mineral Point, PA (15942)	1868
Monaca, PA (15061)	11028
Monessen, PA (15062)	6129
Monongahela, PA (15063)	10026
Morrisdale, PA (16858)	2991
Moshannon, PA (16859)	431
Mount Jewett, PA (16740)	1034
Mount Morris, PA (15349)	1504
Mount Pleasant, PA (15666)	13112
Murrysville, PA (15668)	12760
Nanty Glo, PA (15943)	3096
Natrona Heights, PA (15065)	9811
New Alexandria, PA (15670)	3212
New Bethlehem, PA (16242)	3693
New Brighton, PA (15066)	10473
New Castle, PA (16101)	25595
New Castle, PA (16102)	4613
New Castle, PA (16105)	13571
New Derry, PA (15671)	680
New Eagle, PA (15067)	1929
New Enterprise, PA (16664)	1655
New Florence, PA (15944)	2735
New Freeport, PA (15352)	666
New Galilee, PA (16141)	1525
New Kensington, PA (15068)	33539
New Paris, PA (15554)	2109
New Salem, PA (15468)	1834
New Stanton, PA (15672)	2962
New Wilmington, PA (16142)	4598
Nicktown, PA (15762)	835
Normalville, PA (15469)	1752
North East, PA (16428)	10986
North Versailles, PA (15137)	8495
Oakdale, PA (15071)	8759
Oakmont, PA (15139)	5477
Ohiopyle, PA (15470)	630
Oil City, PA (16301)	13009
Olanta, PA (16863)	651
Osceola Mills, PA (16666)	2432
Osterburg, PA (16667)	1254
Parker, PA (16049)	2637
Patton, PA (16668)	2944
Penfield, PA (15849)	1195
Penn, PA (15675)	924
Penn Run, PA (15765)	1484
Pennsylvania Furnace, PA (16865)	1593
Perryopolis, PA (15473)	3425
Petersburg, PA (16669)	1835
Petrolia, PA (16050)	1201
Philipsburg, PA (16866)	6561
West Mifflin, PA (15122)	17458
Pitcairn, PA (15140)	2420
Monroeville, PA (15146)	25238
Pittsburgh, PA (15201)	9760
Pittsburgh, PA (15202)	16309
Pittsburgh, PA (15203)	6152
Pittsburgh, PA (15204)	6335
Pittsburgh, PA (15205)	18124
Pittsburgh, PA (15206)	20440
Pittsburgh, PA (15207)	8582
Pittsburgh, PA (15208)	7534
Pittsburgh, PA (15209)	11063
Pittsburgh, PA (15210)	19251
Pittsburgh, PA (15211)	8297
Pittsburgh, PA (15212)	20439
Pittsburgh, PA (15213)	8837
Pittsburgh, PA (15214)	10700
Pittsburgh, PA (15215)	10731
Pittsburgh, PA (15216)	19388
Pittsburgh, PA (15217)	20803
Pittsburgh, PA (15218)	11362
Pittsburgh, PA (15219)	7443
Pittsburgh, PA (15220)	15146
Pittsburgh, PA (15221)	24006
Pittsburgh, PA (15222)	2953
Pittsburgh, PA (15223)	6228
Pittsburgh, PA (15224)	7053
Pittsburgh, PA (15225)	969
Pittsburgh, PA (15226)	11640
Pittsburgh, PA (15227)	24667
Pittsburgh, PA (15228)	15814
Pittsburgh, PA (15229)	12508
Pittsburgh, PA (15232)	6837
Pittsburgh, PA (15233)	2094
Pittsburgh, PA (15234)	12505
Pittsburgh, PA (15235)	30387
Pittsburgh, PA (15236)	27107
Pittsburgh, PA (15237)	37268
Pittsburgh, PA (15238)	12416
Pittsburgh, PA (15239)	18952
Pittsburgh, PA (15241)	19209
Pittsburgh, PA (15243)	12455
Pittsfield, PA (16340)	1581
Pleasantville, PA (16341)	1811
Point Marion, PA (15474)	1641
Polk, PA (16342)	2077
Portage, PA (15946)	5949
Port Allegany, PA (16743)	3348
Portersville, PA (16051)	2845
Port Matilda, PA (16870)	6289
Presto, PA (15142)	1732
Prospect, PA (16052)	2250
Prosperity, PA (15329)	1563
Pulaski, PA (16143)	2400
Punxsutawney, PA (15767)	11583
Rebersburg, PA (16872)	1026
Renfrew, PA (16053)	3651
Reynoldsville, PA (15851)	5665
Rices Landing, PA (15357)	1350
Ridgway, PA (15853)	5800
Rillton, PA (15678)	543
Rimersburg, PA (16248)	2646
Rixford, PA (16745)	511
Roaring Spring, PA (16673)	4696
Robertsdale, PA (16674)	517
Robinson, PA (15949)	617
Rochester, PA (15074)	7751
Rochester Mills, PA (15771)	768
Rockton, PA (15856)	794
Rockwood, PA (15557)	3282
Rossiter, PA (15772)	1267
Roulette, PA (16746)	983
Ruffs Dale, PA (15679)	2896
Rural Valley, PA (16249)	1826
Russell, PA (16345)	3368
Russellton, PA (15076)	785
Saegertown, PA (16433)	4539
Saint Marys, PA (15857)	12039
Salisbury, PA (15558)	1511
Salix, PA (15952)	1260
Saltsburg, PA (15681)	4194
Sandy Lake, PA (16145)	2303
Sarver, PA (16055)	7563
Saxonburg, PA (16056)	4396
Saxton, PA (16678)	2219
Scenery Hill, PA (15360)	1680
Schellsburg, PA (15559)	1736
Scottdale, PA (15683)	7090
Cranberry, PA (16319)	1250
Seneca, PA (16346)	2737
Seward, PA (15954)	1828
Sewickley, PA (15143)	17301
Sharon, PA (16146)	10201
Hermitage, PA (16148)	15082
Sharpsville, PA (16150)	6622
Sheffield, PA (16347)	1881
Shelocta, PA (15774)	2747
Shinglehouse, PA (16748)	2418
Shippenville, PA (16254)	2773
Sidman, PA (15955)	1699
Sigel, PA (15860)	999
Six Mile Run, PA (16679)	649
Slickville, PA (15684)	641
Sligo, PA (16255)	1511
Slippery Rock, PA (16057)	8069
Slovan, PA (15078)	477
Smethport, PA (16749)	3388
Smicksburg, PA (16256)	1294
Smithfield, PA (15478)	5048
Smithton, PA (15479)	1811
Smock, PA (15480)	1568
Snow Shoe, PA (16874)	1099
Somerset, PA (15501)	13092
South Fork, PA (15956)	2395
Spartansburg, PA (16434)	2065
Spraggs, PA (15362)	597
Springboro, PA (16435)	1688
Spring Church, PA (15686)	815
Spring Creek, PA (16436)	589
Springdale, PA (15144)	3641
Spring Mills, PA (16875)	3258
Stahlstown, PA (15687)	1162
State College, PA (16801)	21293
University Park, PA (16802)	458
State College, PA (16803)	15132
Stoneboro, PA (16153)	2236
Stoystown, PA (15563)	2609
Strabane, PA (15363)	709
Strattanville, PA (16258)	1518
Sugar Grove, PA (16350)	2027
Summerhill, PA (15958)	1906
Summerville, PA (15864)	1615
Sutersville, PA (15083)	844
Sycamore, PA (15364)	622
Sykesville, PA (15865)	976
Tarentum, PA (15084)	8210
Tarrs, PA (15688)	612
Templeton, PA (16259)	1649
Tidioute, PA (16351)	1329
Tionesta, PA (16353)	2356
Titusville, PA (16354)	8829
Townville, PA (16360)	1137
Trafford, PA (15085)	7089
Transfer, PA (16154)	2363
Turtle Creek, PA (15145)	5751
Strongstown, PA (15957)	455
Tyrone, PA (16686)	11386
Union City, PA (16438)	6490
Uniontown, PA (15401)	24494
Utica, PA (16362)	925
Valencia, PA (16059)	7272
Vanderbilt, PA (15486)	2027
Vandergrift, PA (15690)	7442
Venango, PA (16440)	822
Venetia, PA (15367)	7932
Venus, PA (16364)	980
Verona, PA (15147)	14492
Vintondale, PA (15961)	853
Volant, PA (16156)	2800
Wampum, PA (16157)	3008
Warren, PA (16365)	15626
Warriors Mark, PA (16877)	1474
Washington, PA (15301)	40254
Waterford, PA (16441)	8824
Wattsburg, PA (16442)	2563
Waynesburg, PA (15370)	9752
Weedville, PA (15868)	1254
West Alexander, PA (15376)	1474
West Decatur, PA (16878)	1583
West Finley, PA (15377)	571
West Middlesex, PA (16159)	4294
Westmoreland City, PA (15692)	820
West Newton, PA (15089)	5488
Westover, PA (16692)	613
West Springfield, PA (16443)	1186
West Sunbury, PA (16061)	2420
Wexford, PA (15090)	19418
White, PA (15490)	568
Wilcox, PA (15870)	1150
Williamsburg, PA (16693)	3430
Wilmerding, PA (15148)	1898
Windber, PA (15963)	9388
Wind Ridge, PA (15380)	539
Woodbury, PA (16695)	829
Woodland, PA (16881)	1828
Worthington, PA (16262)	2481
Youngsville, PA (16371)	2652
Youngwood, PA (15697)	2610
Yukon, PA (15698)	662
Zelienople, PA (16063)	6228
Benwood, WV (26031)	1545
Bethany, WV (26032)	485
Cameron, WV (26033)	2388
Chester, WV (26034)	3931
Colliers, WV (26035)	2181
Follansbee, WV (26037)	5622
Glen Dale, WV (26038)	2657
Glen Easton, WV (26039)	828
Mcmechen, WV (26040)	1585
Moundsville, WV (26041)	12774
New Cumberland, WV (26047)	5024
Newell, WV (26050)	1261
Proctor, WV (26055)	1507
Triadelphia, WV (26059)	2728
Valley Grove, WV (26060)	1549
Weirton, WV (26062)	18324
Wellsburg, WV (26070)	7221
Wheeling, WV (26003)	34338
Abbottstown, PA (17301)	3702
Airville, PA (17302)	2518
Akron, PA (17501)	3973
Albrightsville, PA (18210)	6030
Alburtis, PA (18011)	5062
Allensville, PA (17002)	513
Allentown, PA (18101)	2150
Allentown, PA (18102)	36863
Allentown, PA (18103)	38997
Allentown, PA (18104)	36028
Allentown, PA (18106)	6412
Allentown, PA (18109)	13756
Allenwood, PA (17810)	1638
Andreas, PA (18211)	1221
Annville, PA (17003)	9333
Archbald, PA (18403)	6187
Ashland, PA (17921)	5064
Aspers, PA (17304)	2262
Athens, PA (18810)	4909
Auburn, PA (17922)	4204
Bainbridge, PA (17502)	2212
Bally, PA (19503)	1099
Bangor, PA (18013)	15081
Barnesville, PA (18214)	1939
Barto, PA (19504)	4491
Bartonsville, PA (18321)	1795
Bath, PA (18014)	10237
Beach Lake, PA (18405)	1980
Beaver Meadows, PA (18216)	1090
Beaver Springs, PA (17812)	1262
Beavertown, PA (17813)	1626
Bechtelsville, PA (19505)	3004
Belleville, PA (17004)	3683
Benton, PA (17814)	3821
Stillwater, PA (17878)	1355
Bernville, PA (19506)	6458
Berwick, PA (18603)	15678
Bethel, PA (19507)	2863
Bethlehem, PA (18015)	22650
Bethlehem, PA (18016)	423
Bethlehem, PA (18017)	32654
Bethlehem, PA (18018)	25707
Bethlehem, PA (18020)	18523
Biglerville, PA (17307)	4661
Bird In Hand, PA (17505)	1455
Birdsboro, PA (19508)	13937
Blain, PA (17006)	837
Blairs Mills, PA (17213)	503
Blakeslee, PA (18610)	3913
Blandon, PA (19510)	6753
Bloomsburg, PA (17815)	19934
Blossburg, PA (16912)	1516
Blue Ridge Summit, PA (17214)	1069
Boiling Springs, PA (17007)	5354
Boyertown, PA (19512)	15010
Brackney, PA (18812)	1429
Breinigsville, PA (18031)	6106
Brodheadsville, PA (18322)	2676
Brogue, PA (17309)	1809
Burnham, PA (17009)	1673
Bushkill, PA (18324)	8015
Tamiment, PA (18371)	560
Camp Hill, PA (17011)	28574
Canadensis, PA (18325)	2012
Canton, PA (17724)	3884
Carbondale, PA (18407)	11187
Carlisle, PA (17013)	27763
Carlisle, PA (17015)	19054
Catasauqua, PA (18032)	8120
Catawissa, PA (17820)	4897
Center Valley, PA (18034)	6617
Chambersburg, PA (17201)	24638
Chambersburg, PA (17202)	22756
Christiana, PA (17509)	3511
Clarks Summit, PA (18411)	19464
Coaldale, PA (18218)	1824
Cogan Station, PA (17728)	4701
Columbia, PA (17512)	15064
Columbia Cross Roads, PA (16914)	1910
Conestoga, PA (17516)	4159
Coopersburg, PA (18036)	11476
Coplay, PA (18037)	6486
Coudersport, PA (16915)	4741
Covington, PA (16917)	1200
Cresco, PA (18326)	3792
Cressona, PA (17929)	1411
Dallas, PA (18612)	12867
Dallastown, PA (17313)	9131
Dalmatia, PA (17017)	1547
Dalton, PA (18414)	4924
Damascus, PA (18415)	970
Danielsville, PA (18038)	2820
Danville, PA (17821)	15793
Dauphin, PA (17018)	4070
Delta, PA (17314)	4978
Denver, PA (17517)	13251
Dillsburg, PA (17019)	15958
Dingmans Ferry, PA (18328)	6833
Dornsife, PA (17823)	1074
Douglassville, PA (19518)	13057
Drumore, PA (17518)	976
Drums, PA (18222)	7789
Duncannon, PA (17020)	7807
Dushore, PA (18614)	2093
East Berlin, PA (17316)	7396
East Earl, PA (17519)	4783
East Greenville, PA (18041)	4993
Easton, PA (18040)	13958
Easton, PA (18042)	30988
Easton, PA (18045)	23750
East Petersburg, PA (17520)	4377
East Stroudsburg, PA (18301)	20252
East Stroudsburg, PA (18302)	12699
East Waterford, PA (17021)	861
Effort, PA (18330)	7179
Elizabethtown, PA (17022)	24660
Elizabethville, PA (17023)	2913
Elkland, PA (16920)	1521
Elliottsburg, PA (17024)	1648
Elverson, PA (19520)	5150
Elysburg, PA (17824)	3703
Emmaus, PA (18049)	16033
Enola, PA (17025)	14850
Ephrata, PA (17522)	26753
Equinunk, PA (18417)	890
Etters, PA (17319)	9562
Factoryville, PA (18419)	3759
Fairfield, PA (17320)	7137
Falls, PA (18615)	1738
Fannettsburg, PA (17221)	564
Fawn Grove, PA (17321)	2022
Fayetteville, PA (17222)	9448
Felton, PA (17322)	5414
Fleetwood, PA (19522)	13071
Fogelsville, PA (18051)	3264
Forest City, PA (18421)	4034
Pleasant Mount, PA (18453)	881
Forksville, PA (18616)	611
Fort Loudon, PA (17224)	1589
Frackville, PA (17931)	4272
Fredericksburg, PA (17026)	3214
Freeburg, PA (17827)	669
Freeland, PA (18224)	4903
Friendsville, PA (18818)	1089
Galeton, PA (16922)	1639
Gap, PA (17527)	5197
Gardners, PA (17324)	3924
Genesee, PA (16923)	1091
Germansville, PA (18053)	2117
Gettysburg, PA (17325)	21798
Gilbert, PA (18331)	751
Gilbertsville, PA (19525)	12010
Gillett, PA (16925)	2775
Girardville, PA (17935)	1285
Glen Lyon, PA (18617)	1419
Glen Rock, PA (17327)	6728
Glenville, PA (17329)	2514
Gordonville, PA (17529)	2967
Gouldsboro, PA (18424)	4633
Grantville, PA (17028)	3221
Granville Summit, PA (16926)	779
Gratz, PA (17030)	776
Great Bend, PA (18821)	961
Greeley, PA (18425)	934
Greencastle, PA (17225)	16582
Green Lane, PA (18054)	3949
Greentown, PA (18426)	3370
Halifax, PA (17032)	7247
Hallstead, PA (18822)	3006
Hamburg, PA (19526)	9799
Hamlin, PA (18427)	670
Hanover, PA (17331)	45273
Harrisburg, PA (17101)	1215
Harrisburg, PA (17102)	5246
Harrisburg, PA (17103)	9016
Harrisburg, PA (17104)	14435
Harrisburg, PA (17109)	20032
Harrisburg, PA (17110)	20981
Harrisburg, PA (17111)	26273
Harrisburg, PA (17112)	31324
Harrisburg, PA (17113)	9193
Harveys Lake, PA (18618)	3226
Hawley, PA (18428)	9695
Lakeville, PA (18438)	924
Hazleton, PA (18201)	21190
Hazleton, PA (18202)	9331
Hegins, PA (17938)	2277
Hellertown, PA (18055)	10340
Henryville, PA (18332)	2439
Hereford, PA (18056)	894
Herndon, PA (17830)	1739
Hershey, PA (17033)	13190
Highspire, PA (17034)	2155
Holtwood, PA (17532)	2932
Honesdale, PA (18431)	10706
Honey Grove, PA (17035)	681
Hop Bottom, PA (18824)	1154
Hughesville, PA (17737)	5359
Hummelstown, PA (17036)	20463
Hunlock Creek, PA (18621)	4390
Harrisonville, PA (17228)	1041
Hustontown, PA (17229)	1060
Ickesburg, PA (17037)	809
Jermyn, PA (18433)	5718
Jersey Shore, PA (17740)	10809
Jessup, PA (18434)	3514
Jim Thorpe, PA (18229)	7215
Jonestown, PA (17038)	7158
Kempton, PA (19529)	2697
Kingsley, PA (18826)	1444
Kinzers, PA (17535)	1957
Kirkwood, PA (17536)	2181
Klingerstown, PA (17941)	716
Knoxville, PA (16928)	1100
Kresgeville, PA (18333)	1051
Kulpmont, PA (17834)	2884
Kunkletown, PA (18058)	7286
Kutztown, PA (19530)	9192
Laceyville, PA (18623)	2240
Lackawaxen, PA (18435)	839
Lake Ariel, PA (18436)	10997
Lakewood, PA (18439)	433
Lancaster, PA (17601)	44773
Lancaster, PA (17602)	39757
Lancaster, PA (17603)	49093
Landisburg, PA (17040)	2260
Landisville, PA (17538)	5913
Lansford, PA (18232)	2869
Laurys Station, PA (18059)	1117
Lawrenceville, PA (16929)	1840
Lebanon, PA (17042)	31671
Lebanon, PA (17046)	24928
Leesport, PA (19533)	5672
Lehighton, PA (18235)	16083
Lemoyne, PA (17043)	5157
Lenhartsville, PA (19534)	1862
Leola, PA (17540)	8322
Le Raysville, PA (18829)	673
Lewisberry, PA (17339)	6334
Lewisburg, PA (17837)	12169
Lewistown, PA (17044)	16868
Liberty, PA (16930)	1089
Linden, PA (17744)	2679
Lititz, PA (17543)	37403
Little Meadows, PA (18830)	627
Littlestown, PA (17340)	9626
Liverpool, PA (17045)	2805
Lock Haven, PA (17745)	12059
Loganton, PA (17747)	2257
Long Pond, PA (18334)	2928
Loysville, PA (17047)	2050
Lykens, PA (17048)	2895
Mcadoo, PA (18237)	2684
Mc Alisterville, PA (17049)	2680
Mc Clure, PA (17841)	3650
Mc Connellsburg, PA (17233)	4467
Mc Sherrystown, PA (17344)	3074
Mc Veytown, PA (17051)	3613
Macungie, PA (18062)	21548
Mahanoy City, PA (17948)	3660
Mainesburg, PA (16932)	551
Manchester, PA (17345)	6656
Manheim, PA (17545)	18860
Mansfield, PA (16933)	4762
Mapleton Depot, PA (17052)	1395
Marietta, PA (17547)	6154
Marysville, PA (17053)	4585
Matamoras, PA (18336)	2910
Mechanicsburg, PA (17050)	29639
Mechanicsburg, PA (17055)	31415
Mehoopany, PA (18629)	1566
Mercersburg, PA (17236)	7396
Mertztown, PA (19539)	4176
Meshoppen, PA (18630)	2880
Middleburg, PA (17842)	6917
Middlebury Center, PA (16935)	1047
Middletown, PA (17057)	18622
Mifflin, PA (17058)	1462
Mifflinburg, PA (17844)	8338
Mifflintown, PA (17059)	6026
Milan, PA (18831)	1041
Milford, PA (18337)	12850
Mill Creek, PA (17060)	1046
Millersburg, PA (17061)	5854
Millerstown, PA (17062)	3470
Millersville, PA (17551)	6480
Millerton, PA (16936)	1846
Mill Hall, PA (17751)	5945
Millmont, PA (17845)	1790
Millville, PA (17846)	3179
Milroy, PA (17063)	2699
Milton, PA (17847)	9775
Minersville, PA (17954)	3667
Mohnton, PA (19540)	10892
Mohrsville, PA (19541)	3997
Monroeton, PA (18832)	1411
Mont Alto, PA (17237)	1359
Montgomery, PA (17752)	3973
Montoursville, PA (17754)	11190
Montrose, PA (18801)	7043
Morgantown, PA (19543)	4967
Morris, PA (16938)	606
Moscow, PA (18444)	11721
Mount Bethel, PA (18343)	3447
Mount Carmel, PA (17851)	5842
Mount Holly Springs, PA (17065)	3792
Mount Joy, PA (17552)	15530
Mount Pleasant Mills, PA (17853)	2567
Mount Pocono, PA (18344)	3029
Mount Union, PA (17066)	4009
Mountville, PA (17554)	6330
Mount Wolf, PA (17347)	5372
Muncy, PA (17756)	9759
Muncy Valley, PA (17758)	858
Myerstown, PA (17067)	12456
Nanticoke, PA (18634)	10886
Narvon, PA (17555)	5673
Nazareth, PA (18064)	21767
Big Cove Tannery, PA (17212)	538
Needmore, PA (17238)	1648
Nescopeck, PA (18635)	3379
Nesquehoning, PA (18240)	3121
New Albany, PA (18833)	1625
New Berlin, PA (17855)	974
New Bloomfield, PA (17068)	3577
Newburg, PA (17240)	2880
New Cumberland, PA (17070)	14615
Newfoundland, PA (18445)	1878
New Freedom, PA (17349)	7362
New Holland, PA (17557)	11650
Newmanstown, PA (17073)	4480
New Milford, PA (18834)	2905
New Oxford, PA (17350)	11002
New Park, PA (17352)	1176
New Philadelphia, PA (17959)	1178
Newport, PA (17074)	6280
New Providence, PA (17560)	4249
New Ringgold, PA (17960)	3493
New Tripoli, PA (18066)	5517
Newville, PA (17241)	10546
Nicholson, PA (18446)	3133
Northampton, PA (18067)	16693
Northumberland, PA (17857)	6690
Noxen, PA (18636)	1140
Nuremberg, PA (18241)	543
Oley, PA (19547)	4118
Olyphant, PA (18447)	8911
Orangeville, PA (17859)	2632
Orbisonia, PA (17243)	1058
Orefield, PA (18069)	7222
Orrstown, PA (17244)	1977
Orrtanna, PA (17353)	2711
Orwigsburg, PA (17961)	5985
Osceola, PA (16942)	689
Palm, PA (18070)	801
Palmerton, PA (18071)	8987
Palmyra, PA (17078)	18518
Paradise, PA (17562)	3421
Paupack, PA (18451)	427
Paxinos, PA (17860)	1910
Peach Bottom, PA (17563)	3089
Peckville, PA (18452)	4085
Pen Argyl, PA (18072)	6059
Pequea, PA (17565)	2316
Perkiomenville, PA (18074)	4576
Pine Grove, PA (17963)	8027
Pitman, PA (17964)	615
Pittston, PA (18640)	14000
Pittston, PA (18641)	5823
Duryea, PA (18642)	3677
Pittston, PA (18643)	10804
Wyoming, PA (18644)	6696
Plymouth, PA (18651)	7179
Pocono Lake, PA (18347)	2460
Pocono Pines, PA (18350)	1465
Pocono Summit, PA (18346)	2941
Port Carbon, PA (17965)	1811
Port Royal, PA (17082)	2754
Port Trevorton, PA (17864)	1809
Pottsville, PA (17901)	19275
Quarryville, PA (17566)	9799
Reading, PA (19601)	22537
Reading, PA (19602)	11848
Reading, PA (19604)	19119
Reading, PA (19605)	17437
Reading, PA (19606)	29985
Reading, PA (19607)	18907
Reading, PA (19608)	20753
Reading, PA (19609)	9113
Reading, PA (19610)	13613
Reading, PA (19611)	7420
Pennsburg, PA (18073)	7762
Red Hill, PA (18076)	2474
Red Lion, PA (17356)	19451
Reeders, PA (18352)	684
Reedsville, PA (17084)	3704
Reinholds, PA (17569)	5056
Renovo, PA (17764)	1727
Richfield, PA (17086)	1974
Richland, PA (17087)	2418
Riegelsville, PA (18077)	1938
Ringtown, PA (17967)	2146
Roaring Branch, PA (17765)	887
Robesonia, PA (19551)	4573
Rome, PA (18837)	2584
Ronks, PA (17572)	2894
Saint Clair, PA (17970)	2656
Saint Thomas, PA (17252)	3333
Saylorsburg, PA (18353)	10795
Sayre, PA (18840)	8644
Schnecksville, PA (18078)	6560
Schuylkill Haven, PA (17972)	9691
Sciota, PA (18354)	1105
Scotrun, PA (18355)	1255
Scranton, PA (18503)	330
Scranton, PA (18504)	16957
Scranton, PA (18505)	15444
Moosic, PA (18507)	4468
Scranton, PA (18508)	8652
Scranton, PA (18509)	9171
Scranton, PA (18510)	7607
Scranton, PA (18512)	10536
Taylor, PA (18517)	4395
Old Forge, PA (18518)	7135
Scranton, PA (18519)	4523
Selinsgrove, PA (17870)	10612
Seven Valleys, PA (17360)	4812
Shade Gap, PA (17255)	934
Coal Township, PA (17866)	6587
Shamokin, PA (17872)	7558
Shamokin Dam, PA (17876)	1381
Shenandoah, PA (17976)	4842
Shermans Dale, PA (17090)	4609
Shickshinny, PA (18655)	5212
Shippensburg, PA (17257)	19964
Shirleysburg, PA (17260)	976
Shoemakersville, PA (19555)	3223
Shohola, PA (18458)	2440
Shrewsbury, PA (17361)	4993
Slatington, PA (18080)	10196
Spring Grove, PA (17362)	12157
Spring Run, PA (17262)	856
Springville, PA (18844)	1520
Stevens, PA (17578)	5511
Stewartstown, PA (17363)	8466
Strasburg, PA (17579)	5307
Stroudsburg, PA (18360)	22854
Sugarloaf, PA (18249)	3506
Sugar Run, PA (18846)	663
Summit Hill, PA (18250)	2585
Sunbury, PA (17801)	13584
Susquehanna, PA (18847)	4417
Sweet Valley, PA (18656)	1890
Swiftwater, PA (18370)	982
Tafton, PA (18464)	1166
Tamaqua, PA (18252)	9269
Tannersville, PA (18372)	2615
Temple, PA (19560)	6965
Terre Hill, PA (17581)	1098
Thomasville, PA (17364)	3473
Thompson, PA (18465)	1099
Thompsontown, PA (17094)	1986
Three Springs, PA (17264)	1911
Tioga, PA (16946)	2152
Tobyhanna, PA (18466)	12134
Topton, PA (19562)	2093
Towanda, PA (18848)	7488
Tower City, PA (17980)	2920
Tremont, PA (17981)	2137
Trevorton, PA (17881)	1192
Trexlertown, PA (18087)	765
Trout Run, PA (17771)	2727
Troy, PA (16947)	3727
Tunkhannock, PA (18657)	9918
Turbotville, PA (17772)	2076
Ulster, PA (18850)	2092
Ulysses, PA (16948)	1295
Union Dale, PA (18470)	1852
Unityville, PA (17774)	966
Valley View, PA (17983)	1266
Walnut Bottom, PA (17266)	512
Walnutport, PA (18088)	7590
Wapwallopen, PA (18660)	3337
Warfordsburg, PA (17267)	2358
Warren Center, PA (18851)	614
Washington Boro, PA (17582)	1881
Watsontown, PA (17777)	5704
Waymart, PA (18472)	3522
Waynesboro, PA (17268)	23390
Weatherly, PA (18255)	3686
Wellsboro, PA (16901)	8404
Wellsville, PA (17365)	2344
Wernersville, PA (19565)	7511
Westfield, PA (16950)	2595
New Columbia, PA (17856)	2949
West Milton, PA (17886)	692
Whitehall, PA (18052)	23943
White Haven, PA (18661)	4681
Wilkes Barre, PA (18701)	890
Wilkes Barre, PA (18702)	29558
Kingston, PA (18704)	25974
Wilkes Barre, PA (18705)	12443
Wilkes Barre, PA (18706)	13116
Mountain Top, PA (18707)	14133
Shavertown, PA (18708)	8184
Luzerne, PA (18709)	2332
Williamsport, PA (17701)	32448
Williamsport, PA (17702)	9025
Williamstown, PA (17098)	2055
Willow Street, PA (17584)	8112
Wind Gap, PA (18091)	5275
Windsor, PA (17366)	4740
Winfield, PA (17889)	2531
Womelsdorf, PA (19567)	4584
Wrightsville, PA (17368)	6513
Wyalusing, PA (18853)	3633
Wysox, PA (18854)	1298
Yeagertown, PA (17099)	998
Dover, PA (17315)	22466
York, PA (17401)	12004
York, PA (17402)	29261
York, PA (17403)	30052
York, PA (17404)	31101
York, PA (17406)	19428
York, PA (17407)	1961
York, PA (17408)	19082
York Haven, PA (17370)	5191
York Springs, PA (17372)	3503
Zion Grove, PA (17985)	1067
Zionsville, PA (18092)	2807
Abington, PA (19001)	15006
Ambler, PA (19002)	28814
Ardmore, PA (19003)	10660
Atglen, PA (19310)	2510
Avondale, PA (19311)	8721
Bala Cynwyd, PA (19004)	9165
Bensalem, PA (19020)	47276
Croydon, PA (19021)	8630
Berwyn, PA (19312)	10749
Blue Bell, PA (19422)	17420
Bristol, PA (19007)	17778
Broomall, PA (19008)	18432
Bryn Mawr, PA (19010)	15730
Carversville, PA (18913)	421
Chadds Ford, PA (19317)	9306
Chalfont, PA (18914)	18039
Cheltenham, PA (19012)	5933
Chester, PA (19013)	21559
Aston, PA (19014)	18502
Brookhaven, PA (19015)	13552
Crum Lynne, PA (19022)	2710
Chester Springs, PA (19425)	12009
Clifton Heights, PA (19018)	19766
Coatesville, PA (19320)	41003
Cochranville, PA (19330)	4769
Collegeville, PA (19426)	31088
Schwenksville, PA (19473)	12592
Colmar, PA (18915)	1256
Conshohocken, PA (19428)	14701
Darby, PA (19023)	16055
Devon, PA (19333)	6268
Downingtown, PA (19335)	42233
Thorndale, PA (19372)	2186
Doylestown, PA (18901)	25185
Doylestown, PA (18902)	16495
Drexel Hill, PA (19026)	26723
Dublin, PA (18917)	1831
Elkins Park, PA (19027)	16454
Erwinna, PA (18920)	612
Essington, PA (19029)	3453
Exton, PA (19341)	15505
Fairless Hills, PA (19030)	11015
Flourtown, PA (19031)	4002
Folcroft, PA (19032)	5451
Folsom, PA (19033)	6874
Dresher, PA (19025)	5352
Fort Washington, PA (19034)	6067
Fountainville, PA (18923)	993
Frederick, PA (19435)	494
Furlong, PA (18925)	4806
Gladwyne, PA (19035)	3761
Glen Mills, PA (19342)	14826
Glenmoore, PA (19343)	7118
Glenolden, PA (19036)	10991
Glenside, PA (19038)	26925
Harleysville, PA (19438)	20584
Hatboro, PA (19040)	18843
Hatfield, PA (19440)	16392
Haverford, PA (19041)	4830
Holmes, PA (19043)	2430
Honey Brook, PA (19344)	9962
Horsham, PA (19044)	14168
Huntingdon Valley, PA (19006)	19754
Jamison, PA (18929)	8215
Jenkintown, PA (19046)	17162
Kennett Square, PA (19348)	19704
Kintnersville, PA (18930)	2220
Lafayette Hill, PA (19444)	9558
Landenberg, PA (19350)	10195
Langhorne, PA (19047)	30760
Feasterville Trevose, PA (19053)	24238
Lansdale, PA (19446)	47793
Lansdowne, PA (19050)	23056
Levittown, PA (19054)	15140
Levittown, PA (19055)	11766
Levittown, PA (19056)	13810
Levittown, PA (19057)	14645
Lincoln University, PA (19352)	7310
Line Lexington, PA (18932)	502
Malvern, PA (19355)	21947
Marcus Hook, PA (19061)	26101
Media, PA (19063)	31040
Springfield, PA (19064)	22318
Wallingford, PA (19086)	10584
Merion Station, PA (19066)	5008
Morrisville, PA (19067)	47005
Morton, PA (19070)	6334
Narberth, PA (19072)	8771
New Hope, PA (18938)	11903
Newtown, PA (18940)	27529
Newtown Square, PA (19073)	16449
Norristown, PA (19401)	29398
Norristown, PA (19403)	37609
Bridgeport, PA (19405)	4150
King Of Prussia, PA (19406)	20085
Gwynedd, PA (19436)	619
North Wales, PA (19454)	24159
Norwood, PA (19074)	5208
Nottingham, PA (19362)	4788
Oreland, PA (19075)	6573
Ottsville, PA (18942)	2561
Oxford, PA (19363)	13753
Paoli, PA (19301)	6346
Parkesburg, PA (19365)	6118
Perkasie, PA (18944)	20771
Philadelphia, PA (19102)	3209
Philadelphia, PA (19103)	15861
Philadelphia, PA (19104)	19073
Philadelphia, PA (19106)	7869
Philadelphia, PA (19107)	7363
Philadelphia, PA (19111)	46925
Philadelphia, PA (19114)	25060
Philadelphia, PA (19115)	26806
Philadelphia, PA (19116)	25751
Philadelphia, PA (19118)	7573
Philadelphia, PA (19119)	20484
Philadelphia, PA (19120)	47539
Philadelphia, PA (19121)	17926
Philadelphia, PA (19122)	9856
Philadelphia, PA (19123)	7858
Philadelphia, PA (19124)	43982
Philadelphia, PA (19125)	14595
Philadelphia, PA (19126)	11493
Philadelphia, PA (19127)	3454
Philadelphia, PA (19128)	27042
Philadelphia, PA (19129)	7175
Philadelphia, PA (19130)	16367
Philadelphia, PA (19131)	26989
Philadelphia, PA (19132)	22486
Philadelphia, PA (19133)	15096
Philadelphia, PA (19134)	35741
Philadelphia, PA (19135)	22906
Philadelphia, PA (19136)	25639
Philadelphia, PA (19137)	6308
Philadelphia, PA (19138)	22980
Philadelphia, PA (19139)	25515
Philadelphia, PA (19140)	33045
Philadelphia, PA (19141)	20468
Philadelphia, PA (19142)	20396
Philadelphia, PA (19143)	42781
Philadelphia, PA (19144)	27115
Philadelphia, PA (19145)	32550
Philadelphia, PA (19146)	22933
Philadelphia, PA (19147)	24646
Philadelphia, PA (19148)	33956
Philadelphia, PA (19149)	39353
Philadelphia, PA (19150)	18750
Philadelphia, PA (19151)	22320
Philadelphia, PA (19152)	25121
Philadelphia, PA (19153)	8801
Philadelphia, PA (19154)	28207
Mont Clare, PA (19453)	1165
Phoenixville, PA (19460)	32622
Pipersville, PA (18947)	5133
Plymouth Meeting, PA (19462)	13262
Pottstown, PA (19464)	39012
Pottstown, PA (19465)	14626
Prospect Park, PA (19076)	5397
Quakertown, PA (18951)	29756
Richlandtown, PA (18955)	1308
Ridley Park, PA (19078)	9956
Royersford, PA (19468)	22357
Sellersville, PA (18960)	11241
Sharon Hill, PA (19079)	7196
Souderton, PA (18964)	12365
Richboro, PA (18954)	9580
Southampton, PA (18966)	36515
Spring City, PA (19475)	8983
Swarthmore, PA (19081)	8194
Telford, PA (18969)	13427
Thornton, PA (19373)	2474
Toughkenamon, PA (19374)	1551
Upper Black Eddy, PA (18972)	2643
Upper Darby, PA (19082)	30828
Havertown, PA (19083)	32532
Villanova, PA (19085)	5346
Warminster, PA (18974)	37329
Warrington, PA (18976)	18088
Washington Crossing, PA (18977)	4027
Wayne, PA (19087)	27128
West Chester, PA (19380)	43281
West Chester, PA (19382)	41450
West Grove, PA (19390)	12100
Willow Grove, PA (19090)	16854
Woodlyn, PA (19094)	3711
Wyncote, PA (19095)	5124
Wynnewood, PA (19096)	12684
Zieglerville, PA (19492)	536
Bristol, TN (37620)	29934
Abingdon, VA (24210)	11650
Abingdon, VA (24211)	7605
Altavista, VA (24517)	4383
Alton, VA (24520)	1808
Amherst, VA (24521)	8008
Appalachia, VA (24216)	1796
Appomattox, VA (24522)	7853
Ararat, VA (24053)	1837
Atkins, VA (24311)	1633
Austinville, VA (24312)	1722
Axton, VA (24054)	5085
Bandy, VA (24602)	544
Barren Springs, VA (24313)	725
Bassett, VA (24055)	9807
Bastian, VA (24314)	1149
Bedford, VA (24523)	15102
Bent Mountain, VA (24059)	877
Big Island, VA (24526)	1229
Big Rock, VA (24603)	851
Big Stone Gap, VA (24219)	6989
Birchleaf, VA (24220)	557
Blacksburg, VA (24060)	24471
Blackwater, VA (24221)	578
Blairs, VA (24527)	2606
Bland, VA (24315)	2512
Bluefield, VA (24605)	6964
Blue Ridge, VA (24064)	4356
Boones Mill, VA (24065)	5204
Bristol, VA (24201)	11729
Bristol, VA (24202)	10332
Brookneal, VA (24528)	2724
Buchanan, VA (24066)	4049
Buffalo Junction, VA (24529)	1294
Callands, VA (24530)	892
Callaway, VA (24067)	1793
Cana, VA (24317)	2664
Cascade, VA (24069)	1504
Castlewood, VA (24224)	4093
Catawba, VA (24070)	1252
Cedar Bluff, VA (24609)	5374
Ceres, VA (24318)	470
Chatham, VA (24531)	6602
Check, VA (24072)	1043
Chilhowie, VA (24319)	5886
Christiansburg, VA (24073)	23032
Claudville, VA (24076)	851
Cleveland, VA (24225)	1219
Clinchco, VA (24226)	990
Clintwood, VA (24228)	4986
Clover, VA (24534)	1349
Cloverdale, VA (24077)	1012
Coeburn, VA (24230)	6249
Collinsville, VA (24078)	5743
Concord, VA (24538)	3769
Copper Hill, VA (24079)	1312
Crockett, VA (24323)	557
Daleville, VA (24083)	3045
Damascus, VA (24236)	2275
Dante, VA (24237)	760
Danville, VA (24540)	24307
Danville, VA (24541)	21053
Draper, VA (24324)	1772
Dryden, VA (24243)	1679
Dry Fork, VA (24549)	3454
Dublin, VA (24084)	8512
Duffield, VA (24244)	3735
Dugspur, VA (24325)	719
Dungannon, VA (24245)	723
Eagle Rock, VA (24085)	1648
Elk Creek, VA (24326)	923
Elliston, VA (24087)	3135
Evington, VA (24550)	5681
Ewing, VA (24248)	1789
Falls Mills, VA (24613)	775
Fancy Gap, VA (24328)	1399
Ferrum, VA (24088)	3066
Fieldale, VA (24089)	2270
Fincastle, VA (24090)	3739
Floyd, VA (24091)	5888
Forest, VA (24551)	18223
Fort Blackmore, VA (24250)	893
Fries, VA (24330)	2514
Galax, VA (24333)	13435
Gate City, VA (24251)	6976
Weber City, VA (24290)	1240
Glade Hill, VA (24092)	2342
Glade Spring, VA (24340)	4226
Gladstone, VA (24553)	1456
Gladys, VA (24554)	2996
Glasgow, VA (24555)	1729
Goode, VA (24556)	2682
Goodview, VA (24095)	3782
Gretna, VA (24557)	6054
Grundy, VA (24614)	5016
Halifax, VA (24558)	5366
Hardy, VA (24101)	5266
Haysi, VA (24256)	2178
Henry, VA (24102)	1200
Hillsville, VA (24343)	7047
Hiltons, VA (24258)	1141
Hiwassee, VA (24347)	1419
Honaker, VA (24260)	3876
Huddleston, VA (24104)	2775
Hurley, VA (24620)	1606
Hurt, VA (24563)	4384
Independence, VA (24348)	2966
Ivanhoe, VA (24350)	927
Java, VA (24565)	805
Jewell Ridge, VA (24622)	711
Jonesville, VA (24263)	4388
Keeling, VA (24566)	1153
Keokee, VA (24265)	569
Lambsburg, VA (24351)	493
Laurel Fork, VA (24352)	766
Lebanon, VA (24266)	7466
Long Island, VA (24569)	782
Lynchburg, VA (24501)	17907
Lynchburg, VA (24502)	28461
Lynchburg, VA (24503)	16263
Lynchburg, VA (24504)	6383
Lynch Station, VA (24571)	1596
Madison Heights, VA (24572)	13272
Marion, VA (24354)	11186
Martinsville, VA (24112)	23602
Max Meadows, VA (24360)	4753
Meadows Of Dan, VA (24120)	1329
Meadowview, VA (24361)	3723
Moneta, VA (24121)	8667
Monroe, VA (24574)	3232
Montvale, VA (24122)	1551
Mouth Of Wilson, VA (24363)	1033
Narrows, VA (24124)	3350
Nathalie, VA (24577)	3700
Natural Bridge, VA (24578)	841
Natural Bridge Station, VA (24579)	1167
Nelson, VA (24580)	465
New Castle, VA (24127)	3328
Newport, VA (24128)	1597
Nickelsville, VA (24271)	1984
North Tazewell, VA (24630)	5267
Norton, VA (24273)	4436
Oakwood, VA (24631)	968
Patrick Springs, VA (24133)	2130
Pearisburg, VA (24134)	4485
Pembroke, VA (24136)	2729
Penhook, VA (24137)	2069
Pennington Gap, VA (24277)	3561
Pilot, VA (24138)	1240
Pound, VA (24279)	3351
Pounding Mill, VA (24637)	2833
Pulaski, VA (24301)	10431
Radford, VA (24141)	12623
Raven, VA (24639)	2190
Rich Creek, VA (24147)	795
Richlands, VA (24641)	4134
Ridgeway, VA (24148)	6323
Riner, VA (24149)	2989
Ringgold, VA (24586)	4455
Ripplemead, VA (24150)	557
Roanoke, VA (24012)	22512
Roanoke, VA (24013)	5397
Roanoke, VA (24014)	13817
Roanoke, VA (24015)	12643
Roanoke, VA (24016)	5155
Roanoke, VA (24017)	17194
Roanoke, VA (24018)	33211
Roanoke, VA (24019)	23373
Rocky Gap, VA (24366)	791
Rocky Mount, VA (24151)	15043
Rosedale, VA (24280)	979
Rose Hill, VA (24281)	1597
Rowe, VA (24646)	521
Rural Retreat, VA (24368)	4076
Rustburg, VA (24588)	7795
Saint Paul, VA (24283)	2145
Salem, VA (24153)	30271
Saltville, VA (24370)	4748
Scottsburg, VA (24589)	1643
Scottsville, VA (24590)	6149
Shawsville, VA (24162)	1910
South Boston, VA (24592)	10130
Speedwell, VA (24374)	592
Spencer, VA (24165)	1479
Spout Spring, VA (24593)	1358
Stanleytown, VA (24168)	868
Stuart, VA (24171)	6082
Sugar Grove, VA (24375)	1226
Sutherlin, VA (24594)	1355
Swords Creek, VA (24649)	1567
Tazewell, VA (24651)	4369
Thaxton, VA (24174)	1987
Troutdale, VA (24378)	853
Troutville, VA (24175)	7123
Union Hall, VA (24176)	1115
Vansant, VA (24656)	2558
Vernon Hill, VA (24597)	937
Vinton, VA (24179)	15844
Virgilina, VA (24598)	1401
Willis, VA (24380)	2039
Wingina, VA (24599)	437
Wirtz, VA (24184)	3827
Wise, VA (24293)	7758
Woodlawn, VA (24381)	3044
Woolwine, VA (24185)	803
Wytheville, VA (24382)	11285
Alderson, WV (24910)	2759
Alkol, WV (25501)	819
Alma, WV (26320)	614
Alum Creek, WV (25003)	2063
Amherstdale, WV (25607)	641
Ansted, WV (25812)	1318
Apple Grove, WV (25502)	800
Arnoldsburg, WV (25234)	723
Ashton, WV (25503)	581
Athens, WV (24712)	1602
Augusta, WV (26704)	3953
Aurora, WV (26705)	880
Baisden, WV (25608)	521
Baker, WV (26801)	933
Ballard, WV (24918)	1083
Barboursville, WV (25504)	9894
Beaver, WV (25813)	4160
Beckley, WV (25801)	21630
Belington, WV (26250)	3795
Belle, WV (25015)	3515
Belleville, WV (26133)	1159
Belmont, WV (26134)	770
Berkeley Springs, WV (25411)	10129
Beverly, WV (26253)	2512
Big Springs, WV (26137)	558
Birch River, WV (26610)	795
Blacksville, WV (26521)	463
Bloomery, WV (26817)	504
Bluefield, WV (24701)	15203
Bolt, WV (25817)	520
Branchland, WV (25506)	2987
Brandywine, WV (26802)	891
Brenton, WV (24818)	822
Bridgeport, WV (26330)	12642
Bruceton Mills, WV (26525)	4111
Buckhannon, WV (26201)	14223
Buffalo, WV (25033)	1817
Bunker Hill, WV (25413)	6154
Burlington, WV (26710)	1644
Burnsville, WV (26335)	918
Burton, WV (26562)	532
Cabin Creek, WV (25035)	999
Cabins, WV (26855)	590
Cairo, WV (26337)	923
Caldwell, WV (24925)	897
Camden, WV (26338)	517
Camden On Gauley, WV (26208)	611
Canvas, WV (26662)	858
Capon Bridge, WV (26711)	2192
Cedar Grove, WV (25039)	890
Chapmanville, WV (25508)	6341
Charleston, WV (25301)	1800
Charleston, WV (25302)	11961
Charleston, WV (25303)	6275
Charleston, WV (25304)	6483
Charleston, WV (25306)	5065
Charleston, WV (25309)	9969
Charleston, WV (25311)	7427
Charleston, WV (25312)	11193
Charleston, WV (25313)	10597
Charleston, WV (25314)	13109
Charleston, WV (25315)	2406
Charleston, WV (25320)	4294
Charles Town, WV (25414)	13677
Charmco, WV (25958)	516
Chloe, WV (25235)	689
Circleville, WV (26804)	488
Clarksburg, WV (26301)	21971
Clay, WV (25043)	1340
Clendenin, WV (25045)	4358
Coal City, WV (25823)	1669
Coalton, WV (26257)	617
Comfort, WV (25049)	597
Cool Ridge, WV (25825)	1776
Cottageville, WV (25239)	1348
Cowen, WV (26206)	1906
Crab Orchard, WV (25827)	2554
Craigsville, WV (26205)	2714
Crawley, WV (24931)	1193
Crum, WV (25669)	835
Culloden, WV (25510)	4003
Cyclone, WV (24827)	881
Danese, WV (25831)	909
Daniels, WV (25832)	3336
Danville, WV (25053)	3229
Davin, WV (25617)	667
Davis, WV (26260)	1003
Davisville, WV (26142)	2160
Delbarton, WV (25670)	3179
Dingess, WV (25671)	848
Dixie, WV (25059)	507
Duck, WV (25063)	1010
Dunbar, WV (25064)	7497
Dunlow, WV (25511)	649
Durbin, WV (26264)	478
East Bank, WV (25067)	899
East Lynn, WV (25512)	809
Eglon, WV (26716)	574
Elizabeth, WV (26143)	3442
Elk Garden, WV (26717)	896
Elkins, WV (26241)	11523
Elkview, WV (25071)	8712
Ellenboro, WV (26346)	791
Enterprise, WV (26568)	555
Eskdale, WV (25075)	499
Evans, WV (25241)	1355
Fairdale, WV (25839)	1034
Fairmont, WV (26554)	30980
Fairview, WV (26570)	2592
Falling Waters, WV (25419)	7866
Farmington, WV (26571)	1625
Fayetteville, WV (25840)	6065
Fenwick, WV (26202)	500
Fisher, WV (26818)	557
Flatwoods, WV (26621)	601
Flemington, WV (26347)	1506
Fort Ashby, WV (26719)	2421
Fort Gay, WV (25514)	2774
Foster, WV (25081)	886
Frametown, WV (26623)	1040
Frankford, WV (24938)	1231
Franklin, WV (26807)	2493
Fraziers Bottom, WV (25082)	1438
French Creek, WV (26218)	1907
Friendly, WV (26146)	960
Gallipolis Ferry, WV (25515)	1651
Gandeeville, WV (25243)	762
Gap Mills, WV (24941)	766
Gassaway, WV (26624)	2151
Gauley Bridge, WV (25085)	813
Gay, WV (25244)	589
Genoa, WV (25517)	1117
Gerrardstown, WV (25420)	3295
Ghent, WV (25843)	674
Gilbert, WV (25621)	2049
Given, WV (25245)	763
Glen Daniel, WV (25844)	1144
Glen Jean, WV (25846)	491
Glenville, WV (26351)	2085
Glenwood, WV (25520)	1063
Grafton, WV (26354)	8122
Grantsville, WV (26147)	1513
Great Cacapon, WV (25422)	1116
Green Bank, WV (24944)	454
Griffithsville, WV (25521)	739
Hambleton, WV (26269)	828
Hamlin, WV (25523)	2053
Hanover, WV (24839)	712
Harman, WV (26270)	643
Harpers Ferry, WV (25425)	10035
Harrisville, WV (26362)	2416
Harts, WV (25524)	2660
Hedgesville, WV (25427)	11492
Henderson, WV (25106)	501
Hernshaw, WV (25107)	483
Hewett, WV (25108)	561
Hico, WV (25854)	821
High View, WV (26808)	721
Hillsboro, WV (24946)	910
Hinton, WV (25951)	4005
Holden, WV (25625)	998
Horner, WV (26372)	590
Hundred, WV (26575)	656
Huntington, WV (25701)	15809
Huntington, WV (25702)	5103
Huntington, WV (25703)	2122
Huntington, WV (25704)	11496
Huntington, WV (25705)	15882
Hurricane, WV (25526)	18123
Huttonsville, WV (26273)	667
Iaeger, WV (24844)	1249
Inwood, WV (25428)	8680
Ivydale, WV (25113)	596
Jacksonburg, WV (26377)	477
Jane Lew, WV (26378)	3572
Jolo, WV (24850)	530
Julian, WV (25529)	640
Jumping Branch, WV (25969)	848
Kearneysville, WV (25430)	6639
Kenna, WV (25248)	2512
Kenova, WV (25530)	4601
Kermit, WV (25674)	1835
Keyser, WV (26726)	10474
Albright, WV (26519)	1311
Kingwood, WV (26537)	4577
Lake, WV (25121)	516
Lashmeet, WV (24733)	762
Lavalette, WV (25535)	2132
Lenore, WV (25676)	1151
Leon, WV (25123)	2338
Lerona, WV (25971)	820
Le Roy, WV (25252)	836
Lesage, WV (25537)	1827
Lester, WV (25865)	916
Letart, WV (25253)	1566
Lewisburg, WV (24901)	7139
Liberty, WV (25124)	1024
Lindside, WV (24951)	1144
Littleton, WV (26581)	760
Lizemores, WV (25125)	630
Logan, WV (25601)	3739
Looneyville, WV (25259)	547
Lost Creek, WV (26385)	3115
Lumberport, WV (26386)	1923
Madison, WV (25130)	2796
Maidsville, WV (26541)	2091
Man, WV (25635)	1347
Mannington, WV (26582)	3896
Marlinton, WV (24954)	2579
Martinsburg, WV (25401)	10936
Martinsburg, WV (25403)	9792
Martinsburg, WV (25404)	14198
Martinsburg, WV (25405)	8929
Mason, WV (25260)	1329
Masontown, WV (26542)	1818
Matewan, WV (25678)	1139
Mathias, WV (26812)	1314
Matoaka, WV (24736)	610
Maysel, WV (25133)	531
Maysville, WV (26833)	1715
Meadow Bridge, WV (25976)	1545
Middlebourne, WV (26149)	1992
Mill Creek, WV (26280)	1466
Millwood, WV (25262)	789
Milton, WV (25541)	7505
Mineral Wells, WV (26150)	5176
Moatsville, WV (26405)	956
Montgomery, WV (25136)	1110
Montrose, WV (26283)	1272
Moorefield, WV (26836)	5149
Morgantown, WV (26501)	13220
Morgantown, WV (26505)	16568
Morgantown, WV (26508)	22694
Mount Clare, WV (26408)	2425
Mount Hope, WV (25880)	3947
Mount Lookout, WV (26678)	952
Mount Nebo, WV (26679)	1518
Mount Storm, WV (26739)	676
Mullens, WV (25882)	1537
Naoma, WV (25140)	599
Ashford, WV (25009)	744
Nettie, WV (26681)	1274
Independence, WV (26374)	1129
Newburg, WV (26410)	818
New Creek, WV (26743)	1401
New Martinsville, WV (26155)	7052
New Milton, WV (26411)	494
Newton, WV (25266)	562
Nimitz, WV (25978)	507
Nitro, WV (25143)	7120
Normantown, WV (25267)	573
Northfork, WV (24868)	934
Oak Hill, WV (25901)	7952
Oceana, WV (24870)	2676
Old Fields, WV (26845)	724
Omar, WV (25638)	777
Ona, WV (25545)	3898
Paden City, WV (26159)	2162
Palestine, WV (26160)	682
Panther, WV (24872)	518
Parkersburg, WV (26101)	21506
Parkersburg, WV (26104)	13319
Vienna, WV (26105)	10329
Parsons, WV (26287)	2533
Paw Paw, WV (25434)	1558
Pecks Mill, WV (25547)	920
Pennsboro, WV (26415)	2505
Petersburg, WV (26847)	5316
Peterstown, WV (24963)	2929
Peytona, WV (25154)	632
Philippi, WV (26416)	5257
Piedmont, WV (26750)	635
Pine Grove, WV (26419)	920
Pineville, WV (24874)	2495
Pipestem, WV (25979)	651
Poca, WV (25159)	4429
Point Pleasant, WV (25550)	6736
Prichard, WV (25555)	1606
Princeton, WV (24740)	22090
Procious, WV (25164)	835
Purgitsville, WV (26852)	669
Quinwood, WV (25981)	631
Racine, WV (25165)	479
Rainelle, WV (25962)	2574
Ranger, WV (25557)	971
Ranson, WV (25438)	5046
Ravenswood, WV (26164)	6261
Reader, WV (26167)	724
Red House, WV (25168)	2170
Reedsville, WV (26547)	2033
Reedy, WV (25270)	691
Renick, WV (24966)	1024
Richwood, WV (26261)	1725
Ridgeley, WV (26753)	5251
Rio, WV (26755)	557
Ripley, WV (25271)	7112
Rivesville, WV (26588)	2437
Rock, WV (24747)	1645
Rock Cave, WV (26234)	889
Rockport, WV (26169)	701
Romney, WV (26757)	4677
Ronceverte, WV (24970)	3283
Rowlesburg, WV (26425)	856
Rupert, WV (25984)	1341
Saint Albans, WV (25177)	19627
Saint Marys, WV (26170)	4566
Salem, WV (26426)	5185
Salt Rock, WV (25559)	1734
Sandyville, WV (25275)	1825
Scarbro, WV (25917)	1430
Scott Depot, WV (25560)	7601
Seth, WV (25181)	1152
Shady Spring, WV (25918)	3144
Shenandoah Junction, WV (25442)	1602
Shepherdstown, WV (25443)	5438
Shinnston, WV (26431)	4616
Sinks Grove, WV (24976)	829
Sistersville, WV (26175)	2371
Slanesville, WV (25444)	712
Smithville, WV (26178)	487
Sod, WV (25564)	1018
Southside, WV (25187)	509
Spencer, WV (25276)	5558
Springfield, WV (26763)	1119
Spurlockville, WV (25565)	491
Sugar Grove, WV (26815)	772
Sumerco, WV (25567)	592
Summersville, WV (26651)	6954
Summit Point, WV (25446)	1147
Sutton, WV (26601)	3056
Talcott, WV (24981)	594
Terra Alta, WV (26764)	3164
Thomas, WV (26292)	604
Thornton, WV (26440)	895
Tornado, WV (25202)	1205
Tunnelton, WV (26444)	2460
Union, WV (24983)	1883
Upper Tract, WV (26866)	725
Valley Bend, WV (26293)	563
Valley Head, WV (26294)	541
Victor, WV (25938)	989
Volga, WV (26238)	698
Walker, WV (26180)	1790
Walkersville, WV (26447)	851
Wallace, WV (26448)	1036
Wallback, WV (25285)	520
Walton, WV (25286)	1104
Wana, WV (26590)	574
War, WV (24892)	915
Wardensville, WV (26851)	1688
Washington, WV (26181)	5489
Waverly, WV (26184)	1905
Wayne, WV (25570)	4502
Webster Springs, WV (26288)	2477
Welch, WV (24801)	2633
West Columbia, WV (25287)	494
West Hamlin, WV (25571)	2004
West Milford, WV (26451)	666
Weston, WV (26452)	7915
West Union, WV (26456)	2708
Wharton, WV (25208)	676
White Sulphur Springs, WV (24986)	3959
Whitesville, WV (25209)	888
Wiley Ford, WV (26767)	631
Williamson, WV (25661)	3975
Williamstown, WV (26187)	5122
Winfield, WV (25213)	4721
Worthington, WV (26591)	1155
Yawkey, WV (25573)	677
Calhoun, GA (30701)	28670
Chatsworth, GA (30705)	24368
Chickamauga, GA (30707)	12194
Cohutta, GA (30710)	5041
Crandall, GA (30711)	2690
Dalton, GA (30720)	18693
Dalton, GA (30721)	38542
Flintstone, GA (30725)	3686
La Fayette, GA (30728)	13806
Lyerly, GA (30730)	1494
Menlo, GA (30731)	1821
Plainville, GA (30733)	1578
Ranger, GA (30734)	2314
Resaca, GA (30735)	4928
Ringgold, GA (30736)	32429
Rising Fawn, GA (30738)	2854
Rock Spring, GA (30739)	4190
Rocky Face, GA (30740)	7357
Rossville, GA (30741)	20760
Fort Oglethorpe, GA (30742)	5104
Sugar Valley, GA (30746)	1245
Summerville, GA (30747)	10758
Trenton, GA (30752)	7357
Trion, GA (30753)	5251
Tunnel Hill, GA (30755)	7267
Wildwood, GA (30757)	1285
Lookout Mountain, GA (30750)	2575
Adams, TN (37010)	3891
Adamsville, TN (38310)	4536
Afton, TN (37616)	4031
Alamo, TN (38001)	3400
Alcoa, TN (37701)	6070
Alexandria, TN (37012)	1740
Allardt, TN (38504)	1138
Allons, TN (38541)	1282
Altamont, TN (37301)	1213
Andersonville, TN (37705)	3930
Antioch, TN (37013)	59428
Apison, TN (37302)	2811
Ardmore, TN (38449)	2519
Arlington, TN (38002)	30998
Arrington, TN (37014)	1469
Ashland City, TN (37015)	14315
Athens, TN (37303)	18135
Atoka, TN (38004)	8834
Atwood, TN (38220)	1527
Auburntown, TN (37016)	714
Bath Springs, TN (38311)	655
Baxter, TN (38544)	5176
Bean Station, TN (37708)	4967
Beech Bluff, TN (38313)	2660
Beechgrove, TN (37018)	1590
Beersheba Springs, TN (37305)	558
Belfast, TN (37019)	724
Bell Buckle, TN (37020)	3945
Bells, TN (38006)	4081
Belvidere, TN (37306)	2147
Benton, TN (37307)	3923
Bethel Springs, TN (38315)	2751
Bethpage, TN (37022)	4504
Big Rock, TN (37023)	1370
Big Sandy, TN (38221)	2476
Birchwood, TN (37308)	2240
Blaine, TN (37709)	2849
Bloomington Springs, TN (38545)	1064
Blountville, TN (37617)	11570
Bluff City, TN (37618)	10576
Bolivar, TN (38008)	7573
Bon Aqua, TN (37025)	4934
Bradford, TN (38316)	2322
Bradyville, TN (37026)	1762
Brentwood, TN (37027)	45316
Briceville, TN (37710)	749
Brighton, TN (38011)	7861
Brownsville, TN (38012)	11781
Bruceton, TN (38317)	1745
Brush Creek, TN (38547)	1586
Buchanan, TN (38222)	2102
Buffalo Valley, TN (38548)	640
Bulls Gap, TN (37711)	3868
Bumpus Mills, TN (37028)	517
Burlison, TN (38015)	2294
Burns, TN (37029)	4593
Butler, TN (37640)	2617
Bybee, TN (37713)	1206
Byrdstown, TN (38549)	2871
Calhoun, TN (37309)	1752
Camden, TN (38320)	8278
Carthage, TN (37030)	5410
Caryville, TN (37714)	3270
Castalian Springs, TN (37031)	3190
Cedar Grove, TN (38321)	2046
Cedar Hill, TN (37032)	3691
Celina, TN (38551)	3107
Centerville, TN (37033)	5682
Chapel Hill, TN (37034)	5501
Chapmansboro, TN (37035)	3020
Charleston, TN (37310)	3517
Charlotte, TN (37036)	4605
Chattanooga, TN (37402)	1812
Chattanooga, TN (37403)	1555
Chattanooga, TN (37404)	8832
Chattanooga, TN (37405)	10818
Chattanooga, TN (37406)	9531
Chattanooga, TN (37407)	5649
Chattanooga, TN (37408)	959
Chattanooga, TN (37409)	2336
Chattanooga, TN (37410)	2314
Chattanooga, TN (37411)	13435
Chattanooga, TN (37412)	17869
Chattanooga, TN (37415)	18396
Chattanooga, TN (37416)	11829
Chattanooga, TN (37419)	5106
Chattanooga, TN (37421)	36603
Christiana, TN (37037)	5501
Chuckey, TN (37641)	6883
Church Hill, TN (37642)	12150
Mount Carmel, TN (37645)	4533
Clairfield, TN (37715)	551
Clarkrange, TN (38553)	1724
Clarksville, TN (37040)	33347
Clarksville, TN (37042)	51009
Clarksville, TN (37043)	33098
Southside, TN (37171)	817
Cleveland, TN (37311)	17628
Cleveland, TN (37312)	24564
Cleveland, TN (37323)	23761
Clifton, TN (38425)	1379
Clinton, TN (37716)	19578
Coalmont, TN (37313)	915
College Grove, TN (37046)	3110
Collierville, TN (38017)	42115
Collinwood, TN (38450)	2055
Columbia, TN (38401)	42922
Cookeville, TN (38501)	24783
Cookeville, TN (38506)	20859
Copperhill, TN (37317)	1777
Cordova, TN (38016)	34175
Cordova, TN (38018)	29189
Cornersville, TN (37047)	1948
Corryton, TN (37721)	10182
Cosby, TN (37722)	4521
Cottage Grove, TN (38224)	805
Cottontown, TN (37048)	4959
Counce, TN (38326)	1859
Covington, TN (38019)	11989
Cowan, TN (37318)	1520
Crab Orchard, TN (37723)	782
Crawford, TN (38554)	588
Cross Plains, TN (37049)	2827
Crossville, TN (38555)	13065
Crossville, TN (38558)	6569
Crossville, TN (38571)	10575
Crossville, TN (38572)	8843
Culleoka, TN (38451)	4100
Cumberland City, TN (37050)	1329
Cumberland Furnace, TN (37051)	2833
Cumberland Gap, TN (37724)	1614
Cunningham, TN (37052)	2132
Cypress Inn, TN (38452)	763
Dandridge, TN (37725)	12966
Dayton, TN (37321)	13731
Decatur, TN (37322)	6315
Decaturville, TN (38329)	2558
Decherd, TN (37324)	4041
Deer Lodge, TN (37726)	1278
Delano, TN (37325)	1381
Reliance, TN (37369)	700
Del Rio, TN (37727)	1541
Denmark, TN (38391)	1098
Dickson, TN (37055)	20425
Dixon Springs, TN (37057)	641
Dover, TN (37058)	5399
Dowelltown, TN (37059)	1242
Doyle, TN (38559)	1002
Dresden, TN (38225)	4684
Drummonds, TN (38023)	4373
Duck River, TN (38454)	872
Dunlap, TN (37327)	8481
Dyer, TN (38330)	3159
Dyersburg, TN (38024)	20427
Eads, TN (38028)	6168
Eagleville, TN (37060)	1948
Eidson, TN (37731)	552
Elizabethton, TN (37643)	24240
Elmwood, TN (38560)	1047
Elora, TN (37328)	1205
Englewood, TN (37329)	4204
Enville, TN (38332)	860
Erin, TN (37061)	3811
Erwin, TN (37650)	9419
Estill Springs, TN (37330)	5640
Ethridge, TN (38456)	2522
Etowah, TN (37331)	5677
Evensville, TN (37332)	2050
Fairview, TN (37062)	8951
Fall Branch, TN (37656)	3062
Fayetteville, TN (37334)	17374
Finger, TN (38334)	1408
Finley, TN (38030)	847
Five Points, TN (38457)	594
Flag Pond, TN (37657)	650
Flintville, TN (37335)	2041
Franklin, TN (37064)	40050
Franklin, TN (37067)	19811
Franklin, TN (37069)	16667
Friendship, TN (38034)	2142
Friendsville, TN (37737)	4914
Gadsden, TN (38337)	1139
Gainesboro, TN (38562)	4587
Gallatin, TN (37066)	34739
Gates, TN (38037)	1370
Gatlinburg, TN (37738)	5103
Georgetown, TN (37336)	3554
Germantown, TN (38138)	22137
Germantown, TN (38139)	15172
Gleason, TN (38229)	2261
Goodlettsville, TN (37072)	24301
Goodspring, TN (38460)	1118
Gordonsville, TN (38563)	1967
Grand Junction, TN (38039)	1629
Graysville, TN (37338)	2306
Greenback, TN (37742)	4844
Greenbrier, TN (37073)	11103
Greeneville, TN (37743)	19307
Greeneville, TN (37745)	13441
Greenfield, TN (38230)	2816
Grimsley, TN (38565)	965
Gruetli Laager, TN (37339)	1423
Guild, TN (37340)	552
Guys, TN (38339)	575
Halls, TN (38040)	4031
Hampshire, TN (38461)	1154
Hampton, TN (37658)	3335
Harriman, TN (37748)	13895
Harrison, TN (37341)	11000
Harrogate, TN (37752)	4847
Hartford, TN (37753)	619
Hartsville, TN (37074)	5419
Heiskell, TN (37754)	3664
Helenwood, TN (37755)	2377
Henderson, TN (38340)	8919
Hendersonville, TN (37075)	49659
Henning, TN (38041)	2010
Henry, TN (38231)	1436
Hermitage, TN (37076)	28410
Hickman, TN (38567)	656
Hickory Valley, TN (38042)	692
Hilham, TN (38568)	1463
Hillsboro, TN (37342)	2814
Hixson, TN (37343)	34246
Hohenwald, TN (38462)	7770
Holladay, TN (38341)	1609
Hollow Rock, TN (38342)	1173
Hornbeak, TN (38232)	1475
Hornsby, TN (38044)	721
Humboldt, TN (38343)	12415
Huntingdon, TN (38344)	7014
Huntland, TN (37345)	1750
Huntsville, TN (37756)	2113
Huron, TN (38345)	1489
Hurricane Mills, TN (37078)	578
Indian Mound, TN (37079)	2081
Iron City, TN (38463)	1977
Jacksboro, TN (37757)	6975
Jackson, TN (38301)	25142
Jackson, TN (38305)	39451
Jamestown, TN (38556)	8279
Jasper, TN (37347)	6433
Jefferson City, TN (37760)	9183
Jellico, TN (37762)	2314
Joelton, TN (37080)	6307
Johnson City, TN (37601)	25675
Johnson City, TN (37604)	24136
Johnson City, TN (37615)	16338
Jonesborough, TN (37659)	22261
Kelso, TN (37348)	942
Kenton, TN (38233)	2199
Kingsport, TN (37660)	30305
Kingsport, TN (37663)	13178
Kingsport, TN (37664)	22032
Kingsport, TN (37665)	3878
Kingston, TN (37763)	12836
Kingston Springs, TN (37082)	5512
Knoxville, TN (37902)	831
Knoxville, TN (37909)	10829
Knoxville, TN (37912)	15594
Knoxville, TN (37914)	15754
Knoxville, TN (37915)	2955
Knoxville, TN (37916)	1246
Knoxville, TN (37917)	16502
Knoxville, TN (37918)	32909
Knoxville, TN (37919)	22352
Knoxville, TN (37920)	28006
Knoxville, TN (37921)	20905
Knoxville, TN (37922)	29783
Knoxville, TN (37923)	22702
Knoxville, TN (37924)	8996
Knoxville, TN (37931)	20930
Knoxville, TN (37932)	12172
Knoxville, TN (37934)	21174
Knoxville, TN (37938)	14696
Kodak, TN (37764)	7644
Lafayette, TN (37083)	10331
Duff, TN (37729)	921
La Follette, TN (37766)	12520
Lake City, TN (37769)	4569
Lancing, TN (37770)	1827
Lascassas, TN (37085)	3371
La Vergne, TN (37086)	25682
Lavinia, TN (38348)	757
Lawrenceburg, TN (38464)	16715
Lebanon, TN (37087)	31942
Lebanon, TN (37090)	11014
Lenoir City, TN (37771)	12281
Lenoir City, TN (37772)	9552
Leoma, TN (38468)	4106
Lewisburg, TN (37091)	16740
Lexington, TN (38351)	14048
Liberty, TN (37095)	1504
Limestone, TN (37681)	4852
Linden, TN (37096)	4191
Livingston, TN (38570)	7328
Lobelville, TN (37097)	1559
Lookout Mountain, TN (37350)	1832
Loretto, TN (38469)	3203
Loudon, TN (37774)	15756
Louisville, TN (37777)	9280
Luray, TN (38352)	480
Luttrell, TN (37779)	2819
Lyles, TN (37098)	4148
Lynchburg, TN (37352)	2638
Lynnville, TN (38472)	2244
Mc Donald, TN (37353)	3991
Mc Ewen, TN (37101)	5110
Mc Kenzie, TN (38201)	7292
Mcminnville, TN (37110)	23490
Madison, TN (37115)	27744
Madisonville, TN (37354)	12486
Manchester, TN (37355)	19573
Mansfield, TN (38236)	547
Martin, TN (38237)	10359
Maryville, TN (37801)	19697
Maryville, TN (37803)	26014
Maryville, TN (37804)	18783
Mascot, TN (37806)	2377
Mason, TN (38049)	3488
Maynardville, TN (37807)	7401
Medina, TN (38355)	4790
Medon, TN (38356)	1933
Memphis, TN (38103)	6948
Memphis, TN (38104)	15241
Memphis, TN (38105)	3894
Memphis, TN (38106)	20451
Memphis, TN (38107)	13661
Memphis, TN (38108)	13831
Memphis, TN (38109)	37835
Memphis, TN (38111)	30297
Memphis, TN (38112)	12075
Memphis, TN (38114)	21150
Memphis, TN (38115)	30519
Memphis, TN (38116)	33046
Memphis, TN (38117)	22633
Memphis, TN (38118)	32640
Memphis, TN (38119)	18075
Memphis, TN (38120)	12511
Memphis, TN (38122)	17700
Memphis, TN (38125)	30364
Memphis, TN (38126)	4489
Memphis, TN (38127)	33891
Memphis, TN (38128)	32355
Memphis, TN (38133)	16888
Memphis, TN (38134)	30282
Memphis, TN (38135)	24884
Memphis, TN (38141)	18497
Mercer, TN (38392)	612
Michie, TN (38357)	2162
Middleton, TN (38052)	2948
Milan, TN (38358)	9401
Millington, TN (38053)	22315
Milton, TN (37118)	1040
Minor Hill, TN (38473)	855
Mohawk, TN (37810)	1476
Monroe, TN (38573)	1702
Monteagle, TN (37356)	2019
Monterey, TN (38574)	6439
Mooresburg, TN (37811)	2558
Morris Chapel, TN (38361)	821
Morrison, TN (37357)	4350
Morristown, TN (37813)	13004
Morristown, TN (37814)	24892
Moscow, TN (38057)	3088
Midway, TN (37809)	1580
Mosheim, TN (37818)	4149
Moss, TN (38575)	898
Laurel Bloomery, TN (37680)	488
Mountain City, TN (37683)	8327
Mount Juliet, TN (37122)	39644
Mount Pleasant, TN (38474)	6158
Mulberry, TN (37359)	582
Munford, TN (38058)	8770
Murfreesboro, TN (37127)	13028
Murfreesboro, TN (37128)	33173
Murfreesboro, TN (37129)	39668
Murfreesboro, TN (37130)	34702
Nashville, TN (37201)	905
Nashville, TN (37203)	8082
Nashville, TN (37204)	9258
Nashville, TN (37205)	20486
Nashville, TN (37206)	18699
Nashville, TN (37207)	27295
Nashville, TN (37208)	10039
Nashville, TN (37209)	24971
Nashville, TN (37210)	10103
Nashville, TN (37211)	53955
Nashville, TN (37212)	9599
Nashville, TN (37214)	24868
Nashville, TN (37215)	19011
Nashville, TN (37216)	14849
Nashville, TN (37217)	23166
Nashville, TN (37218)	10571
Nashville, TN (37219)	1212
Nashville, TN (37220)	5889
Nashville, TN (37221)	31609
Nashville, TN (37228)	999
Newbern, TN (38059)	6187
New Johnsonville, TN (37134)	2664
New Market, TN (37820)	6133
Newport, TN (37821)	16194
New Tazewell, TN (37825)	4883
Niota, TN (37826)	3500
Nolensville, TN (37135)	7720
Normandy, TN (37360)	1407
Nunnelly, TN (37137)	2055
Oakdale, TN (37829)	1365
Oakfield, TN (38362)	1029
Oakland, TN (38060)	8119
Oak Ridge, TN (37830)	24008
Obion, TN (38240)	1710
Ocoee, TN (37361)	1191
Old Fort, TN (37362)	2722
Old Hickory, TN (37138)	19305
Oliver Springs, TN (37840)	7474
Oneida, TN (37841)	6736
Ooltewah, TN (37363)	25051
Orlinda, TN (37141)	918
Pall Mall, TN (38577)	821
Palmer, TN (37365)	1114
Palmersville, TN (38241)	659
Palmyra, TN (37142)	1428
Paris, TN (38242)	15360
Parrottsville, TN (37843)	2947
Darden, TN (38328)	695
Parsons, TN (38363)	4358
Pegram, TN (37143)	3423
Pelham, TN (37366)	687
Petersburg, TN (37144)	2674
Philadelphia, TN (37846)	3870
Pikeville, TN (37367)	6766
Piney Flats, TN (37686)	6153
Pinson, TN (38366)	2036
Pioneer, TN (37847)	1952
Pleasant Shade, TN (37145)	1853
Pleasant View, TN (37146)	6155
Pocahontas, TN (38061)	755
Portland, TN (37148)	18152
Powell, TN (37849)	21164
Prospect, TN (38477)	2076
Pulaski, TN (38478)	13697
Puryear, TN (38251)	2197
Quebeck, TN (38579)	782
Ramer, TN (38367)	2011
Readyville, TN (37149)	1819
Reagan, TN (38368)	1489
Red Boiling Springs, TN (37150)	3646
Riceville, TN (37370)	3739
Rickman, TN (38580)	1475
Ridgely, TN (38080)	1767
Ripley, TN (38063)	12214
Rives, TN (38253)	964
Roan Mountain, TN (37687)	3536
Robbins, TN (37852)	1667
Rockford, TN (37853)	3124
Rock Island, TN (38581)	3315
Rockvale, TN (37153)	4334
Rockwood, TN (37854)	9352
Rogersville, TN (37857)	15803
Rossville, TN (38066)	2310
Russellville, TN (37860)	3585
Rutherford, TN (38369)	1542
Rutledge, TN (37861)	6167
Saint Joseph, TN (38481)	775
Sale Creek, TN (37373)	2469
Saltillo, TN (38370)	522
Santa Fe, TN (38482)	1403
Sardis, TN (38371)	958
Saulsbury, TN (38067)	1047
Savannah, TN (38372)	13532
Scotts Hill, TN (38374)	1568
Selmer, TN (38375)	6614
Sequatchie, TN (37374)	1297
Sevierville, TN (37862)	15428
Pigeon Forge, TN (37863)	4917
Sevierville, TN (37876)	22377
Sewanee, TN (37375)	2007
Seymour, TN (37865)	17874
Shady Valley, TN (37688)	721
Sharon, TN (38255)	1852
Sharps Chapel, TN (37866)	1250
Shelbyville, TN (37160)	25170
Signal Mountain, TN (37377)	13508
Silver Point, TN (38582)	1051
Smithville, TN (37166)	10335
Smyrna, TN (37167)	40372
Sneedville, TN (37869)	3434
Soddy Daisy, TN (37379)	21291
Somerville, TN (38068)	8574
South Pittsburg, TN (37380)	4855
Sparta, TN (38583)	17899
Speedwell, TN (37870)	3215
Spencer, TN (38585)	2835
Grandview, TN (37337)	1097
Spring City, TN (37381)	6875
Springfield, TN (37172)	23898
Spring Hill, TN (37174)	22942
Springville, TN (38256)	2535
Stanton, TN (38069)	2136
Stantonville, TN (38379)	975
Stewart, TN (37175)	737
Strawberry Plains, TN (37871)	7311
Summertown, TN (38483)	4137
Sunbright, TN (37872)	1562
Surgoinsville, TN (37873)	3242
Sweetwater, TN (37874)	11330
Taft, TN (38488)	1970
Talbott, TN (37877)	7539
Tazewell, TN (37879)	7154
Telford, TN (37690)	3331
Tellico Plains, TN (37385)	5989
Ten Mile, TN (37880)	2904
Tennessee Ridge, TN (37178)	1636
Thompsons Station, TN (37179)	9353
Thorn Hill, TN (37881)	1549
Tiptonville, TN (38079)	2377
Toone, TN (38381)	1200
Townsend, TN (37882)	2283
Tracy City, TN (37387)	3246
Trade, TN (37691)	629
Trenton, TN (38382)	7651
Trezevant, TN (38258)	1242
Trimble, TN (38259)	701
Troy, TN (38260)	3347
Tullahoma, TN (37388)	20304
Turtletown, TN (37391)	1026
Unicoi, TN (37692)	3840
Union City, TN (38261)	12754
Unionville, TN (37180)	2506
Vanleer, TN (37181)	1127
Vonore, TN (37885)	4154
Walland, TN (37886)	3411
Walling, TN (38587)	954
Wartburg, TN (37887)	3997
Wartrace, TN (37183)	2544
Washburn, TN (37888)	2052
Watauga, TN (37694)	1415
Watertown, TN (37184)	4610
Waverly, TN (37185)	6660
Waynesboro, TN (38485)	4948
Westmoreland, TN (37186)	7280
Westpoint, TN (38486)	811
White Bluff, TN (37187)	5633
White House, TN (37188)	11999
White Pine, TN (37890)	5271
Whitesburg, TN (37891)	2848
Whites Creek, TN (37189)	2745
Whiteville, TN (38075)	2918
Whitleyville, TN (38588)	706
Whitwell, TN (37397)	7331
Wildersville, TN (38388)	1313
Primm Springs, TN (38476)	895
Williamsport, TN (38487)	871
Williston, TN (38076)	651
Winchester, TN (37398)	11829
Winfield, TN (37892)	1405
Woodbury, TN (37190)	6711
Woodlawn, TN (37191)	3386
Yuma, TN (38390)	689
Austin, IN (47102)	5403
Boonville, IN (47601)	12023
Borden, IN (47106)	3953
Campbellsburg, IN (47108)	1885
Chandler, IN (47610)	4449
Charlestown, IN (47111)	11961
Chrisney, IN (47611)	1012
Corydon, IN (47112)	13727
Cynthiana, IN (47612)	750
Depauw, IN (47115)	2059
Eckerty, IN (47116)	583
Elberfeld, IN (47613)	2265
Elizabeth, IN (47117)	3691
English, IN (47118)	2588
Taswell, IN (47175)	695
Evansville, IN (47710)	14063
Evansville, IN (47711)	26028
Evansville, IN (47712)	18946
Evansville, IN (47713)	6699
Evansville, IN (47714)	25274
Evansville, IN (47715)	21939
Evansville, IN (47720)	15160
Evansville, IN (47725)	14095
Floyds Knobs, IN (47119)	10134
Fort Branch, IN (47648)	3769
Francisco, IN (47649)	1210
Fredericksburg, IN (47120)	807
Georgetown, IN (47122)	9094
Grandview, IN (47615)	1368
Greenville, IN (47124)	3856
Hardinsburg, IN (47125)	1457
Haubstadt, IN (47639)	3831
Hazleton, IN (47640)	940
Henryville, IN (47126)	3607
Underwood, IN (47177)	1154
Clarksville, IN (47129)	15601
Jeffersonville, IN (47130)	36661
Laconia, IN (47135)	1098
Lanesville, IN (47136)	3818
Leavenworth, IN (47137)	1083
Lexington, IN (47138)	3772
Lynnville, IN (47619)	1473
Marengo, IN (47140)	2198
Marysville, IN (47141)	1328
Mauckport, IN (47142)	749
Memphis, IN (47143)	2693
Milltown, IN (47145)	1678
Mount Vernon, IN (47620)	11552
Nabb, IN (47147)	833
New Albany, IN (47150)	37752
Newburgh, IN (47630)	29541
New Harmony, IN (47631)	1705
New Salisbury, IN (47161)	3048
New Washington, IN (47162)	835
Oakland City, IN (47660)	3969
Otisco, IN (47163)	1245
Owensville, IN (47665)	3093
Palmyra, IN (47164)	3089
Patoka, IN (47666)	1241
Pekin, IN (47165)	5022
Poseyville, IN (47633)	2361
Princeton, IN (47670)	10064
Ramsey, IN (47166)	1234
Richland, IN (47634)	1893
Rockport, IN (47635)	4659
Salem, IN (47167)	12221
Scottsburg, IN (47170)	11696
Sellersburg, IN (47172)	13847
Tennyson, IN (47637)	1292
Wadesville, IN (47638)	3213
Adairville, KY (42202)	1809
Adolphus, KY (42120)	1759
Albany, KY (42602)	6893
Allen, KY (41601)	957
Allensville, KY (42204)	548
Almo, KY (42020)	1804
Alvaton, KY (42122)	3641
Annville, KY (40402)	1985
Argillite, KY (41121)	1293
Arjay, KY (40902)	556
Arlington, KY (42021)	1208
Artemus, KY (40903)	665
Ashcamp, KY (41512)	497
Ashland, KY (41101)	13654
Ashland, KY (41102)	15485
Auburn, KY (42206)	4340
Austin, KY (42123)	643
Auxier, KY (41602)	677
Bagdad, KY (40003)	1595
Banner, KY (41603)	957
Barbourville, KY (40906)	7188
Bardstown, KY (40004)	22978
Bardwell, KY (42023)	1901
Barlow, KY (42024)	1114
Battletown, KY (40104)	903
Baxter, KY (40806)	1684
Beattyville, KY (41311)	3990
Beaver Dam, KY (42320)	6246
Bedford, KY (40006)	4106
Beechmont, KY (42323)	772
Belton, KY (42324)	942
Bee Spring, KY (42207)	943
Belfry, KY (41514)	2672
Benton, KY (42025)	15811
Berea, KY (40403)	18582
Betsy Layne, KY (41605)	870
Big Clifty, KY (42712)	1572
Big Creek, KY (40914)	520
Bimble, KY (40915)	928
Blackey, KY (41804)	657
Blaine, KY (41124)	708
Bledsoe, KY (40810)	901
Bloomfield, KY (40008)	3213
Boaz, KY (42027)	1891
Bonnieville, KY (42713)	1379
Bonnyman, KY (41719)	1242
Booneville, KY (41314)	2893
Boston, KY (40107)	1806
Bowling Green, KY (42101)	35283
Bowling Green, KY (42103)	15347
Bowling Green, KY (42104)	22878
Bradfordsville, KY (40009)	772
Brandenburg, KY (40108)	9395
Bremen, KY (42325)	1685
Brodhead, KY (40409)	2763
Bronston, KY (42518)	2201
Brooks, KY (40109)	2451
Brownsville, KY (42210)	3173
Buckhorn, KY (41721)	500
Buckner, KY (40010)	607
Buffalo, KY (42716)	1273
Bulan, KY (41722)	1495
Burkesville, KY (42717)	4514
Burna, KY (42028)	511
Burnside, KY (42519)	2357
Cadiz, KY (42211)	10064
Calhoun, KY (42327)	3152
Calvert City, KY (42029)	5216
Calvin, KY (40813)	502
Campbellsburg, KY (40011)	1999
Turners Station, KY (40075)	987
Campbellsville, KY (42718)	17818
Elk Horn, KY (42733)	1017
Campton, KY (41301)	3865
Canada, KY (41519)	766
Caneyville, KY (42721)	2761
Canmer, KY (42722)	600
Cannon, KY (40923)	613
Carlisle, KY (40311)	5403
Catlettsburg, KY (41129)	7741
Cave City, KY (42127)	4736
Cawood, KY (40815)	949
Cecilia, KY (42724)	3892
Center, KY (42214)	518
Centertown, KY (42328)	1107
Central City, KY (42330)	6591
Cerulean, KY (42215)	929
Chaplin, KY (40012)	486
Chavies, KY (41727)	737
Clarkson, KY (42726)	3464
Clay, KY (42404)	2013
Clay City, KY (40312)	4490
Clearfield, KY (40313)	1692
Clinton, KY (42031)	2527
Cloverport, KY (40111)	1104
Columbia, KY (42728)	10774
Knifley, KY (42753)	497
Combs, KY (41729)	490
Corbin, KY (40701)	19687
Cornettsville, KY (41731)	773
Corydon, KY (42406)	2437
Coxs Creek, KY (40013)	4534
Crab Orchard, KY (40419)	3235
Crestwood, KY (40014)	17121
Crofton, KY (42217)	3005
Cromwell, KY (42333)	893
Cub Run, KY (42729)	991
Cumberland, KY (40823)	2396
Cunningham, KY (42035)	879
Custer, KY (40115)	549
Danville, KY (40422)	16730
Dawson Springs, KY (42408)	4819
Dexter, KY (42036)	978
Dixon, KY (42409)	1821
Drakesboro, KY (42337)	1393
Dunmor, KY (42339)	690
Dunnville, KY (42528)	1153
Earlington, KY (42410)	1013
East Bernstadt, KY (40729)	4223
Eastview, KY (42732)	1508
Eddyville, KY (42038)	3612
Edmonton, KY (42129)	5160
Ekron, KY (40117)	2201
Elizabethtown, KY (42701)	37226
Elkhorn City, KY (41522)	3047
Elkton, KY (42220)	4909
Eminence, KY (40019)	2816
Ermine, KY (41815)	792
Eubank, KY (42567)	4248
Evarts, KY (40828)	2300
Ezel, KY (41425)	801
Fairdale, KY (40118)	7635
Falls Of Rough, KY (40119)	1468
Fancy Farm, KY (42039)	1317
Farmington, KY (42040)	896
Ferguson, KY (42533)	761
Finchville, KY (40022)	839
Fisherville, KY (40023)	3733
Flatgap, KY (41219)	1397
Flat Lick, KY (40935)	1477
Flatwoods, KY (41139)	6748
Fordsville, KY (42343)	1360
Fort Campbell, KY (42223)	13815
Fort Knox, KY (40121)	6397
Fountain Run, KY (42133)	1042
Frankfort, KY (40601)	39539
Franklin, KY (42134)	12759
Fredonia, KY (42411)	1340
Frenchburg, KY (40322)	2297
Fulton, KY (42041)	3357
Gamaliel, KY (42140)	948
Garfield, KY (40140)	590
Garrett, KY (41630)	861
Garrison, KY (41141)	1908
Georgetown, KY (40324)	32541
Gilbertsville, KY (42044)	2844
Girdler, KY (40943)	748
Glasgow, KY (42141)	22835
Glendale, KY (42740)	1584
Goshen, KY (40026)	4686
Gracey, KY (42232)	729
Graham, KY (42344)	711
Grand Rivers, KY (42045)	1737
Gravel Switch, KY (40328)	864
Gray, KY (40734)	2862
Grayson, KY (41143)	10669
Greensburg, KY (42743)	6650
Greenup, KY (41144)	7836
Greenville, KY (42345)	8336
Grethel, KY (41631)	609
Guston, KY (40142)	1774
Guthrie, KY (42234)	1602
Hagerhill, KY (41222)	1912
Hanson, KY (42413)	2397
Happy, KY (41746)	491
Hardin, KY (42048)	1767
Hardinsburg, KY (40143)	4268
Hardy, KY (41531)	740
Hardyville, KY (42746)	1405
Harlan, KY (40831)	3412
Harned, KY (40144)	1375
Harold, KY (41635)	2103
Harrodsburg, KY (40330)	15164
Hartford, KY (42347)	4708
Hawesville, KY (42348)	3925
Hazard, KY (41701)	7753
Busy, KY (41723)	731
Hazel, KY (42049)	1257
Hazel Green, KY (41332)	884
Heidrick, KY (40949)	661
Henderson, KY (42420)	29083
Herndon, KY (42236)	685
Hickman, KY (42050)	2108
Hickory, KY (42051)	2319
Hi Hat, KY (41636)	580
Hindman, KY (41822)	2175
Hitchins, KY (41146)	513
Hodgenville, KY (42748)	6852
Hopkinsville, KY (42240)	30637
Horse Branch, KY (42349)	1085
Horse Cave, KY (42749)	3736
Hudson, KY (40145)	587
Hueysville, KY (41640)	867
Hustonville, KY (40437)	3277
Hyden, KY (41749)	2646
Inez, KY (41224)	3712
Irvine, KY (40336)	9697
Ravenna, KY (40472)	1088
Irvington, KY (40146)	2690
Island, KY (42350)	1080
Isom, KY (41824)	912
Jackson, KY (41339)	6879
Jamestown, KY (42629)	3614
Viper, KY (41774)	1807
Jeffersonville, KY (40337)	3916
Jenkins, KY (41537)	2846
Jeremiah, KY (41826)	667
Junction City, KY (40440)	1954
Keavy, KY (40737)	1029
Kevil, KY (42053)	4117
Kimper, KY (41539)	1236
Kings Mountain, KY (40442)	823
Kirksey, KY (42054)	834
Kite, KY (41828)	533
Knob Lick, KY (42154)	580
Kuttawa, KY (42055)	1946
La Center, KY (42056)	1602
La Grange, KY (40031)	15818
Lancaster, KY (40444)	10705
Lawrenceburg, KY (40342)	18325
Lebanon, KY (40033)	9191
Lebanon Junction, KY (40150)	3545
Leburn, KY (41831)	722
Ledbetter, KY (42058)	1881
Leitchfield, KY (42754)	10551
Lewisburg, KY (42256)	3774
Lewisport, KY (42351)	3257
Lexington, KY (40502)	20798
Lexington, KY (40503)	22217
Lexington, KY (40504)	17914
Lexington, KY (40505)	19655
Lexington, KY (40507)	1172
Lexington, KY (40508)	9777
Lexington, KY (40509)	25878
Lexington, KY (40510)	785
Lexington, KY (40511)	22292
Lexington, KY (40513)	9824
Lexington, KY (40514)	12798
Lexington, KY (40515)	27792
Lexington, KY (40516)	2109
Lexington, KY (40517)	25686
Liberty, KY (42539)	7011
Lily, KY (40740)	2324
Livermore, KY (42352)	1612
Livingston, KY (40445)	613
Orlando, KY (40460)	638
London, KY (40741)	15405
London, KY (40744)	12878
Loretto, KY (40037)	2278
Lost Creek, KY (41348)	956
Louisa, KY (41230)	8613
Louisville, KY (40202)	2821
Louisville, KY (40203)	10142
Louisville, KY (40204)	10668
Louisville, KY (40205)	19237
Louisville, KY (40206)	14856
Louisville, KY (40207)	25912
Louisville, KY (40208)	6835
Louisville, KY (40209)	475
Louisville, KY (40210)	9539
Louisville, KY (40211)	15183
Louisville, KY (40212)	11586
Louisville, KY (40213)	13424
Louisville, KY (40214)	35096
Louisville, KY (40215)	14970
Louisville, KY (40216)	32430
Louisville, KY (40217)	9266
Louisville, KY (40218)	23129
Louisville, KY (40219)	28999
Louisville, KY (40220)	27667
Louisville, KY (40222)	17818
Louisville, KY (40223)	19666
Louisville, KY (40228)	14166
Louisville, KY (40229)	29263
Louisville, KY (40241)	24957
Louisville, KY (40242)	9022
Louisville, KY (40243)	8686
Louisville, KY (40245)	25413
Louisville, KY (40258)	21374
Louisville, KY (40272)	29272
Louisville, KY (40291)	30658
Louisville, KY (40299)	33001
Lovely, KY (41231)	749
Lowmansville, KY (41232)	531
Mc Carr, KY (41544)	671
Mc Daniels, KY (40152)	586
Mc Dowell, KY (41647)	1224
Mc Kee, KY (40447)	4785
Mc Roberts, KY (41835)	488
Maceo, KY (42355)	1556
Madisonville, KY (42431)	20728
Magnolia, KY (42757)	2261
Mallie, KY (41836)	579
Mammoth Cave, KY (42259)	767
Manchester, KY (40962)	10325
Manitou, KY (42436)	1106
Marion, KY (42064)	6058
Martin, KY (41649)	1955
Mayfield, KY (42066)	16982
Mayking, KY (41837)	684
Means, KY (40346)	590
Melber, KY (42069)	807
Melvin, KY (41650)	553
Middlesboro, KY (40965)	8784
Midway, KY (40347)	2539
Milton, KY (40045)	2580
Monticello, KY (42633)	14080
Morehead, KY (40351)	13422
Morganfield, KY (42437)	5754
Morgantown, KY (42261)	7684
Mount Eden, KY (40046)	1428
Mount Sterling, KY (40353)	16521
Mount Vernon, KY (40456)	6658
Mount Washington, KY (40047)	16308
Mousie, KY (41839)	479
Mouthcard, KY (41548)	507
Muldraugh, KY (40155)	664
Munfordville, KY (42765)	4253
Murray, KY (42071)	19797
Nancy, KY (42544)	4311
Neon, KY (41840)	904
New Castle, KY (40050)	1297
New Concord, KY (42076)	851
New Haven, KY (40051)	3634
New Hope, KY (40052)	478
Nicholasville, KY (40356)	31017
Nortonville, KY (42442)	2435
Oak Grove, KY (42262)	6300
Oakland, KY (42159)	1004
Oil Springs, KY (41238)	790
Olive Hill, KY (41164)	9043
Olmstead, KY (42265)	739
Olympia, KY (40358)	558
Oneida, KY (40972)	891
Owensboro, KY (42301)	32960
Owensboro, KY (42303)	30036
Owenton, KY (40359)	5472
Owingsville, KY (40360)	4962
Paducah, KY (42001)	22402
Paducah, KY (42003)	22476
Paint Lick, KY (40461)	1887
East Point, KY (41216)	742
Paintsville, KY (41240)	4743
Paris, KY (40361)	13921
Park City, KY (42160)	1574
Parkers Lake, KY (42634)	854
Parksville, KY (40464)	897
Payneville, KY (40157)	825
Pembroke, KY (42266)	1723
Pendleton, KY (40055)	1699
Perryville, KY (40468)	1504
Pewee Valley, KY (40056)	2953
Phelps, KY (41553)	1556
Philpot, KY (42366)	5213
Phyllis, KY (41554)	563
Pikeville, KY (41501)	13582
Pilgrim, KY (41250)	542
Pine Knot, KY (42635)	2482
Pine Top, KY (41843)	560
Pineville, KY (40977)	5825
Pinsonfork, KY (41555)	490
Pippa Passes, KY (41844)	627
Pleasureville, KY (40057)	2725
Powderly, KY (42367)	826
Langley, KY (41645)	846
Prestonsburg, KY (41653)	7952
Princeton, KY (42445)	8714
Printer, KY (41655)	530
Prospect, KY (40059)	14862
Nebo, KY (42441)	1198
Providence, KY (42450)	3055
Quincy, KY (41166)	521
Raccoon, KY (41557)	1335
Radcliff, KY (40160)	17547
Raywick, KY (40060)	864
Reed, KY (42451)	662
Regina, KY (41559)	575
Reynolds Station, KY (42368)	999
Richmond, KY (40475)	37798
Rineyville, KY (40162)	4853
Robards, KY (42452)	2032
Robinson Creek, KY (41560)	516
Rockfield, KY (42274)	1951
Rockholds, KY (40759)	1776
Roundhill, KY (42275)	662
Rush, KY (41168)	2324
Russell, KY (41169)	4819
Russell Springs, KY (42642)	9335
Russellville, KY (42276)	11223
Sacramento, KY (42372)	1452
Sadieville, KY (40370)	2433
Salem, KY (42078)	1447
Salt Lick, KY (40371)	1966
Salvisa, KY (40372)	1993
Salyersville, KY (41465)	7733
Sandy Hook, KY (41171)	2755
Science Hill, KY (42553)	4154
Scottsville, KY (42164)	11741
Sebree, KY (42455)	2620
Sedalia, KY (42079)	1149
Sharpsburg, KY (40374)	1280
Shelbiana, KY (41562)	1858
Shelbyville, KY (40065)	21637
Shepherdsville, KY (40165)	26863
Sidney, KY (41564)	821
Simpsonville, KY (40067)	4036
Slaughters, KY (42456)	1464
Smithfield, KY (40068)	1973
Smithland, KY (42081)	1735
Smiths Grove, KY (42171)	5379
Somerset, KY (42501)	11824
Somerset, KY (42503)	16721
Sonora, KY (42776)	2026
South Portsmouth, KY (41174)	733
South Shore, KY (41175)	4249
Spottsville, KY (42458)	854
Springfield, KY (40069)	6588
Staffordsville, KY (41256)	1744
Stamping Ground, KY (40379)	2860
Stanford, KY (40484)	9399
Stanton, KY (40380)	5219
Stanville, KY (41659)	541
Stearns, KY (42647)	2443
Stinnett, KY (40868)	629
Strunk, KY (42649)	853
Sturgis, KY (42459)	3467
Summer Shade, KY (42166)	1786
Summersville, KY (42782)	809
Symsonia, KY (42082)	1549
Taylorsville, KY (40071)	11786
Thelma, KY (41260)	490
Tollesboro, KY (41189)	1843
Tomahawk, KY (41262)	736
Tompkinsville, KY (42167)	6134
Topmost, KY (41862)	581
Trenton, KY (42286)	1140
Tyner, KY (40486)	1545
Uniontown, KY (42461)	1253
Upton, KY (42784)	2123
Utica, KY (42376)	4736
Vanceburg, KY (41179)	5255
Vancleve, KY (41385)	584
Van Lear, KY (41265)	1116
Versailles, KY (40383)	19344
Vicco, KY (41773)	1027
Vine Grove, KY (40175)	10700
Virgie, KY (41572)	2354
Waco, KY (40385)	2533
Waddy, KY (40076)	2174
Wallins Creek, KY (40873)	1377
Warfield, KY (41267)	581
Water Valley, KY (42085)	715
Waverly, KY (42462)	1123
Wayland, KY (41666)	553
Waynesburg, KY (40489)	2888
Webbville, KY (41180)	688
Webster, KY (40176)	914
Wellington, KY (40387)	1311
West Liberty, KY (41472)	6373
West Paducah, KY (42086)	3509
West Point, KY (40177)	1143
Westport, KY (40077)	534
White Plains, KY (42464)	1433
Whitesburg, KY (41858)	4789
Whitesville, KY (42378)	2680
Whitley City, KY (42653)	2926
Wickliffe, KY (42087)	1811
Williamsburg, KY (40769)	11540
Willisburg, KY (40078)	1678
Wilmore, KY (40390)	4629
Winchester, KY (40391)	27600
Wingo, KY (42088)	2197
Sitka, KY (41255)	706
Wittensville, KY (41274)	677
Woodbine, KY (40771)	1160
Woodburn, KY (42170)	1254
Wooton, KY (41776)	1316
Worthington, KY (41183)	1368
Yosemite, KY (42566)	503
South Fulton, TN (38257)	3778
Ada, OH (45810)	4763
Adena, OH (43901)	1712
Akron, OH (44301)	11576
Akron, OH (44302)	3523
Akron, OH (44303)	5813
Akron, OH (44304)	1590
Akron, OH (44305)	16710
Akron, OH (44306)	14933
Akron, OH (44307)	4827
Akron, OH (44308)	351
Akron, OH (44310)	16557
Akron, OH (44311)	3721
Akron, OH (44312)	26429
Akron, OH (44313)	20720
Akron, OH (44314)	14215
Akron, OH (44319)	19429
Akron, OH (44320)	15309
Akron, OH (44321)	12644
Akron, OH (44333)	16582
Alger, OH (45812)	1655
Alliance, OH (44601)	26285
Alvada, OH (44802)	886
Alvordton, OH (43501)	669
Amherst, OH (44001)	19185
Amsterdam, OH (43903)	1612
Andover, OH (44003)	3476
Antwerp, OH (45813)	3085
Apple Creek, OH (44606)	5177
Arcadia, OH (44804)	1036
Archbold, OH (43502)	6315
Arlington, OH (45814)	2418
Ashland, OH (44805)	25269
Ashtabula, OH (44004)	24745
Attica, OH (44807)	2044
Atwater, OH (44201)	5724
Aurora, OH (44202)	17576
Austinburg, OH (44010)	1490
Avon, OH (44011)	17564
Avon Lake, OH (44012)	20328
Barberton, OH (44203)	33328
Beach City, OH (44608)	2222
Bellaire, OH (43906)	6531
Bellevue, OH (44811)	11113
Bellville, OH (44813)	6567
Beloit, OH (44609)	3143
Berea, OH (44017)	14569
Bergholz, OH (43908)	1081
Berkey, OH (43504)	1010
Berlin Center, OH (44401)	2546
Berlin Heights, OH (44814)	2551
Big Prairie, OH (44611)	1510
Bloomdale, OH (44817)	1215
Bloomingdale, OH (43910)	3143
Bloomville, OH (44818)	2204
Bluffton, OH (45817)	5371
Bolivar, OH (44612)	4500
Bowerston, OH (44695)	1108
Bowling Green, OH (43402)	21455
Bradner, OH (43406)	1512
Brewster, OH (44613)	1680
Bridgeport, OH (43912)	4988
Brilliant, OH (43913)	1179
Bristolville, OH (44402)	2898
Brookfield, OH (44403)	3577
Brunswick, OH (44212)	38144
Bryan, OH (43506)	12989
Bucyrus, OH (44820)	14786
Burbank, OH (44214)	1820
Burghill, OH (44404)	1223
Burgoon, OH (43407)	575
Burton, OH (44021)	5173
Butler, OH (44822)	2794
Cadiz, OH (43907)	4250
Campbell, OH (44405)	5931
Canal Fulton, OH (44614)	10907
Canfield, OH (44406)	20252
Canton, OH (44702)	356
Canton, OH (44703)	5736
Canton, OH (44704)	2682
Canton, OH (44705)	13404
Canton, OH (44706)	14346
Canton, OH (44707)	6629
Canton, OH (44708)	21106
Canton, OH (44709)	14628
Canton, OH (44710)	6925
Canton, OH (44714)	7089
Canton, OH (44718)	10976
North Canton, OH (44720)	34296
Canton, OH (44721)	11678
East Canton, OH (44730)	5281
Carrollton, OH (44615)	9012
Castalia, OH (44824)	3768
Cecil, OH (45821)	1167
Celina, OH (45822)	16605
Chagrin Falls, OH (44022)	15819
Chagrin Falls, OH (44023)	16077
Chardon, OH (44024)	20806
Chesterland, OH (44026)	10527
Chippewa Lake, OH (44215)	1835
Clarington, OH (43915)	1271
Cleveland, OH (44102)	27699
Cleveland, OH (44103)	11042
Cleveland, OH (44104)	13430
Cleveland, OH (44105)	28184
Cleveland, OH (44106)	14014
Lakewood, OH (44107)	40239
Cleveland, OH (44108)	18024
Cleveland, OH (44109)	28830
Cleveland, OH (44110)	13607
Cleveland, OH (44111)	31255
Cleveland, OH (44112)	14933
Cleveland, OH (44113)	10106
Cleveland, OH (44114)	3371
Cleveland, OH (44115)	4057
Rocky River, OH (44116)	18256
Euclid, OH (44117)	7440
Cleveland, OH (44118)	29798
Cleveland, OH (44119)	9805
Cleveland, OH (44120)	28365
Cleveland, OH (44121)	26480
Beachwood, OH (44122)	29290
Euclid, OH (44123)	13620
Cleveland, OH (44124)	33970
Cleveland, OH (44125)	23068
Cleveland, OH (44126)	15032
Cleveland, OH (44127)	3564
Cleveland, OH (44128)	22126
Cleveland, OH (44129)	24474
Cleveland, OH (44130)	44285
Independence, OH (44131)	19061
Euclid, OH (44132)	11128
North Royalton, OH (44133)	27776
Cleveland, OH (44134)	33030
Cleveland, OH (44135)	20486
Strongsville, OH (44136)	23285
Maple Heights, OH (44137)	18342
Olmsted Falls, OH (44138)	19267
Solon, OH (44139)	22574
Bay Village, OH (44140)	14350
Brecksville, OH (44141)	13152
Brookpark, OH (44142)	16814
Cleveland, OH (44143)	21472
Cleveland, OH (44144)	17899
Westlake, OH (44145)	28762
Bedford, OH (44146)	24571
Broadview Heights, OH (44147)	17163
Strongsville, OH (44149)	17671
Clinton, OH (44216)	8457
Cloverdale, OH (45827)	1983
Clyde, OH (43410)	9017
Coldwater, OH (45828)	5327
Collins, OH (44826)	1534
Columbiana, OH (44408)	8754
Columbia Station, OH (44028)	7817
Columbus Grove, OH (45830)	5282
Conneaut, OH (44030)	11749
Continental, OH (45831)	2695
Convoy, OH (45832)	2527
Cortland, OH (44410)	15757
Crestline, OH (44827)	5808
Creston, OH (44217)	3484
Curtice, OH (43412)	3804
Custar, OH (43511)	773
Cuyahoga Falls, OH (44221)	24573
Cuyahoga Falls, OH (44223)	15579
Stow, OH (44224)	33898
Cygnet, OH (43413)	1226
Dalton, OH (44618)	5430
Deerfield, OH (44411)	1852
Defiance, OH (43512)	24242
Dellroy, OH (44620)	1315
Delphos, OH (45833)	9356
Delta, OH (43515)	6891
Dennison, OH (44621)	3700
Deshler, OH (43516)	2542
Diamond, OH (44412)	2403
Dillonvale, OH (43917)	2163
Dorset, OH (44032)	1319
Dover, OH (44622)	15557
Doylestown, OH (44230)	6845
Dundee, OH (44624)	3695
Dunkirk, OH (45836)	1230
East Liverpool, OH (43920)	17882
East Palestine, OH (44413)	5943
East Rochester, OH (44625)	1237
East Sparta, OH (44626)	2682
Edgerton, OH (43517)	3117
Edon, OH (43518)	2274
Elmore, OH (43416)	2544
Elyria, OH (44035)	50414
North Ridgeville, OH (44039)	26034
Farmdale, OH (44417)	1471
Fayette, OH (43521)	2264
Findlay, OH (45840)	44349
Flushing, OH (43977)	1675
Forest, OH (45843)	3140
Fort Jennings, OH (45844)	2951
Fort Loramie, OH (45845)	2883
Fort Recovery, OH (45846)	3792
Fostoria, OH (44830)	15359
Fowler, OH (44418)	1175
Fredericksburg, OH (44627)	4185
Freeport, OH (43973)	1347
Fremont, OH (43420)	25714
Galion, OH (44833)	13981
Garrettsville, OH (44231)	6844
Gates Mills, OH (44040)	3144
Geneva, OH (44041)	12404
Genoa, OH (43430)	4202
Gibsonburg, OH (43431)	4063
Girard, OH (44420)	12959
Glenmont, OH (44628)	940
Gnadenhutten, OH (44629)	1914
Grafton, OH (44044)	10538
Grand Rapids, OH (43522)	2986
Graytown, OH (43432)	1313
Green Springs, OH (44836)	2165
Greenwich, OH (44837)	3472
Grover Hill, OH (45849)	993
Hamler, OH (43524)	1173
Hammondsville, OH (43930)	788
Hanoverton, OH (44423)	2073
Harrod, OH (45850)	3150
Hartville, OH (44632)	8511
Haskins, OH (43525)	927
Haviland, OH (45851)	531
Helena, OH (43435)	1313
Hicksville, OH (43526)	5026
Hinckley, OH (44233)	7081
Hiram, OH (44234)	3123
Holgate, OH (43527)	1966
Holland, OH (43528)	13829
Holmesville, OH (44633)	1748
Homerville, OH (44235)	1171
Homeworth, OH (44634)	1868
Hopedale, OH (43976)	1222
Hubbard, OH (44425)	13005
Hudson, OH (44236)	23264
Huntsburg, OH (44046)	1701
Huron, OH (44839)	11084
Irondale, OH (43932)	804
Jacobsburg, OH (43933)	1646
Jefferson, OH (44047)	7841
Jeromesville, OH (44840)	2514
Jewett, OH (43986)	1491
Kansas, OH (44841)	744
Kensington, OH (44427)	1279
Kent, OH (44240)	25942
Streetsboro, OH (44241)	14230
Killbuck, OH (44637)	2117
Kingsville, OH (44048)	2174
Kinsman, OH (44428)	2837
Lagrange, OH (44050)	5525
Lake Milton, OH (44429)	2146
Lakeside Marblehead, OH (43440)	4110
Lakeville, OH (44638)	1259
Leavittsburg, OH (44430)	3279
Leetonia, OH (44431)	4212
Leipsic, OH (45856)	4301
Liberty Center, OH (43532)	3308
Lima, OH (45801)	16631
Lima, OH (45804)	11009
Lima, OH (45805)	18096
Lima, OH (45806)	9800
Lima, OH (45807)	10643
Lindsey, OH (43442)	883
Lisbon, OH (44432)	8544
Litchfield, OH (44253)	3228
Lodi, OH (44254)	4269
Lorain, OH (44052)	22116
Lorain, OH (44053)	14680
Sheffield Lake, OH (44054)	10947
Lorain, OH (44055)	14238
Loudonville, OH (44842)	4828
Louisville, OH (44641)	17500
Lowellville, OH (44436)	3261
Lucas, OH (44843)	2285
Luckey, OH (43443)	1629
Lyons, OH (43533)	1358
Mc Clure, OH (43534)	1491
Mc Comb, OH (45858)	2707
Mc Cutchenville, OH (44844)	703
Mc Donald, OH (44437)	3797
Madison, OH (44057)	16496
Magnolia, OH (44643)	2693
Malinta, OH (43535)	737
Malvern, OH (44644)	4056
Mansfield, OH (44902)	3269
Mansfield, OH (44903)	21277
Mansfield, OH (44904)	12545
Mansfield, OH (44905)	9841
Mansfield, OH (44906)	13477
Mansfield, OH (44907)	11464
Mantua, OH (44255)	6996
Maria Stein, OH (45860)	1886
Marshallville, OH (44645)	2194
Martin, OH (43445)	1047
Martins Ferry, OH (43935)	6942
Massillon, OH (44646)	38659
Massillon, OH (44647)	14897
Masury, OH (44438)	3879
Maumee, OH (43537)	24370
Mechanicstown, OH (44651)	664
Medina, OH (44256)	53655
Mendon, OH (45862)	1268
Mentor, OH (44060)	55006
Metamora, OH (43540)	1219
Middlefield, OH (44062)	9719
Middle Point, OH (45863)	1051
Milan, OH (44846)	3108
Millbury, OH (43447)	3111
Millersburg, OH (44654)	14444
Mineral City, OH (44656)	2337
Mineral Ridge, OH (44440)	3954
Minerva, OH (44657)	8558
Mingo Junction, OH (43938)	4479
Minster, OH (45865)	4377
Mogadore, OH (44260)	11851
Monclova, OH (43542)	3141
Monroeville, OH (44847)	3425
Montpelier, OH (43543)	6488
Montville, OH (44064)	1522
Mount Blanchard, OH (45867)	1087
Mount Cory, OH (45868)	596
Munroe Falls, OH (44262)	4690
Napoleon, OH (43545)	12429
Navarre, OH (44662)	7868
Negley, OH (44441)	1428
Nevada, OH (44849)	1897
New Bavaria, OH (43548)	656
New Bremen, OH (45869)	4272
Newbury, OH (44065)	3719
New Knoxville, OH (45871)	1935
New London, OH (44851)	4542
New Middletown, OH (44442)	3472
New Philadelphia, OH (44663)	20885
New Riegel, OH (44853)	1295
New Springfield, OH (44443)	1597
Newton Falls, OH (44444)	8868
New Washington, OH (44854)	1615
New Waterford, OH (44445)	2766
Ney, OH (43549)	1253
Niles, OH (44446)	16704
North Baltimore, OH (45872)	3370
North Benton, OH (44449)	1078
North Bloomfield, OH (44450)	1540
North Fairfield, OH (44855)	1131
Macedonia, OH (44056)	10243
Northfield, OH (44067)	18408
North Jackson, OH (44451)	2656
North Lawrence, OH (44666)	2633
North Lima, OH (44452)	2525
North Olmsted, OH (44070)	29015
Norwalk, OH (44857)	19944
Nova, OH (44859)	1575
Novelty, OH (44072)	4287
Oak Harbor, OH (43449)	7354
Oakwood, OH (45873)	2070
Oberlin, OH (44074)	7834
Ohio City, OH (45874)	1819
Orrville, OH (44667)	11101
Orwell, OH (44076)	3835
Ottawa, OH (45875)	9608
Painesville, OH (44077)	46918
Pandora, OH (45877)	1871
Paris, OH (44669)	1282
Paulding, OH (45879)	5170
Payne, OH (45880)	2118
Pemberville, OH (43450)	3126
Peninsula, OH (44264)	2083
Perry, OH (44081)	6228
Perrysburg, OH (43551)	31679
Perrysville, OH (44864)	2654
Petersburg, OH (44454)	893
Pierpont, OH (44082)	1224
Pioneer, OH (43554)	2170
Plymouth, OH (44865)	2681
Polk, OH (44866)	1640
Portage, OH (43451)	986
Port Clinton, OH (43452)	11969
Powhatan Point, OH (43942)	1927
Ravenna, OH (44266)	27359
Jenera, OH (45841)	865
Rawson, OH (45881)	1265
Rayland, OH (43943)	3057
Republic, OH (44867)	1923
Richfield, OH (44286)	5503
Richmond, OH (43944)	2204
Risingsun, OH (43457)	1339
Rittman, OH (44270)	7222
Rock Creek, OH (44084)	3016
Rockford, OH (45882)	2589
Rogers, OH (44455)	1429
Rome, OH (44085)	2578
Rootstown, OH (44272)	4681
Rudolph, OH (43462)	1016
Saint Henry, OH (45883)	3398
Saint Marys, OH (45885)	10830
Salem, OH (44460)	21189
Salineville, OH (43945)	2372
Sandusky, OH (44870)	32996
Sardis, OH (43946)	1585
Scio, OH (43988)	1856
Sebring, OH (44672)	3823
Seville, OH (44273)	5915
Shadyside, OH (43947)	4486
Shelby, OH (44875)	11720
Sherrodsville, OH (44675)	1589
Sherwood, OH (43556)	1596
Shiloh, OH (44878)	2326
Shreve, OH (44676)	3972
Smithville, OH (44677)	2326
Southington, OH (44470)	3290
Spencer, OH (44275)	2936
Spencerville, OH (45887)	4027
Saint Clairsville, OH (43950)	11430
Sterling, OH (44276)	1744
Steubenville, OH (43952)	12725
Steubenville, OH (43953)	9680
Strasburg, OH (44680)	3492
Struthers, OH (44471)	8772
Stryker, OH (43557)	2452
Sugarcreek, OH (44681)	6038
Sullivan, OH (44880)	2224
Swanton, OH (43558)	11801
Sycamore, OH (44882)	2512
Sylvania, OH (43560)	28018
Tallmadge, OH (44278)	15605
Thompson, OH (44086)	2080
Tiffin, OH (44883)	23129
Tiltonsville, OH (43963)	1084
Tiro, OH (44887)	898
Rossford, OH (43460)	5520
Toledo, OH (43604)	4719
Toledo, OH (43605)	18481
Toledo, OH (43606)	17486
Toledo, OH (43607)	14619
Toledo, OH (43608)	10000
Toledo, OH (43609)	15393
Toledo, OH (43610)	3319
Toledo, OH (43611)	14938
Toledo, OH (43612)	23354
Toledo, OH (43613)	25765
Toledo, OH (43614)	24062
Toledo, OH (43615)	29943
Oregon, OH (43616)	14807
Toledo, OH (43617)	6659
Northwood, OH (43619)	6493
Toledo, OH (43620)	3104
Toledo, OH (43623)	16876
Toronto, OH (43964)	8006
Twinsburg, OH (44087)	18295
Uhrichsville, OH (44683)	6504
Tippecanoe, OH (44699)	794
Uniontown, OH (44685)	23900
Valley City, OH (44280)	4545
Van Buren, OH (45889)	1231
Vanlue, OH (45890)	577
Van Wert, OH (45891)	12969
Venedocia, OH (45894)	559
Vermilion, OH (44089)	14132
Vickery, OH (43464)	1223
Vienna, OH (44473)	3373
Wadsworth, OH (44281)	25319
Wakeman, OH (44889)	5745
Walbridge, OH (43465)	4511
Wapakoneta, OH (45895)	15469
Warren, OH (44481)	9152
Warren, OH (44483)	19999
Warren, OH (44484)	19658
Warren, OH (44485)	11744
Washingtonville, OH (44490)	640
Waterville, OH (43566)	6853
Wauseon, OH (43567)	11179
Wayne, OH (43466)	1835
Waynesburg, OH (44688)	2544
Waynesfield, OH (45896)	1753
Wellington, OH (44090)	9932
Wellsville, OH (43968)	5767
West Farmington, OH (44491)	2705
Weston, OH (43569)	2410
West Salem, OH (44287)	6131
West Unity, OH (43570)	2652
Whitehouse, OH (43571)	6054
Wickliffe, OH (44092)	14390
Willard, OH (44890)	9165
Williamsfield, OH (44093)	1152
Willoughby, OH (44094)	30728
Eastlake, OH (44095)	29475
Willshire, OH (45898)	1022
Wilmot, OH (44689)	513
Windham, OH (44288)	3363
Windsor, OH (44099)	1568
Woodville, OH (43469)	2801
Wooster, OH (44691)	35102
Yorkville, OH (43971)	939
Youngstown, OH (44502)	6309
Youngstown, OH (44504)	3006
Youngstown, OH (44505)	11569
Youngstown, OH (44506)	1574
Youngstown, OH (44507)	3357
Youngstown, OH (44509)	8150
Youngstown, OH (44510)	1314
Youngstown, OH (44511)	15743
Youngstown, OH (44512)	28831
Youngstown, OH (44514)	20459
Youngstown, OH (44515)	23293
Aurora, IN (47001)	9177
Batesville, IN (47006)	10273
Brookville, IN (47012)	8685
Cedar Grove, IN (47016)	836
Cross Plains, IN (47017)	531
Dillsboro, IN (47018)	3733
Florence, IN (47020)	834
Guilford, IN (47022)	2863
West Harrison, IN (47060)	5824
Holton, IN (47023)	1437
Laurel, IN (47024)	2514
Lawrenceburg, IN (47025)	19235
Metamora, IN (47030)	1325
Milan, IN (47031)	4334
Moores Hill, IN (47032)	3168
Oldenburg, IN (47036)	984
Osgood, IN (47037)	3521
Patriot, IN (47038)	923
Rising Sun, IN (47040)	4500
Sunman, IN (47041)	5277
Versailles, IN (47042)	3630
Bennington, IN (47011)	689
Vevay, IN (47043)	4158
West College Corner, IN (47003)	841
Alexandria, KY (41001)	14345
Augusta, KY (41002)	1898
Berry, KY (41003)	2054
Brooksville, KY (41004)	3236
Burlington, KY (41005)	18294
Butler, KY (41006)	3692
California, KY (41007)	3431
Carrollton, KY (41008)	5851
Ghent, KY (41045)	1016
Corinth, KY (41010)	2477
Covington, KY (41011)	18593
Covington, KY (41014)	4909
Latonia, KY (41015)	16948
Covington, KY (41016)	4698
Ft Mitchell, KY (41017)	34850
Erlanger, KY (41018)	23049
Crittenden, KY (41030)	5021
Cynthiana, KY (41031)	12947
De Mossville, KY (41033)	1717
Dover, KY (41034)	840
Dry Ridge, KY (41035)	8779
Ewing, KY (41039)	2091
Falmouth, KY (41040)	5869
Flemingsburg, KY (41041)	5645
Florence, KY (41042)	40441
Foster, KY (41043)	1532
Germantown, KY (41044)	881
Glencoe, KY (41046)	1406
Hebron, KY (41048)	12047
Hillsboro, KY (41049)	1670
Independence, KY (41051)	22044
Mayslick, KY (41055)	1454
Maysville, KY (41056)	11034
Melbourne, KY (41059)	2316
Morning View, KY (41063)	2575
Mount Olivet, KY (41064)	1505
Newport, KY (41071)	14293
Bellevue, KY (41073)	4685
Dayton, KY (41074)	3958
Fort Thomas, KY (41075)	13767
Newport, KY (41076)	13065
Petersburg, KY (41080)	1565
Sanders, KY (41083)	927
Sparta, KY (41086)	1502
Union, KY (41091)	15060
Verona, KY (41092)	2977
Wallingford, KY (41093)	1957
Walton, KY (41094)	10032
Warsaw, KY (41095)	3067
Williamstown, KY (41097)	5283
Worthville, KY (41098)	1365
Aberdeen, OH (45101)	1826
Adamsville, OH (43802)	940
Albany, OH (45710)	4364
Shade, OH (45776)	590
Alexandria, OH (43001)	2179
Amanda, OH (43102)	3800
Amelia, OH (45102)	18614
Amesville, OH (45711)	772
Anna, OH (45302)	3738
Ansonia, OH (45303)	1836
Arcanum, OH (45304)	6436
Ashley, OH (43003)	2354
Ashville, OH (43103)	8944
Athens, OH (45701)	15703
Bainbridge, OH (45612)	3771
Baltic, OH (43804)	2632
Baltimore, OH (43105)	7064
Fleming, OH (45729)	1285
Barnesville, OH (43713)	5733
Batavia, OH (45103)	25565
Beallsville, OH (43716)	1541
Beaver, OH (45613)	2534
Bellbrook, OH (45305)	9423
Belle Center, OH (43310)	2707
Bellefontaine, OH (43311)	16110
Belmont, OH (43718)	2624
Belpre, OH (45714)	8334
Bethel, OH (45106)	9918
Bethesda, OH (43719)	1833
Beverly, OH (45715)	2116
Bidwell, OH (45614)	3363
Blacklick, OH (43004)	19234
Blanchester, OH (45107)	8162
Bloomingburg, OH (43106)	1423
Blue Creek, OH (45616)	967
Blue Rock, OH (43720)	1058
Botkins, OH (45306)	2036
Bradford, OH (45308)	3900
Bremen, OH (43107)	2650
Brinkhaven, OH (43006)	506
Brookville, OH (45309)	10484
Byesville, OH (43723)	3881
Cable, OH (43009)	1725
Caldwell, OH (43724)	5176
Caledonia, OH (43314)	2603
Cambridge, OH (43725)	16033
Camden, OH (45311)	4924
Canal Winchester, OH (43110)	27043
Cardington, OH (43315)	5923
Carey, OH (43316)	5296
Carroll, OH (43112)	4099
Casstown, OH (45312)	1364
Cedarville, OH (45314)	2851
Centerburg, OH (43011)	6022
Chandlersville, OH (43727)	1280
Chesapeake, OH (45619)	6472
Cheshire, OH (45620)	745
Chesterhill, OH (43728)	834
Chillicothe, OH (45601)	41201
Cincinnati, OH (45202)	9646
Cincinnati, OH (45203)	1392
Cincinnati, OH (45204)	3950
Cincinnati, OH (45205)	11782
Cincinnati, OH (45206)	6918
Cincinnati, OH (45207)	3907
Cincinnati, OH (45208)	14765
Cincinnati, OH (45209)	7341
Cincinnati, OH (45211)	28472
Cincinnati, OH (45212)	17321
Cincinnati, OH (45213)	9840
Cincinnati, OH (45214)	5143
Cincinnati, OH (45215)	25019
Cincinnati, OH (45216)	6739
Cincinnati, OH (45217)	5071
Cincinnati, OH (45218)	3405
Cincinnati, OH (45219)	6493
Cincinnati, OH (45220)	8863
Cincinnati, OH (45223)	8539
Cincinnati, OH (45224)	16213
Cincinnati, OH (45225)	5039
Cincinnati, OH (45226)	4658
Cincinnati, OH (45227)	14335
Cincinnati, OH (45229)	8302
Cincinnati, OH (45230)	23360
Cincinnati, OH (45231)	34716
Cincinnati, OH (45232)	3857
Cincinnati, OH (45233)	13900
Cincinnati, OH (45236)	20772
Cincinnati, OH (45237)	15064
Cincinnati, OH (45238)	38407
Cincinnati, OH (45239)	23191
Cincinnati, OH (45240)	22932
Cincinnati, OH (45241)	21481
Cincinnati, OH (45242)	20309
Cincinnati, OH (45243)	13715
Cincinnati, OH (45244)	25904
Cincinnati, OH (45245)	15551
Cincinnati, OH (45246)	12303
Cincinnati, OH (45247)	20669
Cincinnati, OH (45248)	22227
Cincinnati, OH (45249)	12430
Cincinnati, OH (45251)	18953
Cincinnati, OH (45252)	4523
Cincinnati, OH (45255)	19356
Circleville, OH (43113)	18845
Clarksburg, OH (43115)	1035
Clarksville, OH (45113)	3438
Clayton, OH (45315)	4355
Cleves, OH (45002)	10875
College Corner, OH (45003)	737
Columbus, OH (43085)	21192
Columbus, OH (43201)	13039
Columbus, OH (43202)	13248
Columbus, OH (43203)	4578
Columbus, OH (43204)	30596
Columbus, OH (43205)	7185
Columbus, OH (43206)	16195
Columbus, OH (43207)	33999
Columbus, OH (43209)	21668
Columbus, OH (43210)	961
Columbus, OH (43211)	14170
Columbus, OH (43212)	14682
Columbus, OH (43213)	25024
Columbus, OH (43214)	21382
Columbus, OH (43215)	7942
Columbus, OH (43217)	1647
Columbus, OH (43219)	19317
Columbus, OH (43220)	22159
Columbus, OH (43221)	28271
Columbus, OH (43222)	2532
Columbus, OH (43223)	17746
Columbus, OH (43224)	30338
Columbus, OH (43227)	17299
Columbus, OH (43228)	39028
Columbus, OH (43229)	36984
Columbus, OH (43230)	44446
Columbus, OH (43231)	15755
Columbus, OH (43232)	32615
Columbus, OH (43235)	33427
Columbus, OH (43240)	2770
Commercial Point, OH (43116)	1210
Conesville, OH (43811)	721
Conover, OH (45317)	959
Coolville, OH (45723)	2869
Corning, OH (43730)	1903
Coshocton, OH (43812)	15393
Covington, OH (45318)	4627
Crooksville, OH (43731)	4045
Croton, OH (43013)	1038
Crown City, OH (45623)	2494
Cumberland, OH (43732)	1435
Cutler, OH (45724)	1242
Danville, OH (43014)	2593
Union City, OH (45390)	2663
Dayton, OH (45402)	6917
Dayton, OH (45403)	9944
Dayton, OH (45404)	7426
Dayton, OH (45405)	13462
Dayton, OH (45406)	15924
Dayton, OH (45409)	5212
Dayton, OH (45410)	10518
Dayton, OH (45414)	17442
Dayton, OH (45415)	10591
Dayton, OH (45416)	4451
Dayton, OH (45417)	6079
Dayton, OH (45418)	4119
Dayton, OH (45419)	13536
Dayton, OH (45420)	20075
Dayton, OH (45424)	42226
Dayton, OH (45426)	12385
Dayton, OH (45429)	22829
Dayton, OH (45430)	6737
Dayton, OH (45431)	21303
Dayton, OH (45432)	12720
Dayton, OH (45433)	1281
Dayton, OH (45434)	11285
Dayton, OH (45439)	7893
Dayton, OH (45440)	18060
Dayton, OH (45449)	15294
Dayton, OH (45458)	26491
Dayton, OH (45459)	24977
De Graff, OH (43318)	2930
Delaware, OH (43015)	38397
Dresden, OH (43821)	3679
Dublin, OH (43016)	28782
Dublin, OH (43017)	34054
Duncan Falls, OH (43734)	1038
East Liberty, OH (43319)	907
Eaton, OH (45320)	12850
Edison, OH (43320)	1323
Eldorado, OH (45321)	815
Englewood, OH (45322)	18552
Enon, OH (45323)	4727
Fairborn, OH (45324)	28221
Fayetteville, OH (45118)	3252
Felicity, OH (45120)	2862
Fletcher, OH (45326)	1041
Frankfort, OH (45628)	4121
Franklin, OH (45005)	24974
Franklin Furnace, OH (45629)	2369
Frazeysburg, OH (43822)	3940
Fredericktown, OH (43019)	7332
Fresno, OH (43824)	2956
Galena, OH (43021)	8874
Gallipolis, OH (45631)	11566
Galloway, OH (43119)	23235
Gambier, OH (43022)	2086
Georgetown, OH (45121)	6901
Farmersville, OH (45325)	2355
Germantown, OH (45327)	7968
Glenford, OH (43739)	1786
Mount Perry, OH (43760)	1472
Glouster, OH (45732)	3446
Goshen, OH (45122)	9043
Granville, OH (43023)	10048
Greenfield, OH (45123)	6903
Greenville, OH (45331)	19287
Grove City, OH (43123)	49757
Groveport, OH (43125)	10484
Guysville, OH (45735)	1356
Hamden, OH (45634)	1445
Hamersville, OH (45130)	3089
Hamilton, OH (45011)	53645
Hamilton, OH (45013)	43290
Fairfield, OH (45014)	37746
Hamilton, OH (45015)	9206
Harpster, OH (43323)	561
Harrison, OH (45030)	15450
Hebron, OH (43025)	4683
Hilliard, OH (43026)	47635
Hillsboro, OH (45133)	18299
Hollansburg, OH (45332)	498
Hopewell, OH (43746)	1103
Houston, OH (45333)	1260
Howard, OH (43028)	6218
Huntsville, OH (43324)	2436
Ironton, OH (45638)	16078
Jackson, OH (45640)	12415
Jackson Center, OH (45334)	1797
Jamestown, OH (45335)	5979
Jeffersonville, OH (43128)	1978
Jerusalem, OH (43747)	841
Johnstown, OH (43031)	10310
Junction City, OH (43748)	2140
Kenton, OH (43326)	10577
Kimbolton, OH (43749)	1888
Kings Mills, OH (45034)	1077
Kingston, OH (45644)	3467
Kitts Hill, OH (45645)	2328
Lakeview, OH (43331)	3564
Lancaster, OH (43130)	46417
Langsville, OH (45741)	605
La Rue, OH (43332)	1822
Laura, OH (45337)	1575
Laurelville, OH (43135)	3598
South Bloomingville, OH (43152)	793
Lebanon, OH (45036)	27844
Leesburg, OH (45135)	3922
Lewisburg, OH (45338)	4590
Lewis Center, OH (43035)	20522
Lewistown, OH (43333)	746
Lewisville, OH (43754)	1094
Lithopolis, OH (43136)	1015
Little Hocking, OH (45742)	2559
Lockbourne, OH (43137)	2131
Logan, OH (43138)	14179
London, OH (43140)	16541
Londonderry, OH (45647)	1880
Long Bottom, OH (45743)	1007
Lore City, OH (43755)	1326
Loveland, OH (45140)	46082
Lowell, OH (45744)	2491
Lower Salem, OH (45745)	899
Lucasville, OH (45648)	8792
Ludlow Falls, OH (45339)	1120
Lynchburg, OH (45142)	3772
Mc Arthur, OH (45651)	4213
Mcconnelsville, OH (43756)	3754
Mc Dermott, OH (45652)	2547
Maineville, OH (45039)	20577
Malta, OH (43758)	2590
Manchester, OH (45144)	2955
Maplewood, OH (45340)	757
Marengo, OH (43334)	5186
Marietta, OH (45750)	21307
Marion, OH (43302)	39261
Martinsville, OH (45146)	1334
Midland, OH (45148)	1357
Marysville, OH (43040)	24694
Mason, OH (45040)	44080
Mechanicsburg, OH (43044)	4468
Medway, OH (45341)	3176
Miamisburg, OH (45342)	29817
Middleport, OH (45760)	2438
Middletown, OH (45042)	22364
Middletown, OH (45044)	40206
Milford, OH (45150)	27012
Milford Center, OH (43045)	1717
Millersport, OH (43046)	2833
Millfield, OH (45761)	1225
Minford, OH (45653)	3146
Monroe, OH (45050)	7958
Morral, OH (43337)	970
Morrow, OH (45152)	9557
Moscow, OH (45153)	1515
Mount Gilead, OH (43338)	8033
Mount Orab, OH (45154)	7392
Mount Sterling, OH (43143)	4846
Mount Vernon, OH (43050)	22196
Mount Victory, OH (43340)	1220
Nashport, OH (43830)	5102
Nelsonville, OH (45764)	5117
New Albany, OH (43054)	17470
Newark, OH (43055)	47334
Heath, OH (43056)	14622
New Bloomington, OH (43341)	827
New Carlisle, OH (45344)	14497
Newcomerstown, OH (43832)	5825
New Concord, OH (43762)	3605
New Holland, OH (43145)	1678
New Lebanon, OH (45345)	5163
New Lexington, OH (43764)	6156
New Madison, OH (45346)	2000
New Marshfield, OH (45766)	1135
New Matamoras, OH (45767)	2097
New Paris, OH (45347)	3525
New Plymouth, OH (45654)	679
Newport, OH (45768)	1544
New Richmond, OH (45157)	7935
New Straitsville, OH (43766)	1230
New Vienna, OH (45159)	2961
North Bend, OH (45052)	3845
North Lewisburg, OH (43060)	2100
Norwich, OH (43767)	1296
Oak Hill, OH (45656)	4805
Okeana, OH (45053)	3078
Oregonia, OH (45054)	2050
Orient, OH (43146)	7480
Ostrander, OH (43061)	3523
Otway, OH (45657)	1931
Owensville, OH (45160)	611
Oxford, OH (45056)	12167
Pataskala, OH (43062)	23288
Patriot, OH (45658)	1748
Pedro, OH (45659)	2098
Peebles, OH (45660)	5871
Philo, OH (43771)	1587
Pickerington, OH (43147)	33524
Piketon, OH (45661)	5348
Piqua, OH (45356)	21001
Plain City, OH (43064)	10273
Pleasant City, OH (43772)	1599
Pleasant Hill, OH (45359)	1723
Pleasant Plain, OH (45162)	2300
Pleasantville, OH (43148)	1894
Pomeroy, OH (45769)	4757
Portland, OH (45770)	439
Portsmouth, OH (45662)	19913
West Portsmouth, OH (45663)	4988
Port Washington, OH (43837)	1506
Powell, OH (43065)	33749
Proctorville, OH (45669)	8714
Prospect, OH (43342)	2966
Quaker City, OH (43773)	2371
Salesville, OH (43778)	1097
Quincy, OH (43343)	1199
Racine, OH (45771)	2664
Radnor, OH (43066)	1149
Ray, OH (45672)	1273
Raymond, OH (43067)	1423
Reedsville, OH (45772)	1327
Reno, OH (45773)	599
Reynoldsburg, OH (43068)	43129
Richwood, OH (43344)	4746
Ridgeway, OH (43345)	789
Ripley, OH (45167)	2817
Rockbridge, OH (43149)	2149
Roseville, OH (43777)	3441
New Weston, OH (45348)	795
Rossburg, OH (45362)	941
Rushsylvania, OH (43347)	1260
Rushville, OH (43150)	1837
Russells Point, OH (43348)	1699
Russellville, OH (45168)	1229
Russia, OH (45363)	1519
Rutland, OH (45775)	1089
Sabina, OH (45169)	3975
Saint Louisville, OH (43071)	2029
Saint Paris, OH (43072)	5011
Sarahsville, OH (43779)	835
Sardinia, OH (45171)	5043
Scottown, OH (45678)	901
Seaman, OH (45679)	2291
Senecaville, OH (43780)	1834
Shawnee, OH (43782)	635
Sidney, OH (45365)	25141
Somerset, OH (43783)	3687
Somerville, OH (45064)	2527
South Charleston, OH (45368)	4215
South Lebanon, OH (45065)	3521
South Point, OH (45680)	9882
South Salem, OH (45681)	1214
South Solon, OH (43153)	782
South Vienna, OH (45369)	3097
South Webster, OH (45682)	1677
Springboro, OH (45066)	20638
Springfield, OH (45502)	14878
Springfield, OH (45503)	25854
Springfield, OH (45504)	13461
Springfield, OH (45505)	14526
Springfield, OH (45506)	10005
Spring Valley, OH (45370)	2197
Stewart, OH (45778)	700
Stockport, OH (43787)	2222
Stone Creek, OH (43840)	1052
Stout, OH (45684)	1317
Stoutsville, OH (43154)	2655
Sugar Grove, OH (43155)	2068
Summerfield, OH (43788)	720
Sunbury, OH (43074)	10172
Terrace Park, OH (45174)	2148
The Plains, OH (45780)	2301
Thornville, OH (43076)	7200
Thurman, OH (45685)	936
Tipp City, OH (45371)	16367
Trenton, OH (45067)	11430
Troy, OH (45373)	29208
Upper Sandusky, OH (43351)	8595
Urbana, OH (43078)	16893
Utica, OH (43080)	4274
Vandalia, OH (45377)	13029
Versailles, OH (45380)	4688
Vincent, OH (45784)	2787
Vinton, OH (45686)	2402
Waldo, OH (43356)	1051
Walhonding, OH (43843)	960
Warsaw, OH (43844)	3342
Washington Court House, OH (43160)	17667
Waterford, OH (45786)	2585
Waverly, OH (45690)	10843
Waynesville, OH (45068)	9240
Wellston, OH (45692)	6669
West Alexandria, OH (45381)	4794
West Chester, OH (45069)	43697
Westerville, OH (43081)	47781
Westerville, OH (43082)	26537
West Jefferson, OH (43162)	6007
West Lafayette, OH (43845)	3792
West Liberty, OH (43357)	4118
West Manchester, OH (45382)	1028
West Mansfield, OH (43358)	2208
West Milton, OH (45383)	5926
West Union, OH (45693)	6569
Wharton, OH (43359)	678
Wheelersburg, OH (45694)	9145
Whipple, OH (45788)	934
Wilkesville, OH (45695)	525
Williamsburg, OH (45176)	7328
Williamsport, OH (43164)	1936
Willow Wood, OH (45696)	1035
Wilmington, OH (45177)	17750
Winchester, OH (45697)	3769
Woodsfield, OH (43793)	3884
Woodstock, OH (43084)	674
Xenia, OH (45385)	30782
Yellow Springs, OH (45387)	4576
Yorkshire, OH (45388)	706
Zanesfield, OH (43360)	1422
Zanesville, OH (43701)	42159
Albany, IL (61230)	1094
Aledo, IL (61231)	4604
Andalusia, IL (61232)	1261
Annawan, IL (61234)	1154
Atkinson, IL (61235)	1275
Cambridge, IL (61238)	2714
Carbon Cliff, IL (61239)	844
Coal Valley, IL (61240)	5554
Colona, IL (61241)	6282
Cordova, IL (61242)	1057
East Moline, IL (61244)	19064
Erie, IL (61250)	2437
Fulton, IL (61252)	4918
Geneseo, IL (61254)	10570
Hampton, IL (61256)	1702
Hillsdale, IL (61257)	1101
Illinois City, IL (61259)	1241
Joy, IL (61260)	712
Lyndon, IL (61261)	855
Lynn Center, IL (61262)	712
Milan, IL (61264)	9256
Moline, IL (61265)	38912
Morrison, IL (61270)	6595
New Boston, IL (61272)	1315
Orion, IL (61273)	3066
Port Byron, IL (61275)	3904
Prophetstown, IL (61277)	2838
Reynolds, IL (61279)	923
Rock Island, IL (61201)	28916
Sherrard, IL (61281)	2317
Silvis, IL (61282)	6789
Tampico, IL (61283)	1383
Taylor Ridge, IL (61284)	2275
Thomson, IL (61285)	1507
Ackley, IA (50601)	2095
Adair, IA (50002)	1094
Adel, IA (50003)	5662
Afton, IA (50830)	1402
Agency, IA (52530)	850
Ainsworth, IA (52201)	1091
Akron, IA (51001)	2058
Albert City, IA (50510)	968
Albia, IA (52531)	4732
Albion, IA (50005)	623
Alburnett, IA (52202)	961
Alden, IA (50006)	1444
Algona, IA (50511)	6295
Allerton, IA (50008)	672
Allison, IA (50602)	1354
Alta, IA (51002)	2340
Alta Vista, IA (50603)	510
Alton, IA (51003)	1440
Altoona, IA (50009)	13943
Amana, IA (52203)	1578
Ames, IA (50010)	21973
Ames, IA (50014)	15742
Anamosa, IA (52205)	6356
Anita, IA (50020)	1233
Ankeny, IA (50021)	18872
Ankeny, IA (50023)	22710
Anthon, IA (51004)	888
Aplington, IA (50604)	1552
Arcadia, IA (51430)	687
Arlington, IA (50606)	756
Armstrong, IA (50514)	1274
Arnolds Park, IA (51331)	1029
Ashton, IA (51232)	793
Atalissa, IA (52720)	798
Atkins, IA (52206)	1972
Atlantic, IA (50022)	7112
Auburn, IA (51433)	576
Audubon, IA (50025)	2788
Aurelia, IA (51005)	1310
Badger, IA (50516)	611
Bagley, IA (50026)	468
Bancroft, IA (50517)	882
Batavia, IA (52533)	969
Battle Creek, IA (51006)	884
Baxter, IA (50028)	1369
Bayard, IA (50029)	543
Bedford, IA (50833)	1930
Belle Plaine, IA (52208)	2645
Bellevue, IA (52031)	4290
Belmond, IA (50421)	2593
Bennett, IA (52721)	668
Bernard, IA (52032)	1234
Bettendorf, IA (52722)	30958
Birmingham, IA (52535)	745
Blairstown, IA (52209)	980
Blakesburg, IA (52536)	856
Bloomfield, IA (52537)	5320
Blue Grass, IA (52726)	4006
Bode, IA (50519)	523
Bonaparte, IA (52620)	708
Bondurant, IA (50035)	4438
Boone, IA (50036)	13690
Boyden, IA (51234)	1112
Brandon, IA (52210)	629
Breda, IA (51436)	836
Brighton, IA (52540)	1190
Britt, IA (50423)	2328
Bronson, IA (51007)	638
Brooklyn, IA (52211)	2284
Buffalo Center, IA (50424)	1208
Burlington, IA (52601)	23919
Burt, IA (50522)	697
Bussey, IA (50044)	768
Calamus, IA (52729)	755
Callender, IA (50523)	569
Calmar, IA (52132)	1450
Camanche, IA (52730)	4102
Cambridge, IA (50046)	1323
Carlisle, IA (50047)	4609
Carroll, IA (51401)	10479
Cascade, IA (52033)	2734
Casey, IA (50048)	746
Castalia, IA (52133)	476
Cedar Falls, IA (50613)	28522
Robins, IA (52328)	2553
Cedar Rapids, IA (52401)	929
Cedar Rapids, IA (52402)	32180
Cedar Rapids, IA (52403)	19279
Cedar Rapids, IA (52404)	28280
Cedar Rapids, IA (52405)	20107
Cedar Rapids, IA (52411)	6319
Center Point, IA (52213)	3772
Toddville, IA (52341)	1006
Centerville, IA (52544)	6109
Central City, IA (52214)	2640
Chariton, IA (50049)	5162
Charles City, IA (50616)	8244
Charlotte, IA (52731)	791
Charter Oak, IA (51439)	828
Chelsea, IA (52215)	748
Cherokee, IA (51012)	5529
Churdan, IA (50050)	592
Cincinnati, IA (52549)	569
Clare, IA (50524)	482
Clarence, IA (52216)	1230
Clarion, IA (50525)	2918
Clarksville, IA (50619)	1947
Clear Lake, IA (50428)	7996
Cleghorn, IA (51014)	480
Clermont, IA (52135)	717
Clinton, IA (52732)	21927
Clutier, IA (52217)	519
Coggon, IA (52218)	1328
Colesburg, IA (52035)	865
Colfax, IA (50054)	2854
Collins, IA (50055)	803
Colo, IA (50056)	1191
Columbus Junction, IA (52738)	3027
Conesville, IA (52739)	608
Conrad, IA (50621)	1269
Coon Rapids, IA (50058)	1601
Corning, IA (50841)	2411
Correctionville, IA (51016)	1158
Corydon, IA (50060)	2007
Crawfordsville, IA (52621)	622
Cresco, IA (52136)	5009
Creston, IA (50801)	7533
Cumberland, IA (50843)	481
Cumming, IA (50061)	1625
Dakota City, IA (50529)	743
Dallas Center, IA (50063)	2183
Danbury, IA (51019)	708
Danville, IA (52623)	1666
Davenport, IA (52801)	400
Davenport, IA (52802)	7696
Davenport, IA (52803)	16702
Davenport, IA (52804)	21667
Davenport, IA (52806)	22349
Davenport, IA (52807)	18404
Dayton, IA (50530)	962
Decorah, IA (52101)	10409
Dorchester, IA (52140)	460
Deep River, IA (52222)	633
Delhi, IA (52223)	1184
Delmar, IA (52037)	1050
Denison, IA (51442)	7649
Denver, IA (50622)	2840
Des Moines, IA (50309)	3299
Des Moines, IA (50310)	25439
Des Moines, IA (50311)	11817
Des Moines, IA (50312)	12788
Des Moines, IA (50313)	13013
Des Moines, IA (50314)	7376
Des Moines, IA (50315)	27553
Des Moines, IA (50316)	11068
Des Moines, IA (50317)	28311
Des Moines, IA (50320)	15371
Des Moines, IA (50321)	6169
Urbandale, IA (50322)	29647
Urbandale, IA (50323)	9140
Clive, IA (50325)	13630
Pleasant Hill, IA (50327)	8647
De Soto, IA (50069)	922
West Des Moines, IA (50265)	27430
West Des Moines, IA (50266)	20361
De Witt, IA (52742)	6617
Dexter, IA (50070)	1246
Diagonal, IA (50845)	576
Dickens, IA (51333)	473
Dike, IA (50624)	1512
Dixon, IA (52745)	572
Donahue, IA (52746)	843
Donnellson, IA (52625)	2301
Doon, IA (51235)	879
Douds, IA (52551)	573
Dows, IA (50071)	823
Drakesville, IA (52552)	614
Dubuque, IA (52001)	31922
Dubuque, IA (52002)	12501
Dubuque, IA (52003)	12170
Dumont, IA (50625)	825
Duncombe, IA (50532)	789
Dunkerton, IA (50626)	1458
Durant, IA (52747)	1983
Dyersville, IA (52040)	4964
Dysart, IA (52224)	1735
Eagle Grove, IA (50533)	3157
Earlham, IA (50072)	2342
Earlville, IA (52041)	1448
Early, IA (50535)	763
Eddyville, IA (52553)	1419
Edgewood, IA (52042)	1324
Eldon, IA (52554)	1087
Eldora, IA (50627)	2642
Eldridge, IA (52748)	7608
Elgin, IA (52141)	1144
Elkader, IA (52043)	1947
Elkhart, IA (50073)	1011
Ellsworth, IA (50075)	723
Elma, IA (50628)	1059
Ely, IA (52227)	2084
Emmetsburg, IA (50536)	3460
Epworth, IA (52045)	2087
Estherville, IA (51334)	6012
Everly, IA (51338)	930
Exira, IA (50076)	1233
Fairbank, IA (50629)	1824
Fairfax, IA (52228)	2394
Fairfield, IA (52556)	9861
Farley, IA (52046)	1865
Farmersburg, IA (52047)	515
Farmington, IA (52626)	1043
Farnhamville, IA (50538)	487
Fayette, IA (52142)	1074
Fenton, IA (50539)	467
Floyd, IA (50435)	644
Fonda, IA (50540)	892
Fontanelle, IA (50846)	973
Forest City, IA (50436)	4832
Fort Atkinson, IA (52144)	1166
Fort Dodge, IA (50501)	21855
Otho, IA (50569)	698
Fort Madison, IA (52627)	9906
Fredericksburg, IA (50630)	1463
Fremont, IA (52561)	769
Fruitland, IA (52749)	836
Galva, IA (51020)	564
Garnavillo, IA (52049)	1111
Garner, IA (50438)	3568
Garrison, IA (52229)	610
Garwin, IA (50632)	941
George, IA (51237)	1447
Gilbert, IA (50105)	1075
Gilman, IA (50106)	980
Gilmore City, IA (50541)	723
Gladbrook, IA (50635)	1349
Glidden, IA (51443)	1588
Goldfield, IA (50542)	837
Goose Lake, IA (52750)	525
Gowrie, IA (50543)	1288
Graettinger, IA (51342)	1015
Grand Junction, IA (50107)	898
Grand Mound, IA (52751)	927
Granger, IA (50109)	2322
Granville, IA (51022)	712
Greeley, IA (52050)	474
Greene, IA (50636)	1729
Greenfield, IA (50849)	2386
Grimes, IA (50111)	7928
Grinnell, IA (50112)	8660
Grundy Center, IA (50638)	2810
Guthrie Center, IA (50115)	2167
Guttenberg, IA (52052)	2584
Hampton, IA (50441)	4742
Harpers Ferry, IA (52146)	788
Hartford, IA (50118)	720
Hartley, IA (51346)	2181
Hawarden, IA (51023)	2716
Hawkeye, IA (52147)	911
Hazleton, IA (50641)	1245
Hedrick, IA (52563)	1252
Hiawatha, IA (52233)	5715
Hinton, IA (51024)	1784
Holland, IA (50642)	498
Holstein, IA (51025)	1759
Holy Cross, IA (52053)	997
Homestead, IA (52236)	506
Hopkinton, IA (52237)	1337
Hornick, IA (51026)	743
Hospers, IA (51238)	1073
Hubbard, IA (50122)	1166
Hudson, IA (50643)	2521
Hull, IA (51239)	2607
Humboldt, IA (50548)	4880
Humeston, IA (50123)	657
Huxley, IA (50124)	3036
Ida Grove, IA (51445)	2474
Independence, IA (50644)	7129
Indianola, IA (50125)	15319
Inwood, IA (51240)	1402
Ionia, IA (50645)	997
Iowa City, IA (52240)	21415
Coralville, IA (52241)	14525
Iowa City, IA (52245)	14314
Iowa City, IA (52246)	14879
Iowa Falls, IA (50126)	5417
Ireton, IA (51027)	1023
Irwin, IA (51446)	449
Janesville, IA (50647)	1557
Jefferson, IA (50129)	4365
Jesup, IA (50648)	3476
Jewell, IA (50130)	1482
Johnston, IA (50131)	14786
Joice, IA (50446)	474
Kalona, IA (52247)	4271
Kanawha, IA (50447)	918
Kelley, IA (50134)	552
Kellogg, IA (50135)	1410
Kensett, IA (50448)	581
Keokuk, IA (52632)	10097
Keosauqua, IA (52565)	1617
Keota, IA (52248)	1548
Keystone, IA (52249)	839
Kingsley, IA (51028)	1780
Kiron, IA (51448)	522
Klemme, IA (50449)	635
Knoxville, IA (50138)	9320
Lacona, IA (50139)	1076
Ladora, IA (52251)	499
Lake City, IA (51449)	1711
Lake Mills, IA (50450)	2486
Lake Park, IA (51347)	1227
Lake View, IA (51450)	1393
Lakota, IA (50451)	467
Lamoni, IA (50140)	1729
Lamont, IA (50650)	602
La Motte, IA (52054)	911
Lansing, IA (52151)	1809
La Porte City, IA (50651)	3141
Larchwood, IA (51241)	1436
Latimer, IA (50452)	692
Laurel, IA (50141)	470
Laurens, IA (50554)	1378
Lawler, IA (52154)	948
Lawton, IA (51030)	1515
Le Claire, IA (52753)	4434
Lehigh, IA (50557)	629
Leighton, IA (50143)	574
Leland, IA (50453)	515
Le Mars, IA (51031)	10367
Lenox, IA (50851)	1574
Leon, IA (50144)	2214
Letts, IA (52754)	1121
Libertyville, IA (52567)	520
Lime Springs, IA (52155)	1059
Lisbon, IA (52253)	2673
Little Rock, IA (51243)	622
Livermore, IA (50558)	523
Lockridge, IA (52635)	552
Lohrville, IA (51453)	572
Lone Tree, IA (52755)	1653
Long Grove, IA (52756)	2008
Lorimor, IA (50149)	779
Lost Nation, IA (52254)	755
Lovilia, IA (50150)	770
Lowden, IA (52255)	1011
Luana, IA (52156)	566
Lucas, IA (50151)	595
Lu Verne, IA (50560)	502
Lynnville, IA (50153)	658
Lytton, IA (50561)	453
Mc Gregor, IA (52157)	1458
Madrid, IA (50156)	3564
Malcom, IA (50157)	675
Manchester, IA (52057)	7071
Manilla, IA (51454)	1164
Manly, IA (50456)	1419
Manning, IA (51455)	1942
Manson, IA (50563)	2175
Mapleton, IA (51034)	1479
Maquoketa, IA (52060)	7148
Marble Rock, IA (50653)	544
Marcus, IA (51035)	1485
Marengo, IA (52301)	3312
Marion, IA (52302)	31303
Marshalltown, IA (50158)	24585
Martelle, IA (52305)	552
Mason City, IA (50401)	23757
Massena, IA (50853)	593
Maurice, IA (51036)	609
Maxwell, IA (50161)	1723
Maynard, IA (50655)	703
Mechanicsville, IA (52306)	1518
Mediapolis, IA (52637)	2091
Melbourne, IA (50162)	1028
Melcher-dallas, IA (50062)	545
Melrose, IA (52569)	476
Menlo, IA (50164)	561
Merrill, IA (51038)	1407
Miles, IA (52064)	738
Milford, IA (51351)	3871
Ackworth, IA (50001)	552
Milo, IA (50166)	1400
Milton, IA (52570)	636
Minburn, IA (50167)	666
Mingo, IA (50168)	769
Mitchellville, IA (50169)	2113
Monona, IA (52159)	2062
Waterville, IA (52170)	498
Monroe, IA (50170)	2371
Montezuma, IA (50171)	2429
Monticello, IA (52310)	5413
Montour, IA (50173)	613
Montrose, IA (52639)	1649
Moravia, IA (52571)	1149
Morning Sun, IA (52640)	1074
Moscow, IA (52760)	529
Moulton, IA (52572)	807
Mount Ayr, IA (50854)	1864
Mount Pleasant, IA (52641)	9194
Mount Vernon, IA (52314)	4220
Moville, IA (51039)	2093
Murray, IA (50174)	1120
Muscatine, IA (52761)	25359
Mystic, IA (52574)	664
Nashua, IA (50658)	2120
Nevada, IA (50201)	7004
New Albin, IA (52160)	703
Newell, IA (50568)	1133
Newhall, IA (52315)	1052
New Hampton, IA (50659)	4716
New Hartford, IA (50660)	1078
New London, IA (52645)	2679
New Sharon, IA (50207)	2163
Newton, IA (50208)	16122
New Vienna, IA (52065)	831
New Virginia, IA (50210)	1447
Nichols, IA (52766)	667
Nora Springs, IA (50458)	1733
North English, IA (52316)	1396
North Liberty, IA (52317)	12151
Northwood, IA (50459)	2575
Norwalk, IA (50211)	9475
Norway, IA (52318)	895
Ocheyedan, IA (51354)	926
Odebolt, IA (51458)	1310
Oelwein, IA (50662)	5479
Ogden, IA (50212)	2706
Okoboji, IA (51355)	898
Olin, IA (52320)	959
Ollie, IA (52576)	464
Onawa, IA (51040)	2819
Orange City, IA (51041)	5168
Orient, IA (50858)	701
Osage, IA (50461)	4708
Osceola, IA (50213)	5585
Oskaloosa, IA (52577)	11691
Ossian, IA (52161)	1243
Otley, IA (50214)	715
Ottumwa, IA (52501)	23442
Oxford, IA (52322)	2117
Oxford Junction, IA (52323)	704
Palo, IA (52324)	1575
Panora, IA (50216)	2424
Parkersburg, IA (50665)	2392
Parnell, IA (52325)	678
Paton, IA (50217)	485
Paullina, IA (51046)	1444
Pella, IA (50219)	11011
Peosta, IA (52068)	3394
Perry, IA (50220)	6920
Peterson, IA (51047)	576
Pierson, IA (51048)	494
Plainfield, IA (50666)	878
Pleasantville, IA (50225)	2451
Plymouth, IA (50464)	560
Pocahontas, IA (50574)	1870
Polk City, IA (50226)	3947
Pomeroy, IA (50575)	748
Postville, IA (52162)	2664
Prairie City, IA (50228)	2051
Prescott, IA (50859)	532
Preston, IA (52069)	1356
Primghar, IA (51245)	1143
Princeton, IA (52768)	1205
Prole, IA (50229)	936
Quasqueton, IA (52326)	461
Quimby, IA (51049)	456
Radcliffe, IA (50230)	938
Raymond, IA (50667)	700
Readlyn, IA (50668)	1059
Redfield, IA (50233)	1123
Reinbeck, IA (50669)	2101
Remsen, IA (51050)	2409
Rhodes, IA (50234)	456
Riceville, IA (50466)	1445
Richland, IA (52585)	810
Ridgeway, IA (52165)	884
Ringsted, IA (50578)	557
Riverside, IA (52327)	2591
Rockford, IA (50468)	1364
Rock Rapids, IA (51246)	2941
Rock Valley, IA (51247)	3891
Rockwell, IA (50469)	1375
Rockwell City, IA (50579)	2094
Roland, IA (50236)	1384
Rolfe, IA (50581)	807
Rowley, IA (52329)	717
Royal, IA (51357)	621
Rudd, IA (50471)	614
Runnells, IA (50237)	2642
Russell, IA (50238)	954
Ruthven, IA (51358)	1127
Ryan, IA (52330)	722
Sabula, IA (52070)	903
Sac City, IA (50583)	2356
Saint Ansgar, IA (50472)	1906
Saint Charles, IA (50240)	1990
Salem, IA (52649)	831
Salix, IA (51052)	845
Sanborn, IA (51248)	1563
Schaller, IA (51053)	1036
Schleswig, IA (51461)	1032
Scranton, IA (51462)	930
Sergeant Bluff, IA (51054)	4440
Seymour, IA (52590)	855
Sheffield, IA (50475)	1407
Sheldon, IA (51201)	5070
Shell Rock, IA (50670)	1784
Shellsburg, IA (52332)	1728
Durango, IA (52039)	1079
Sherrill, IA (52073)	1312
Sibley, IA (51249)	2996
Sigourney, IA (52591)	2444
Sioux Center, IA (51250)	5875
Sioux City, IA (51101)	367
Sioux City, IA (51103)	12587
Sioux City, IA (51104)	17252
Sioux City, IA (51105)	6486
Sioux City, IA (51106)	21521
Sioux City, IA (51108)	4731
Sioux City, IA (51109)	2525
Sioux Rapids, IA (50585)	991
Slater, IA (50244)	1579
Sloan, IA (51055)	1137
Solon, IA (52333)	5537
South English, IA (52335)	537
Spencer, IA (51301)	10717
Sperry, IA (52650)	752
Spirit Lake, IA (51360)	7173
Springville, IA (52336)	1995
Stacyville, IA (50476)	656
Stanhope, IA (50246)	609
Stanwood, IA (52337)	734
State Center, IA (50247)	1995
Steamboat Rock, IA (50672)	489
Stockport, IA (52651)	543
Stockton, IA (52769)	574
Storm Lake, IA (50588)	10128
Story City, IA (50248)	3788
Stratford, IA (50249)	1051
Strawberry Point, IA (52076)	1916
Stuart, IA (50250)	1868
Sully, IA (50251)	1230
Sumner, IA (50674)	3108
Sutherland, IA (51058)	891
Swea City, IA (50590)	753
Swisher, IA (52338)	2966
Tama, IA (52339)	3686
Templeton, IA (51463)	523
Terril, IA (51364)	626
Thompson, IA (50478)	694
Thornton, IA (50479)	546
Tiffin, IA (52340)	1820
Tipton, IA (52772)	4232
Titonka, IA (50480)	773
Toledo, IA (52342)	2656
Traer, IA (50675)	2001
Tripoli, IA (50676)	1654
Truro, IA (50257)	767
Union, IA (50258)	678
Urbana, IA (52345)	1219
Ute, IA (51060)	539
Vail, IA (51465)	674
Van Horne, IA (52346)	1007
Van Meter, IA (50261)	1855
Ventura, IA (50482)	791
Victor, IA (52347)	1262
Villisca, IA (50864)	1681
Vinton, IA (52349)	6095
Walcott, IA (52773)	2086
Walford, IA (52351)	1309
Walker, IA (52352)	1761
Wall Lake, IA (51466)	936
Wapello, IA (52653)	2893
Washington, IA (52353)	7601
Waterloo, IA (50701)	24230
Waterloo, IA (50702)	15833
Waterloo, IA (50703)	13807
Evansdale, IA (50707)	6546
Waucoma, IA (52171)	898
Waukee, IA (50263)	12093
Waukon, IA (52172)	5195
Waverly, IA (50677)	9167
Wayland, IA (52654)	1384
Webster City, IA (50595)	7601
Wellman, IA (52356)	2204
Wellsburg, IA (50680)	988
Wesley, IA (50483)	689
West Bend, IA (50597)	1186
West Branch, IA (52358)	3224
West Burlington, IA (52655)	3726
Westfield, IA (51062)	496
West Liberty, IA (52776)	4010
West Point, IA (52656)	2091
Westside, IA (51467)	553
West Union, IA (52175)	2895
Wever, IA (52658)	921
What Cheer, IA (50268)	776
Wheatland, IA (52777)	1131
Whiting, IA (51063)	915
Whittemore, IA (50598)	797
Williams, IA (50271)	540
Williamsburg, IA (52361)	4061
Wilton, IA (52778)	3454
Winfield, IA (52659)	1315
Winterset, IA (50273)	6575
Winthrop, IA (50682)	1296
Woodward, IA (50276)	1857
Worthington, IA (52078)	796
Wyoming, IA (52362)	831
Zearing, IA (50278)	697
Zwingle, IA (52079)	686
Adams, MN (55909)	1206
Adrian, MN (56110)	1666
Afton, MN (55001)	2750
Aitkin, MN (56431)	7072
Akeley, MN (56433)	1211
Albany, MN (56307)	4213
Albert Lea, MN (56007)	17858
Albertville, MN (55301)	8310
Alden, MN (56009)	1471
Alexandria, MN (56308)	20392
Altura, MN (55910)	1303
Amboy, MN (56010)	1041
Angora, MN (55703)	624
Britt, MN (55710)	1153
Annandale, MN (55302)	5958
Anoka, MN (55303)	39074
Andover, MN (55304)	40521
Appleton, MN (56208)	1764
Arlington, MN (55307)	2708
Ashby, MN (56309)	1080
Askov, MN (55704)	904
Atwater, MN (56209)	2092
Aurora, MN (55705)	2605
Austin, MN (55912)	23996
Avon, MN (56310)	4551
Babbitt, MN (55706)	1520
Backus, MN (56435)	1961
Bagley, MN (56621)	3543
Balaton, MN (56115)	1176
Barnum, MN (55707)	2707
Barrett, MN (56311)	590
Baudette, MN (56623)	2425
Bayport, MN (55003)	1707
Beaver Creek, MN (56116)	496
Becker, MN (55308)	7337
Belgrade, MN (56312)	1997
Belle Plaine, MN (56011)	7401
Bellingham, MN (56212)	490
Belview, MN (56214)	650
Bemidji, MN (56601)	22996
Benson, MN (56215)	3906
Bertha, MN (56437)	947
Bethel, MN (55005)	3718
Bigfork, MN (56628)	1246
Big Lake, MN (55309)	15038
Bird Island, MN (55310)	1371
Blackduck, MN (56630)	1927
Blomkest, MN (56216)	636
Blooming Prairie, MN (55917)	3275
Blue Earth, MN (56013)	3946
Bovey, MN (55709)	3212
Bowlus, MN (56314)	1053
Boyd, MN (56218)	509
Braham, MN (55006)	3121
Brainerd, MN (56401)	23511
Baxter, MN (56425)	6468
Brandon, MN (56315)	1355
Brewster, MN (56119)	917
Bricelyn, MN (56014)	697
Brook Park, MN (55007)	1954
Brooten, MN (56316)	1173
Browerville, MN (56438)	2416
Brownsdale, MN (55918)	889
Browns Valley, MN (56219)	881
Brownsville, MN (55919)	861
Brownton, MN (55312)	1419
Buffalo, MN (55313)	19513
Buffalo Lake, MN (55314)	1068
Burtrum, MN (56318)	1013
Butterfield, MN (56120)	898
Byron, MN (55920)	6356
Caledonia, MN (55921)	4193
Cambridge, MN (55008)	12059
Canby, MN (56220)	2568
Cannon Falls, MN (55009)	7157
Canton, MN (55922)	517
Carlos, MN (56319)	1175
Carlton, MN (55718)	2685
Carver, MN (55315)	3984
Cass Lake, MN (56633)	3423
Cedar, MN (55011)	9021
Center City, MN (55012)	1720
Ceylon, MN (56121)	554
Champlin, MN (55316)	20946
Chandler, MN (56122)	505
Chanhassen, MN (55317)	17368
Chaska, MN (55318)	21769
Chatfield, MN (55923)	3817
Chisago City, MN (55013)	5532
Chisholm, MN (55719)	4623
Chokio, MN (56221)	706
Circle Pines, MN (55014)	23573
Clara City, MN (56222)	1724
Claremont, MN (55924)	1176
Clarissa, MN (56440)	1002
Clarkfield, MN (56223)	1152
Clarks Grove, MN (56016)	923
Clearbrook, MN (56634)	1243
Clear Lake, MN (55319)	4530
Clearwater, MN (55320)	4200
Cleveland, MN (56017)	1457
Clinton, MN (56225)	668
Cloquet, MN (55720)	13288
Cohasset, MN (55721)	2857
Cokato, MN (55321)	4178
Cold Spring, MN (56320)	6910
Cologne, MN (55322)	2758
Comfrey, MN (56019)	806
Cook, MN (55723)	2093
Cosmos, MN (56228)	792
Cottage Grove, MN (55016)	29532
Cotton, MN (55724)	623
Cottonwood, MN (56229)	1668
Courtland, MN (56021)	953
Cromwell, MN (55726)	776
Crosby, MN (56441)	2583
Crosslake, MN (56442)	2252
Currie, MN (56123)	470
Cushing, MN (56443)	1224
Cyrus, MN (56323)	445
Dakota, MN (55925)	1005
Dalbo, MN (55017)	580
Dalton, MN (56324)	976
Danube, MN (56230)	737
Darwin, MN (55324)	1126
Dassel, MN (55325)	3752
Dawson, MN (56232)	1970
Dayton, MN (55327)	3210
Deer River, MN (56636)	3996
Deerwood, MN (56444)	2583
Delano, MN (55328)	7172
Delavan, MN (56023)	443
Dennison, MN (55018)	885
Dexter, MN (55926)	705
Dodge Center, MN (55927)	3423
Donnelly, MN (56235)	522
Dover, MN (55929)	1072
Duluth, MN (55802)	1619
Duluth, MN (55803)	15005
Duluth, MN (55804)	12686
Duluth, MN (55805)	5750
Duluth, MN (55806)	6599
Duluth, MN (55807)	7639
Duluth, MN (55808)	4429
Duluth, MN (55810)	7278
Duluth, MN (55811)	19664
Duluth, MN (55812)	5525
Dundas, MN (55019)	1610
Eagle Bend, MN (56446)	1336
Eagle Lake, MN (56024)	2391
Easton, MN (56025)	503
Echo, MN (56237)	534
Eden Valley, MN (55329)	1677
Edgerton, MN (56128)	1750
Elgin, MN (55932)	1853
Elk River, MN (55330)	31206
Ellendale, MN (56026)	1719
Ellsworth, MN (56129)	693
Elmore, MN (56027)	816
Ely, MN (55731)	4713
Elysian, MN (56028)	1164
Embarrass, MN (55732)	1224
Emily, MN (56447)	839
Emmons, MN (56029)	634
Esko, MN (55733)	4134
Evansville, MN (56326)	1258
Eveleth, MN (55734)	5240
Excelsior, MN (55331)	16166
Eyota, MN (55934)	3011
Fairfax, MN (55332)	1660
Fairmont, MN (56031)	10681
Faribault, MN (55021)	22884
Farmington, MN (55024)	26991
Finland, MN (55603)	433
Finlayson, MN (55735)	1404
Floodwood, MN (55736)	1241
Foley, MN (56329)	5983
Oak Park, MN (56357)	858
Forbes, MN (55738)	503
Forest Lake, MN (55025)	19742
Foreston, MN (56330)	1389
Fort Ripley, MN (56449)	1375
Fountain, MN (55935)	806
Franklin, MN (55333)	670
Freeport, MN (56331)	1816
Fulda, MN (56131)	2076
Garden City, MN (56034)	470
Garfield, MN (56332)	1209
Garrison, MN (56450)	880
Gaylord, MN (55334)	2581
Ghent, MN (56239)	561
Gibbon, MN (55335)	1395
Gilbert, MN (55741)	2722
Glencoe, MN (55336)	7168
Glenville, MN (56036)	1732
Glenwood, MN (56334)	4759
Gonvick, MN (56644)	665
Goodhue, MN (55027)	2544
Good Thunder, MN (56037)	1473
Graceville, MN (56240)	790
Granada, MN (56039)	912
Grand Marais, MN (55604)	3068
Grand Meadow, MN (55936)	1618
Grand Portage, MN (55605)	502
Grand Rapids, MN (55744)	16279
Granite Falls, MN (56241)	3594
Grasston, MN (55030)	1032
Green Isle, MN (55338)	1040
Grey Eagle, MN (56336)	1230
Grove City, MN (56243)	1436
Hackensack, MN (56452)	1729
Hamburg, MN (55339)	873
Hamel, MN (55340)	5637
Hampton, MN (55031)	1764
Hancock, MN (56244)	1299
Hanover, MN (55341)	2350
Hanska, MN (56041)	1020
Harmony, MN (55939)	1548
Harris, MN (55032)	3026
Hartland, MN (56042)	636
Hastings, MN (55033)	25103
Hayfield, MN (55940)	2199
Hayward, MN (56043)	463
Hector, MN (55342)	1739
Henderson, MN (56044)	1755
Hendricks, MN (56136)	1066
Herman, MN (56248)	722
Heron Lake, MN (56137)	1003
Hewitt, MN (56453)	699
Hibbing, MN (55746)	13817
Hill City, MN (55748)	1139
Hills, MN (56138)	796
Hinckley, MN (55037)	3823
Hines, MN (56647)	577
Hoffman, MN (56339)	916
Hokah, MN (55941)	922
Holdingford, MN (56340)	1868
Hollandale, MN (56045)	691
Hopkins, MN (55305)	17425
Hopkins, MN (55343)	20423
Eden Prairie, MN (55344)	11838
Minnetonka, MN (55345)	19697
Eden Prairie, MN (55346)	15754
Eden Prairie, MN (55347)	27496
Houston, MN (55943)	2607
Howard Lake, MN (55349)	3293
Hoyt Lakes, MN (55750)	1654
Hugo, MN (55038)	17873
Hutchinson, MN (55350)	15663
International Falls, MN (56649)	7765
Iron, MN (55751)	1267
Ironton, MN (56455)	1358
Isanti, MN (55040)	10429
Isle, MN (56342)	2498
Ivanhoe, MN (56142)	845
Jackson, MN (56143)	3887
Janesville, MN (56048)	3340
Jasper, MN (56144)	1065
Jeffers, MN (56145)	540
Jordan, MN (55352)	7551
Kandiyohi, MN (56251)	851
Kasota, MN (56050)	1311
Kasson, MN (55944)	5978
Kelliher, MN (56650)	571
Kellogg, MN (55945)	1297
Kensington, MN (56343)	806
Kenyon, MN (55946)	2773
Kerkhoven, MN (56252)	1099
Kettle River, MN (55757)	662
Kiester, MN (56051)	647
Kilkenny, MN (56052)	674
Kimball, MN (55353)	2639
La Crescent, MN (55947)	6757
Lafayette, MN (56054)	835
Lake Benton, MN (56149)	1056
Lake City, MN (55041)	6678
Lake Crystal, MN (56055)	3399
Lake Elmo, MN (55042)	7753
Lakefield, MN (56150)	2490
Lakeland, MN (55043)	3295
Lake Lillian, MN (56253)	900
Lakeville, MN (55044)	41090
Lake Wilson, MN (56151)	735
Lamberton, MN (56152)	1198
Lanesboro, MN (55949)	1598
Laporte, MN (56461)	2368
Le Center, MN (56057)	3405
Le Roy, MN (55951)	1315
Lester Prairie, MN (55354)	2390
Le Sueur, MN (56058)	5346
Lewiston, MN (55952)	2291
Lindstrom, MN (55045)	6536
Litchfield, MN (55355)	8039
Little Falls, MN (56345)	12016
Littlefork, MN (56653)	1087
Long Lake, MN (55356)	4768
Long Prairie, MN (56347)	5290
Longville, MN (56655)	1276
Lonsdale, MN (55046)	4254
Loretto, MN (55357)	2847
Farwell, MN (56327)	674
Lowry, MN (56349)	664
Lutsen, MN (55612)	455
Luverne, MN (56156)	5162
Lyle, MN (55953)	793
Lynd, MN (56157)	638
Mcgregor, MN (55760)	2224
Mabel, MN (55954)	1204
Madelia, MN (56062)	2661
Madison, MN (56256)	2338
Madison Lake, MN (56063)	2375
Makinen, MN (55763)	469
Mankato, MN (56001)	30746
Mankato, MN (56003)	12372
Mantorville, MN (55955)	2451
Maple Lake, MN (55358)	4409
Maple Plain, MN (55359)	5484
Mapleton, MN (56065)	2377
Marietta, MN (56257)	438
Marine On Saint Croix, MN (55047)	2345
Marshall, MN (56258)	12055
Mayer, MN (55360)	2244
Maynard, MN (56260)	824
Mazeppa, MN (55956)	1676
Meadowlands, MN (55765)	626
Medford, MN (55049)	2182
Melrose, MN (56352)	4670
Menahga, MN (56464)	3225
Merrifield, MN (56465)	1878
Milaca, MN (56353)	7245
Milan, MN (56262)	605
Millville, MN (55957)	659
Milroy, MN (56263)	490
Miltona, MN (56354)	1149
Minneapolis, MN (55401)	5440
Minneapolis, MN (55402)	1200
Minneapolis, MN (55403)	10370
Minneapolis, MN (55404)	14905
Minneapolis, MN (55405)	11100
Minneapolis, MN (55406)	26993
Minneapolis, MN (55407)	26247
Minneapolis, MN (55408)	20917
Minneapolis, MN (55409)	9201
Minneapolis, MN (55410)	17170
Minneapolis, MN (55411)	16898
Minneapolis, MN (55412)	15286
Minneapolis, MN (55413)	8673
Minneapolis, MN (55414)	10417
Minneapolis, MN (55415)	1196
Minneapolis, MN (55416)	24658
Minneapolis, MN (55417)	20872
Minneapolis, MN (55418)	24247
Minneapolis, MN (55419)	22317
Minneapolis, MN (55420)	18534
Minneapolis, MN (55421)	21176
Minneapolis, MN (55422)	24243
Minneapolis, MN (55423)	29761
Minneapolis, MN (55424)	8774
Minneapolis, MN (55425)	7168
Minneapolis, MN (55426)	20614
Minneapolis, MN (55427)	20132
Minneapolis, MN (55428)	23451
Minneapolis, MN (55429)	21083
Minneapolis, MN (55430)	16574
Minneapolis, MN (55431)	16251
Minneapolis, MN (55432)	24668
Minneapolis, MN (55433)	27980
Minneapolis, MN (55434)	24721
Minneapolis, MN (55435)	9825
Minneapolis, MN (55436)	12140
Minneapolis, MN (55437)	15947
Minneapolis, MN (55438)	15427
Minneapolis, MN (55439)	8279
Minneapolis, MN (55441)	15526
Minneapolis, MN (55442)	12403
Minneapolis, MN (55443)	27809
Minneapolis, MN (55444)	13638
Minneapolis, MN (55445)	8177
Minneapolis, MN (55446)	16542
Minneapolis, MN (55447)	18811
Minneapolis, MN (55448)	24634
Minneapolis, MN (55449)	19845
Minneapolis, MN (55454)	4068
Minneota, MN (56264)	1825
Minnesota City, MN (55959)	1894
Minnesota Lake, MN (56068)	959
Montevideo, MN (56265)	6866
Montgomery, MN (56069)	3792
Monticello, MN (55362)	14937
Montrose, MN (55363)	3602
Moose Lake, MN (55767)	2787
Mora, MN (55051)	7688
Morgan, MN (56266)	1357
Morris, MN (56267)	4786
Morristown, MN (55052)	1695
Morton, MN (56270)	1035
Motley, MN (56466)	2480
Mound, MN (55364)	12656
Mountain Iron, MN (55768)	2442
Mountain Lake, MN (56159)	2247
Murdock, MN (56271)	1060
Nashwauk, MN (55769)	1884
Nelson, MN (56355)	518
Nerstrand, MN (55053)	903
Nevis, MN (56467)	1995
New Germany, MN (55367)	831
New London, MN (56273)	4234
Elko New Market, MN (55020)	3023
Elko New Market, MN (55054)	1662
Newport, MN (55055)	2742
New Prague, MN (56071)	9948
New Richland, MN (56072)	2071
New Ulm, MN (56073)	14611
Nicollet, MN (56074)	1798
Nisswa, MN (56468)	4012
North Branch, MN (55056)	11285
Northfield, MN (55057)	17172
Northome, MN (56661)	706
Ogilvie, MN (56358)	2594
Olivia, MN (56277)	2788
Onamia, MN (56359)	2684
Oronoco, MN (55960)	2676
Orr, MN (55771)	1308
Ortonville, MN (56278)	2209
Osakis, MN (56360)	3196
Osseo, MN (55311)	28970
Osseo, MN (55369)	29961
Outing, MN (56662)	472
Owatonna, MN (55060)	25176
Palisade, MN (56469)	837
Parkers Prairie, MN (56361)	2040
Park Rapids, MN (56470)	8476
Paynesville, MN (56362)	5003
Pengilly, MN (55775)	1086
Pennock, MN (56279)	1087
Pequot Lakes, MN (56472)	6122
Peterson, MN (55962)	678
Hillman, MN (56338)	1431
Pierz, MN (56364)	4188
Pillager, MN (56473)	2795
Pine City, MN (55063)	7226
Pine Island, MN (55963)	4522
Pine River, MN (56474)	3464
Pipestone, MN (56164)	4934
Plainview, MN (55964)	3935
Plato, MN (55370)	685
Porter, MN (56280)	454
Preston, MN (55965)	2036
Princeton, MN (55371)	13602
Prinsburg, MN (56281)	559
Prior Lake, MN (55372)	26347
Puposky, MN (56667)	541
Racine, MN (55967)	804
Randall, MN (56475)	1386
Randolph, MN (55065)	974
Raymond, MN (56282)	1381
Red Wing, MN (55066)	15965
Redwood Falls, MN (56283)	5710
Remer, MN (56672)	1532
Renville, MN (56284)	1784
Rice, MN (56367)	5831
Richmond, MN (56368)	3685
Rochester, MN (55901)	43714
Rochester, MN (55902)	19541
Rochester, MN (55904)	20555
Rochester, MN (55906)	15543
Rockford, MN (55373)	4831
Rogers, MN (55374)	11547
Rollingstone, MN (55969)	968
Roosevelt, MN (56673)	597
Rose Creek, MN (55970)	839
Rosemount, MN (55068)	24049
Round Lake, MN (56167)	600
Royalton, MN (56373)	2615
Rush City, MN (55069)	3881
Rushford, MN (55971)	2598
Rushmore, MN (56168)	868
Russell, MN (56169)	611
Ruthton, MN (56170)	522
Sacred Heart, MN (56285)	1002
Saginaw, MN (55779)	3187
Saint Bonifacius, MN (55375)	3264
Saint Charles, MN (55972)	4295
Saint Cloud, MN (56301)	21226
Saint Cloud, MN (56303)	20644
Saint Cloud, MN (56304)	10660
Sauk Rapids, MN (56379)	13530
Waite Park, MN (56387)	5111
Saint Francis, MN (55070)	6077
Saint James, MN (56081)	5050
Saint Joseph, MN (56374)	6660
Saint Stephen, MN (56375)	716
Saint Michael, MN (55376)	13761
Saint Paul, MN (55101)	4516
Saint Paul, MN (55102)	12963
Saint Paul, MN (55103)	8535
Saint Paul, MN (55104)	30008
Saint Paul, MN (55105)	21132
Saint Paul, MN (55106)	36448
Saint Paul, MN (55107)	10102
Saint Paul, MN (55108)	11086
Saint Paul, MN (55109)	26675
Saint Paul, MN (55110)	34155
Saint Paul, MN (55112)	35657
Saint Paul, MN (55113)	32692
Saint Paul, MN (55114)	1902
Saint Paul, MN (55115)	7825
Saint Paul, MN (55116)	19601
Saint Paul, MN (55117)	30600
Saint Paul, MN (55118)	23819
Saint Paul, MN (55119)	31051
Saint Paul, MN (55120)	4135
Saint Paul, MN (55121)	7016
Saint Paul, MN (55122)	27501
Saint Paul, MN (55123)	23478
Saint Paul, MN (55124)	44823
Saint Paul, MN (55125)	38570
Saint Paul, MN (55126)	23739
Saint Paul, MN (55127)	15796
Saint Paul, MN (55128)	24584
Saint Paul, MN (55129)	15319
Saint Paul, MN (55130)	10092
Saint Paul Park, MN (55071)	4596
Saint Peter, MN (56082)	9388
Sanborn, MN (56083)	816
Sandstone, MN (55072)	2569
Sartell, MN (56377)	14443
Sauk Centre, MN (56378)	6587
Burnsville, MN (55306)	13644
Burnsville, MN (55337)	38193
Savage, MN (55378)	22994
Scandia, MN (55073)	2930
Sebeka, MN (56477)	2045
Shafer, MN (55074)	1792
Shakopee, MN (55379)	33688
Sherburn, MN (56171)	1528
Shevlin, MN (56676)	1366
Side Lake, MN (55781)	634
Silver Bay, MN (55614)	2081
Silver Lake, MN (55381)	1774
Slayton, MN (56172)	2697
Sleepy Eye, MN (56085)	4879
Solway, MN (56678)	1010
South Haven, MN (55382)	3166
South Saint Paul, MN (55075)	16581
Inver Grove Heights, MN (55076)	18797
Inver Grove Heights, MN (55077)	10368
Spicer, MN (56288)	4226
Springfield, MN (56087)	2758
Spring Grove, MN (55974)	1777
Spring Park, MN (55384)	1265
Spring Valley, MN (55975)	3746
Stacy, MN (55079)	7283
Stanchfield, MN (55080)	2313
Staples, MN (56479)	4060
Starbuck, MN (56381)	2111
Stewart, MN (55385)	1210
Stewartville, MN (55976)	6530
Stillwater, MN (55082)	30430
Sturgeon Lake, MN (55783)	1883
Sunburg, MN (56289)	603
Swanville, MN (56382)	1249
Taylors Falls, MN (55084)	1470
Tenstrike, MN (56683)	566
Tower, MN (55790)	1649
Garvin, MN (56132)	477
Tracy, MN (56175)	2593
Trimont, MN (56176)	1006
Truman, MN (56088)	1744
Two Harbors, MN (55616)	5913
Tyler, MN (56178)	1502
Utica, MN (55979)	786
Verndale, MN (56481)	1674
Vernon Center, MN (56090)	557
Vesta, MN (56292)	572
Victoria, MN (55386)	5345
Villard, MN (56385)	820
Virginia, MN (55792)	7808
Wabasha, MN (55981)	3469
Wabasso, MN (56293)	1080
Waconia, MN (55387)	10340
Wadena, MN (56482)	5246
Wahkon, MN (56386)	533
Walker, MN (56484)	3282
Walnut Grove, MN (56180)	1093
Wanamingo, MN (55983)	1256
Warba, MN (55793)	476
Waseca, MN (56093)	10276
Watertown, MN (55388)	4556
Waterville, MN (56096)	2614
Watkins, MN (55389)	2199
Waverly, MN (55390)	2133
Wayzata, MN (55391)	13306
Webster, MN (55088)	1582
Welch, MN (55089)	1631
Welcome, MN (56181)	1015
Wells, MN (56097)	3220
Westbrook, MN (56183)	1093
West Concord, MN (55985)	1618
Wheaton, MN (56296)	1763
Williams, MN (56686)	812
Willmar, MN (56201)	18474
Willow River, MN (55795)	1113
Wilmont, MN (56185)	511
Windom, MN (56101)	4947
Winnebago, MN (56098)	1824
Winona, MN (55987)	24430
Winsted, MN (55395)	2521
Winthrop, MN (55396)	1889
Wood Lake, MN (56297)	787
Worthington, MN (56187)	10806
Wrenshall, MN (55797)	1280
Wright, MN (55798)	492
Wykoff, MN (55990)	796
Wyoming, MN (55092)	9399
Norwood Young America, MN (55368)	1961
Young America, MN (55397)	2352
Zimmerman, MN (55398)	12919
Zumbro Falls, MN (55991)	1241
Zumbrota, MN (55992)	4154
Alma, WI (54610)	1506
Alma Center, WI (54611)	1120
Almena, WI (54805)	1276
Altoona, WI (54720)	5898
Amery, WI (54001)	6953
Arcadia, WI (54612)	4707
Arkansaw, WI (54721)	1164
Arkdale, WI (54613)	1475
Ashland, WI (54806)	9183
Augusta, WI (54722)	2953
Baldwin, WI (54002)	5276
Balsam Lake, WI (54810)	2123
Bangor, WI (54614)	2479
Barron, WI (54812)	4756
Barronett, WI (54813)	570
Bay City, WI (54723)	1066
Bayfield, WI (54814)	2122
Beldenville, WI (54003)	902
Birchwood, WI (54817)	2013
Black River Falls, WI (54615)	8455
Blair, WI (54616)	1995
Bloomer, WI (54724)	6192
Boyceville, WI (54725)	2437
Boyd, WI (54726)	1477
Bruce, WI (54819)	2050
Brule, WI (54820)	727
Cable, WI (54821)	1229
Cadott, WI (54727)	4126
Cameron, WI (54822)	3836
Camp Douglas, WI (54618)	1963
Cashton, WI (54619)	2686
Centuria, WI (54824)	1788
Chaseburg, WI (54621)	952
Chetek, WI (54728)	5213
Chippewa Falls, WI (54729)	26758
Clayton, WI (54004)	1909
Clear Lake, WI (54005)	2671
Cochrane, WI (54622)	1887
Colfax, WI (54730)	4266
Comstock, WI (54826)	623
Conrath, WI (54731)	552
Coon Valley, WI (54623)	1754
Cornell, WI (54732)	2326
Couderay, WI (54828)	511
Cumberland, WI (54829)	4649
Cushing, WI (54006)	695
Dallas, WI (54733)	1149
Danbury, WI (54830)	2464
Deer Park, WI (54007)	1095
De Soto, WI (54624)	1157
Downing, WI (54734)	703
Dresser, WI (54009)	2097
Durand, WI (54736)	3586
Eastman, WI (54626)	1080
Eau Claire, WI (54701)	28813
Eau Claire, WI (54703)	32547
Eleva, WI (54738)	3015
Elk Mound, WI (54739)	4161
Ellsworth, WI (54011)	5757
Elmwood, WI (54740)	1735
Ettrick, WI (54627)	1793
Exeland, WI (54835)	852
Fairchild, WI (54741)	1236
Fall Creek, WI (54742)	4070
Ferryville, WI (54628)	957
Fountain City, WI (54629)	2318
Frederic, WI (54837)	3103
Galesville, WI (54630)	3387
Gays Mills, WI (54631)	1460
Genoa, WI (54632)	1031
Glenwood City, WI (54013)	2984
Gordon, WI (54838)	945
Grantsburg, WI (54840)	4046
Hager City, WI (54014)	2071
Hammond, WI (54015)	2937
Hayward, WI (54843)	10035
High Bridge, WI (54846)	470
Marengo, WI (54855)	593
Hillsboro, WI (54634)	2969
Hixton, WI (54635)	1514
Holcombe, WI (54745)	1892
Holmen, WI (54636)	11872
Hudson, WI (54016)	26369
Houlton, WI (54082)	1355
Humbird, WI (54746)	620
Independence, WI (54747)	2318
Iron River, WI (54847)	2067
Jim Falls, WI (54748)	1123
Kendall, WI (54638)	1269
Knapp, WI (54749)	1026
La Crosse, WI (54601)	33522
La Crosse, WI (54603)	11465
Ladysmith, WI (54848)	4949
La Farge, WI (54639)	1639
Lake Nebagamon, WI (54849)	1725
Luck, WI (54853)	3266
Maiden Rock, WI (54750)	978
Maple, WI (54854)	771
Mason, WI (54856)	1336
Melrose, WI (54642)	1699
Menomonie, WI (54751)	16951
Merrillan, WI (54754)	1334
Milltown, WI (54858)	1224
Mindoro, WI (54644)	1288
Minong, WI (54859)	1706
Mondovi, WI (54755)	5799
Necedah, WI (54646)	3100
Nelson, WI (54756)	829
New Auburn, WI (54757)	2688
New Richmond, WI (54017)	14245
Norwalk, WI (54648)	1436
Onalaska, WI (54650)	20299
Ontario, WI (54651)	948
Osceola, WI (54020)	6332
Osseo, WI (54758)	3865
Pepin, WI (54759)	1247
Plum City, WI (54761)	1039
Poplar, WI (54864)	1266
Prairie Farm, WI (54762)	1052
Prescott, WI (54021)	5542
Readstown, WI (54652)	724
Rice Lake, WI (54868)	12887
Ridgeland, WI (54763)	922
River Falls, WI (54022)	15377
Roberts, WI (54023)	3441
Rockland, WI (54653)	883
Saint Croix Falls, WI (54024)	4275
Sarona, WI (54870)	1339
Sheldon, WI (54766)	1277
Shell Lake, WI (54871)	2668
Siren, WI (54872)	2172
Soldiers Grove, WI (54655)	1409
Solon Springs, WI (54873)	2447
Somerset, WI (54025)	5883
South Range, WI (54874)	2947
Sparta, WI (54656)	14730
Spooner, WI (54801)	5608
Springbrook, WI (54875)	876
Spring Valley, WI (54767)	2755
Stanley, WI (54768)	3469
Star Prairie, WI (54026)	1618
Stockholm, WI (54769)	452
Stoddard, WI (54658)	2206
Stone Lake, WI (54876)	1439
Strum, WI (54770)	1910
Foxboro, WI (54836)	936
Superior, WI (54880)	23716
Taylor, WI (54659)	1000
Thorp, WI (54771)	3169
Tomah, WI (54660)	13215
Trego, WI (54888)	1294
Trempealeau, WI (54661)	2961
Turtle Lake, WI (54889)	2388
Viola, WI (54664)	1254
Viroqua, WI (54665)	6813
Warrens, WI (54666)	2075
Washburn, WI (54891)	2834
Webster, WI (54893)	3218
Westby, WI (54667)	3846
West Salem, WI (54669)	6713
Weyerhaeuser, WI (54895)	822
Wheeler, WI (54772)	934
Whitehall, WI (54773)	2695
Wilson, WI (54027)	890
Wilton, WI (54670)	1150
Winter, WI (54896)	1313
Woodville, WI (54028)	2151
Ada, MN (56510)	1974
Argyle, MN (56713)	896
Audubon, MN (56511)	1596
Badger, MN (56714)	1052
Barnesville, MN (56514)	3111
Battle Lake, MN (56515)	2586
Breckenridge, MN (56520)	3351
Callaway, MN (56521)	620
Campbell, MN (56522)	522
Clitherall, MN (56524)	640
Crookston, MN (56716)	7173
Deer Creek, MN (56527)	721
Dent, MN (56528)	1391
Detroit Lakes, MN (56501)	12936
Rochert, MN (56578)	741
Dilworth, MN (56529)	3289
East Grand Forks, MN (56721)	8479
Elbow Lake, MN (56531)	1734
Erhard, MN (56534)	1038
Erskine, MN (56535)	1036
Fergus Falls, MN (56537)	15712
Fertile, MN (56540)	1566
Fisher, MN (56723)	860
Fosston, MN (56542)	2314
Frazee, MN (56544)	4195
Gary, MN (56545)	614
Glyndon, MN (56547)	2318
Goodridge, MN (56725)	846
Greenbush, MN (56726)	1368
Grygla, MN (56727)	653
Hallock, MN (56728)	1247
Halstad, MN (56548)	573
Hawley, MN (56549)	3869
Henning, MN (56551)	1748
Karlstad, MN (56732)	926
Lake Park, MN (56554)	2238
Lancaster, MN (56735)	679
Mcintosh, MN (56556)	895
Mahnomen, MN (56557)	2240
Mentor, MN (56736)	785
Middle River, MN (56737)	735
Moorhead, MN (56560)	28610
Newfolden, MN (56738)	1143
New York Mills, MN (56567)	2703
Ogema, MN (56569)	981
Oklee, MN (56742)	685
Osage, MN (56570)	1045
Oslo, MN (56744)	536
Ottertail, MN (56571)	1526
Pelican Rapids, MN (56572)	4703
Perham, MN (56573)	5226
Plummer, MN (56748)	502
Ponsford, MN (56575)	508
Red Lake Falls, MN (56750)	2183
Richville, MN (56576)	764
Roseau, MN (56751)	5002
Rothsay, MN (56579)	1013
Sabin, MN (56580)	1017
Stephen, MN (56757)	816
Thief River Falls, MN (56701)	10548
Twin Valley, MN (56584)	1134
Ulen, MN (56585)	849
Underwood, MN (56586)	1644
Vergas, MN (56587)	1322
Vining, MN (56588)	471
Warren, MN (56762)	2182
Salol, MN (56756)	663
Warroad, MN (56763)	4566
Waubun, MN (56589)	1423
Absarokee, MT (59001)	1377
Alberton, MT (59820)	1016
Anaconda, MT (59711)	7043
Arlee, MT (59821)	1727
Ashland, MT (59003)	861
Baker, MT (59313)	2241
Ballantine, MT (59006)	723
Belgrade, MT (59714)	15060
Belt, MT (59412)	1409
Bigfork, MT (59911)	6546
Big Sandy, MT (59520)	897
Big Timber, MT (59011)	2695
Billings, MT (59101)	28978
Billings, MT (59102)	38624
Billings, MT (59105)	24609
Billings, MT (59106)	10738
Bonner, MT (59823)	1342
Boulder, MT (59632)	1466
Box Elder, MT (59521)	1946
Bozeman, MT (59715)	22298
Bozeman, MT (59718)	20160
Bridger, MT (59014)	1195
Broadus, MT (59317)	964
Broadview, MT (59015)	462
Browning, MT (59417)	5105
Busby, MT (59016)	519
Butte, MT (59701)	24796
Cascade, MT (59421)	1573
Charlo, MT (59824)	1199
Chester, MT (59522)	1222
Chinook, MT (59523)	1854
Choteau, MT (59422)	2321
Circle, MT (59215)	945
Clancy, MT (59634)	4267
Clinton, MT (59825)	1818
Columbia Falls, MT (59912)	11120
Columbus, MT (59019)	3449
Condon, MT (59826)	467
Conrad, MT (59425)	3038
Corvallis, MT (59828)	4610
Crow Agency, MT (59022)	2070
Culbertson, MT (59218)	882
Cut Bank, MT (59427)	3875
Darby, MT (59829)	1938
Deer Lodge, MT (59722)	3647
Dillon, MT (59725)	6199
Drummond, MT (59832)	649
Dutton, MT (59433)	522
East Helena, MT (59635)	6442
Ekalaka, MT (59324)	635
Emigrant, MT (59027)	769
Ennis, MT (59729)	1943
Eureka, MT (59917)	3387
Fairfield, MT (59436)	1586
Fairview, MT (59221)	1372
Florence, MT (59833)	4657
Forsyth, MT (59327)	2368
Fort Benton, MT (59442)	1618
Fort Shaw, MT (59443)	545
Frenchtown, MT (59834)	2185
Huson, MT (59846)	1173
Fromberg, MT (59029)	585
Gallatin Gateway, MT (59730)	1407
Gardiner, MT (59030)	1136
Glasgow, MT (59230)	3923
Glendive, MT (59330)	6781
Great Falls, MT (59401)	10188
Great Falls, MT (59404)	22082
Great Falls, MT (59405)	24840
Black Eagle, MT (59414)	961
Hamilton, MT (59840)	10754
Hardin, MT (59034)	3466
Harlem, MT (59526)	1851
Havre, MT (59501)	10582
Helena, MT (59601)	22488
Helena, MT (59602)	18953
Hot Springs, MT (59845)	748
Huntley, MT (59037)	1477
Hysham, MT (59038)	544
Joliet, MT (59041)	1638
Jordan, MT (59337)	657
Kalispell, MT (59901)	36386
Kila, MT (59920)	1260
Lakeside, MT (59922)	1970
Laurel, MT (59044)	9257
Lewistown, MT (59457)	7742
Libby, MT (59923)	7500
Lincoln, MT (59639)	1032
Livingston, MT (59047)	9854
Lodge Grass, MT (59050)	1373
Lolo, MT (59847)	4885
Malta, MT (59538)	2525
Manhattan, MT (59741)	3783
Marion, MT (59925)	989
Miles City, MT (59301)	9163
Missoula, MT (59801)	20255
Missoula, MT (59802)	13113
Missoula, MT (59803)	13346
Missoula, MT (59804)	6052
Missoula, MT (59808)	14352
Molt, MT (59057)	588
Nashua, MT (59248)	589
Noxon, MT (59853)	599
Park City, MT (59063)	1650
Philipsburg, MT (59858)	1141
Plains, MT (59859)	2530
Plentywood, MT (59254)	1830
Polson, MT (59860)	8213
Poplar, MT (59255)	2328
Power, MT (59468)	500
Red Lodge, MT (59068)	3039
Reed Point, MT (59069)	467
Rexford, MT (59930)	533
Roberts, MT (59070)	863
Ronan, MT (59864)	4641
Roundup, MT (59072)	3141
Ryegate, MT (59074)	445
Saint Ignatius, MT (59865)	2321
Saint Regis, MT (59866)	717
Sand Coulee, MT (59472)	659
Savage, MT (59262)	521
Scobey, MT (59263)	1189
Seeley Lake, MT (59868)	1732
Shelby, MT (59474)	2630
Shepherd, MT (59079)	2772
Sheridan, MT (59749)	1347
Sidney, MT (59270)	6477
Somers, MT (59932)	1231
Stanford, MT (59479)	709
Stevensville, MT (59870)	7895
Sunburst, MT (59482)	587
Sun River, MT (59483)	550
Superior, MT (59872)	1813
Terry, MT (59349)	752
Thompson Falls, MT (59873)	2560
Three Forks, MT (59752)	2945
Townsend, MT (59644)	3219
Trout Creek, MT (59874)	1178
Troy, MT (59935)	2615
Twin Bridges, MT (59754)	797
Valier, MT (59486)	1144
Vaughn, MT (59487)	974
Victor, MT (59875)	2927
West Yellowstone, MT (59758)	1671
Whitefish, MT (59937)	10876
Whitehall, MT (59759)	2980
White Sulphur Springs, MT (59645)	1205
Wibaux, MT (59353)	784
Wilsall, MT (59086)	630
Wolf Creek, MT (59648)	559
Wolf Point, MT (59201)	3609
Worden, MT (59088)	1048
Ashley, ND (58413)	987
Baldwin, ND (58521)	558
Beach, ND (58621)	1119
Belcourt, ND (58316)	4500
Belfield, ND (58622)	1382
Berthold, ND (58718)	882
Beulah, ND (58523)	3203
Bismarck, ND (58501)	22915
Bismarck, ND (58503)	21583
Bismarck, ND (58504)	19832
Bottineau, ND (58318)	3196
Bowbells, ND (58721)	472
Bowman, ND (58623)	2072
Burlington, ND (58722)	1337
Buxton, ND (58218)	655
Cando, ND (58324)	1196
Carrington, ND (58421)	2471
Carson, ND (58529)	521
Casselton, ND (58012)	2157
Cavalier, ND (58220)	2081
Center, ND (58530)	1058
Cooperstown, ND (58425)	1256
Crosby, ND (58730)	1095
Devils Lake, ND (58301)	8122
Dickinson, ND (58601)	16638
Drayton, ND (58225)	1004
Dunseith, ND (58329)	2052
Edgeley, ND (58433)	957
Edinburg, ND (58227)	474
Elgin, ND (58533)	772
Ellendale, ND (58436)	1494
Emerado, ND (58228)	781
Enderlin, ND (58027)	1158
Fairmount, ND (58030)	638
Fargo, ND (58102)	21874
Fargo, ND (58103)	36270
Fargo, ND (58104)	22549
Fessenden, ND (58438)	614
Finley, ND (58230)	606
Flasher, ND (58535)	468
Forman, ND (58032)	577
Fort Yates, ND (58538)	1600
Garrison, ND (58540)	1943
Glenburn, ND (58740)	669
Glen Ullin, ND (58631)	956
Grafton, ND (58237)	4532
Grand Forks, ND (58201)	28120
Grand Forks, ND (58203)	11071
Grand Forks Afb, ND (58204)	1605
Granville, ND (58741)	486
Gwinner, ND (58040)	865
Halliday, ND (58636)	499
Hankinson, ND (58041)	1367
Harvey, ND (58341)	2255
Argusville, ND (58005)	643
Harwood, ND (58042)	1237
Hatton, ND (58240)	1040
Hazen, ND (58545)	3178
Hebron, ND (58638)	844
Hettinger, ND (58639)	1674
Hillsboro, ND (58045)	1883
Hoople, ND (58243)	506
Hope, ND (58046)	501
Horace, ND (58047)	3100
Jamestown, ND (58401)	13269
Kenmare, ND (58746)	1453
Killdeer, ND (58640)	1121
Kindred, ND (58051)	1313
Kulm, ND (58456)	471
Lakota, ND (58344)	895
Lamoure, ND (58458)	1039
Langdon, ND (58249)	2345
Larimore, ND (58251)	1765
Leeds, ND (58346)	579
Leonard, ND (58052)	521
Lidgerwood, ND (58053)	1049
Linton, ND (58552)	1498
Lisbon, ND (58054)	2757
Mcclusky, ND (58463)	565
Mcville, ND (58254)	447
Maddock, ND (58348)	687
Mandan, ND (58554)	19270
Manvel, ND (58256)	786
Mapleton, ND (58059)	1078
Max, ND (58759)	669
Mayville, ND (58257)	1638
Medina, ND (58467)	500
Menoken, ND (58558)	697
Michigan, ND (58259)	417
Milnor, ND (58060)	1098
Minot, ND (58701)	22685
Minot, ND (58703)	15365
Minot Afb, ND (58704)	3198
Minot Afb, ND (58705)	788
Minto, ND (58261)	955
Mohall, ND (58761)	945
Mott, ND (58646)	970
Napoleon, ND (58561)	868
Neche, ND (58265)	456
New England, ND (58647)	908
New Rockford, ND (58356)	1409
New Salem, ND (58563)	1722
New Town, ND (58763)	2581
Northwood, ND (58267)	1250
Oakes, ND (58474)	2257
Park River, ND (58270)	1635
Parshall, ND (58770)	955
Pembina, ND (58271)	725
Portland, ND (58274)	866
Powers Lake, ND (58773)	608
Ray, ND (58849)	725
Reynolds, ND (58275)	719
Richardton, ND (58652)	852
Rolette, ND (58366)	820
Rolla, ND (58367)	1619
Rugby, ND (58368)	3060
Saint John, ND (58369)	653
Saint Michael, ND (58370)	783
Saint Thomas, ND (58276)	477
Sawyer, ND (58781)	602
Scranton, ND (58653)	510
Sheyenne, ND (58374)	440
South Heart, ND (58655)	466
Stanley, ND (58784)	1543
Stanton, ND (58571)	516
Steele, ND (58482)	834
Strasburg, ND (58573)	486
Surrey, ND (58785)	986
Thompson, ND (58278)	1803
Tioga, ND (58852)	1433
Towner, ND (58788)	954
Turtle Lake, ND (58575)	779
Underwood, ND (58576)	765
Valley City, ND (58072)	6422
Velva, ND (58790)	1386
Wahpeton, ND (58075)	6699
Walcott, ND (58077)	685
Walhalla, ND (58282)	1224
Washburn, ND (58577)	1536
Watford City, ND (58854)	2375
West Fargo, ND (58078)	22386
Westhope, ND (58793)	572
Williston, ND (58801)	13634
Willow City, ND (58384)	511
Wilton, ND (58579)	1033
Wishek, ND (58495)	1118
Wyndmere, ND (58081)	764
Aberdeen, SD (57401)	23965
Alcester, SD (57001)	1348
Alexandria, SD (57311)	1081
Arlington, SD (57212)	1737
Armour, SD (57313)	976
Artesian, SD (57314)	545
Aurora, SD (57002)	800
Avon, SD (57315)	883
Baltic, SD (57003)	1632
Bath, SD (57427)	558
Belle Fourche, SD (57717)	6476
Beresford, SD (57004)	3001
Big Stone City, SD (57216)	996
Black Hawk, SD (57718)	5845
Bowdle, SD (57428)	553
Ellsworth Afb, SD (57706)	2237
Box Elder, SD (57719)	4929
Brandon, SD (57005)	9235
Bridgewater, SD (57319)	864
Bristol, SD (57219)	450
Britton, SD (57430)	1868
Brookings, SD (57006)	15382
Bruce, SD (57220)	725
Bryant, SD (57221)	573
Buffalo, SD (57720)	591
Burke, SD (57523)	912
Canistota, SD (57012)	962
Canton, SD (57013)	3832
Castlewood, SD (57223)	1092
Centerville, SD (57014)	1320
Chamberlain, SD (57325)	2752
Chancellor, SD (57015)	741
Chester, SD (57016)	614
Clark, SD (57225)	1446
Clear Lake, SD (57226)	1814
Colman, SD (57017)	1152
Colome, SD (57528)	644
Colton, SD (57018)	1243
Corsica, SD (57328)	994
Crooks, SD (57020)	1407
Renner, SD (57055)	1002
Custer, SD (57730)	4499
Deadwood, SD (57732)	2066
Dell Rapids, SD (57022)	4446
De Smet, SD (57231)	1427
Dupree, SD (57623)	732
Eagle Butte, SD (57625)	2743
Edgemont, SD (57735)	1011
Elk Point, SD (57025)	2482
Elkton, SD (57026)	1249
Emery, SD (57332)	2154
Estelline, SD (57234)	1006
Ethan, SD (57334)	734
Eureka, SD (57437)	1097
Faith, SD (57626)	833
Faulkton, SD (57438)	977
Flandreau, SD (57028)	2722
Florence, SD (57235)	726
Fort Pierre, SD (57532)	2566
Fort Thompson, SD (57339)	969
Frederick, SD (57441)	495
Freeman, SD (57029)	1789
Garretson, SD (57030)	2575
Gary, SD (57237)	564
Gayville, SD (57031)	547
Geddes, SD (57342)	504
Gettysburg, SD (57442)	1466
Gregory, SD (57533)	1609
Groton, SD (57445)	1827
Harrisburg, SD (57032)	5057
Hartford, SD (57033)	4156
Hayti, SD (57241)	806
Hecla, SD (57446)	433
Henry, SD (57243)	528
Hermosa, SD (57744)	1788
Herreid, SD (57632)	565
Highmore, SD (57345)	1037
Hill City, SD (57745)	1950
Hitchcock, SD (57348)	490
Hot Springs, SD (57747)	4655
Hoven, SD (57450)	597
Howard, SD (57349)	1300
Hudson, SD (57034)	651
Humboldt, SD (57035)	1062
Hurley, SD (57036)	753
Huron, SD (57350)	11666
Ipswich, SD (57451)	1791
Irene, SD (57037)	809
Iroquois, SD (57353)	661
Jefferson, SD (57038)	1471
Kadoka, SD (57543)	696
Keystone, SD (57751)	699
Kimball, SD (57355)	991
Kyle, SD (57752)	1296
Lake Andes, SD (57356)	1185
Lake Norden, SD (57248)	785
Lake Preston, SD (57249)	923
Langford, SD (57454)	486
Lead, SD (57754)	3152
Lemmon, SD (57638)	1588
Lennox, SD (57039)	2904
Leola, SD (57456)	625
Letcher, SD (57359)	600
Lower Brule, SD (57548)	896
Mc Laughlin, SD (57642)	1133
Madison, SD (57042)	7353
Marion, SD (57043)	1250
Martin, SD (57551)	1615
Menno, SD (57045)	876
Midland, SD (57552)	508
Milbank, SD (57252)	4253
Miller, SD (57362)	1789
Mission, SD (57555)	2297
Mission Hill, SD (57046)	559
Mitchell, SD (57301)	14701
Mobridge, SD (57601)	3226
Montrose, SD (57048)	955
Mount Vernon, SD (57363)	887
Murdo, SD (57559)	619
Newell, SD (57760)	1048
New Underwood, SD (57761)	957
North Sioux City, SD (57049)	5515
Oacoma, SD (57365)	448
Oglala, SD (57764)	846
Onida, SD (57564)	870
Parker, SD (57053)	1723
Parkston, SD (57366)	2005
Parmelee, SD (57566)	507
Peever, SD (57257)	527
Philip, SD (57567)	1216
Piedmont, SD (57769)	2978
Pierre, SD (57501)	14058
Pine Ridge, SD (57770)	3139
Plankinton, SD (57368)	976
Platte, SD (57369)	2005
Pollock, SD (57648)	431
Porcupine, SD (57772)	867
Presho, SD (57568)	663
Pukwana, SD (57370)	655
Rapid City, SD (57701)	31822
Rapid City, SD (57702)	29801
Rapid City, SD (57703)	12052
Redfield, SD (57469)	2606
Revillo, SD (57259)	447
Roscoe, SD (57471)	573
Rosholt, SD (57260)	837
Saint Francis, SD (57572)	896
Salem, SD (57058)	1681
Scotland, SD (57059)	1075
Selby, SD (57472)	848
Sioux Falls, SD (57103)	29619
Sioux Falls, SD (57104)	18944
Sioux Falls, SD (57105)	18748
Sioux Falls, SD (57106)	38092
Sioux Falls, SD (57107)	6663
Sioux Falls, SD (57108)	15323
Sioux Falls, SD (57110)	10783
Sisseton, SD (57262)	3924
Spearfish, SD (57783)	11707
Springfield, SD (57062)	1110
Stickney, SD (57375)	599
Sturgis, SD (57785)	7646
Summit, SD (57266)	450
Tabor, SD (57063)	752
Tea, SD (57064)	4252
Timber Lake, SD (57656)	650
Tripp, SD (57376)	792
Tyndall, SD (57066)	1304
Valley Springs, SD (57068)	1402
Veblen, SD (57270)	473
Burbank, SD (57010)	462
Vermillion, SD (57069)	6905
Viborg, SD (57070)	1055
Volga, SD (57071)	2436
Volin, SD (57072)	577
Wagner, SD (57380)	2338
Wakonda, SD (57073)	554
Wall, SD (57790)	1059
Wanblee, SD (57577)	513
Warner, SD (57479)	607
Watertown, SD (57201)	21061
Waubay, SD (57273)	1026
Webster, SD (57274)	2478
Wentworth, SD (57075)	897
Wessington, SD (57381)	497
Wessington Springs, SD (57382)	1211
White, SD (57276)	955
White Lake, SD (57383)	603
White River, SD (57579)	873
Whitewood, SD (57793)	1555
Willow Lake, SD (57278)	521
Wilmot, SD (57279)	906
Winner, SD (57580)	3617
Wolsey, SD (57384)	763
Woonsocket, SD (57385)	1086
Worthing, SD (57077)	1172
Yankton, SD (57078)	15005
Altoona, KS (66710)	619
Arcadia, KS (66711)	471
Arma, KS (66712)	1579
Atchison, KS (66002)	10086
Baldwin City, KS (66006)	5787
Basehor, KS (66007)	4989
Baxter Springs, KS (66713)	4420
Blue Mound, KS (66010)	489
Bonner Springs, KS (66012)	9439
Bucyrus, KS (66013)	1734
Chanute, KS (66720)	9143
Cherokee, KS (66724)	882
Colony, KS (66015)	670
Columbus, KS (66725)	4538
Cummings, KS (66016)	472
De Soto, KS (66018)	4627
Easton, KS (66020)	1433
Edgerton, KS (66021)	2269
Effingham, KS (66023)	957
Erie, KS (66733)	1789
Eudora, KS (66025)	6292
Fontana, KS (66026)	565
Fort Scott, KS (66701)	9598
Fredonia, KS (66736)	3298
Galena, KS (66739)	3969
Gardner, KS (66030)	16688
Garnett, KS (66032)	4139
Girard, KS (66743)	3523
Greeley, KS (66033)	652
Highland, KS (66035)	802
Humboldt, KS (66748)	2288
Iola, KS (66749)	6079
Kansas City, KS (66101)	7458
Kansas City, KS (66102)	19113
Kansas City, KS (66103)	9428
Kansas City, KS (66104)	17894
Kansas City, KS (66105)	1824
Kansas City, KS (66106)	18231
Kansas City, KS (66109)	17446
Kansas City, KS (66111)	7060
Kansas City, KS (66112)	9092
Kincaid, KS (66039)	574
Lacygne, KS (66040)	2753
La Harpe, KS (66751)	672
Lancaster, KS (66041)	648
Lane, KS (66042)	593
Lawrence, KS (66044)	16052
Lawrence, KS (66046)	13843
Lawrence, KS (66047)	13614
Lawrence, KS (66049)	20738
Fort Leavenworth, KS (66027)	3546
Lansing, KS (66043)	7563
Leavenworth, KS (66048)	26489
Lecompton, KS (66050)	1596
Linwood, KS (66052)	1666
Louisburg, KS (66053)	6365
Mc Cune, KS (66753)	951
Mc Louth, KS (66054)	2471
Moran, KS (66755)	972
Mound City, KS (66056)	1420
Mulberry, KS (66756)	792
Neodesha, KS (66757)	2990
Nortonville, KS (66060)	936
Olathe, KS (66061)	44030
Olathe, KS (66062)	62025
Osawatomie, KS (66064)	4626
Oskaloosa, KS (66066)	2238
Ottawa, KS (66067)	12924
Ozawkie, KS (66070)	2183
Paola, KS (66071)	10473
Parker, KS (66072)	886
Perry, KS (66073)	2044
Pittsburg, KS (66762)	17111
Frontenac, KS (66763)	2718
Pleasanton, KS (66075)	1666
Pomona, KS (66076)	1883
Princeton, KS (66078)	811
Rantoul, KS (66079)	657
Richmond, KS (66080)	906
Riverton, KS (66770)	1090
Saint Paul, KS (66771)	816
Scammon, KS (66773)	690
Mission, KS (66202)	13580
Shawnee, KS (66203)	16375
Overland Park, KS (66204)	14958
Mission, KS (66205)	11532
Leawood, KS (66206)	9298
Overland Park, KS (66207)	12152
Prairie Village, KS (66208)	19259
Leawood, KS (66209)	18342
Overland Park, KS (66210)	15833
Leawood, KS (66211)	4389
Overland Park, KS (66212)	26941
Overland Park, KS (66213)	24367
Overland Park, KS (66214)	10183
Lenexa, KS (66215)	21795
Shawnee, KS (66216)	21995
Shawnee, KS (66217)	4582
Shawnee, KS (66218)	6340
Lenexa, KS (66219)	8818
Lenexa, KS (66220)	6418
Overland Park, KS (66221)	12706
Overland Park, KS (66223)	18381
Overland Park, KS (66224)	10071
Shawnee, KS (66226)	10690
Lenexa, KS (66227)	4074
Spring Hill, KS (66083)	7626
Stilwell, KS (66085)	6899
Thayer, KS (66776)	1063
Tonganoxie, KS (66086)	7970
Toronto, KS (66777)	443
Troy, KS (66087)	1774
Uniontown, KS (66779)	542
Valley Falls, KS (66088)	1978
Walnut, KS (66780)	472
Wathena, KS (66090)	2033
Weir, KS (66781)	1055
Wellsville, KS (66092)	3465
Westphalia, KS (66093)	524
Williamsburg, KS (66095)	743
Winchester, KS (66097)	851
Yates Center, KS (66783)	1891
Adrian, MO (64720)	3076
Advance, MO (63730)	2616
Agency, MO (64401)	1291
Albany, MO (64402)	1906
Aldrich, MO (65601)	653
Alma, MO (64001)	575
Altenburg, MO (63732)	765
Alton, MO (65606)	2361
Amazonia, MO (64421)	779
Amsterdam, MO (64723)	531
Anderson, MO (64831)	4361
Annapolis, MO (63620)	989
Appleton City, MO (64724)	1451
Arbyrd, MO (63821)	556
Arcadia, MO (63621)	975
Archie, MO (64725)	1894
Asbury, MO (64832)	539
Ash Grove, MO (65604)	2992
Aurora, MO (65605)	9165
Ava, MO (65608)	7090
Bakersfield, MO (65609)	622
Barnard, MO (64423)	639
Bates City, MO (64011)	2729
Belgrade, MO (63622)	731
Bell City, MO (63735)	605
Belleview, MO (63623)	615
Belton, MO (64012)	22429
Benton, MO (63736)	2616
Bernie, MO (63822)	2272
Bertrand, MO (63823)	945
Bethany, MO (64424)	3474
Billings, MO (65610)	4051
Birch Tree, MO (65438)	2076
Bismarck, MO (63624)	2593
Bloomfield, MO (63825)	3379
Bloomsdale, MO (63627)	2408
Blue Eye, MO (65611)	1662
Blue Springs, MO (64014)	20557
Blue Springs, MO (64015)	26554
Bogard, MO (64622)	501
Bois D Arc, MO (65612)	1091
Bolckow, MO (64427)	496
Bolivar, MO (65613)	12190
Bonne Terre, MO (63628)	10369
Bosworth, MO (64623)	506
Bourbon, MO (65441)	4205
Bragg City, MO (63827)	512
Branson, MO (65616)	17207
Braymer, MO (64624)	1303
Breckenridge, MO (64625)	524
Brighton, MO (65617)	1369
Bronaugh, MO (64728)	497
Brookfield, MO (64628)	4707
Brookline, MO (65619)	6066
Broseley, MO (63932)	970
Browning, MO (64630)	462
Bucklin, MO (64631)	762
Buckner, MO (64016)	3796
Bucyrus, MO (65444)	745
Buffalo, MO (65622)	6597
Bunker, MO (63629)	964
Burlington Junction, MO (64428)	747
Butler, MO (64730)	5629
Cabool, MO (65689)	3510
Blackwell, MO (63626)	729
Cadet, MO (63630)	3112
Cainsville, MO (64632)	554
Caledonia, MO (63631)	631
Camden Point, MO (64018)	794
Cameron, MO (64429)	7553
Campbell, MO (63933)	2737
Cape Fair, MO (65624)	1314
Cape Girardeau, MO (63701)	26449
Cape Girardeau, MO (63703)	5269
Cardwell, MO (63829)	782
Carl Junction, MO (64834)	7698
Carrollton, MO (64633)	4326
Carterville, MO (64835)	1432
Carthage, MO (64836)	17296
Caruthersville, MO (63830)	4987
Cassville, MO (65625)	6392
Caulfield, MO (65626)	1229
Centerview, MO (64019)	1891
Chadwick, MO (65629)	497
Chaffee, MO (63740)	3891
Charleston, MO (63834)	4154
Chilhowee, MO (64733)	890
Chillicothe, MO (64601)	9133
Clarksdale, MO (64430)	694
Clarkton, MO (63837)	1118
Cleveland, MO (64734)	1781
Clever, MO (65631)	3669
Clinton, MO (64735)	10581
Collins, MO (64738)	849
Concordia, MO (64020)	2936
Conway, MO (65632)	2260
Corder, MO (64021)	567
Cosby, MO (64436)	686
Cowgill, MO (64637)	507
Craig, MO (64437)	645
Crane, MO (65633)	3009
Creighton, MO (64739)	863
Crocker, MO (65452)	2524
Cross Timbers, MO (65634)	522
Cuba, MO (65453)	6614
Dearborn, MO (64439)	1415
Deepwater, MO (64740)	1419
De Kalb, MO (64440)	650
Dexter, MO (63841)	10395
Diamond, MO (64840)	2329
Dixon, MO (65459)	6176
Doe Run, MO (63637)	966
Doniphan, MO (63935)	7092
Dora, MO (65637)	805
Drexel, MO (64742)	1824
Dudley, MO (63936)	662
Dunnegan, MO (65640)	600
Eagle Rock, MO (65641)	929
Eagleville, MO (64442)	620
Easton, MO (64443)	978
East Prairie, MO (63845)	4132
Edgar Springs, MO (65462)	1224
Edgerton, MO (64444)	1144
El Dorado Springs, MO (64744)	5807
Eldridge, MO (65463)	797
Elkland, MO (65644)	2114
Ellington, MO (63638)	2092
Ellsinore, MO (63937)	2092
Eminence, MO (65466)	1244
Essex, MO (63846)	1139
Everton, MO (65646)	1513
Excelsior Springs, MO (64024)	12907
Exeter, MO (65647)	1672
Fairdealing, MO (63939)	1090
Fairfax, MO (64446)	968
Fair Grove, MO (65648)	4465
Fair Play, MO (65649)	1209
Fairview, MO (64842)	622
Falcon, MO (65470)	793
Farmington, MO (63640)	18389
Faucett, MO (64448)	991
Fisk, MO (63940)	1045
Park Hills, MO (63601)	12633
Leadwood, MO (63653)	821
Flemington, MO (65650)	943
Fordland, MO (65652)	2732
Forsyth, MO (65653)	4465
Fort Leonard Wood, MO (65473)	5364
Saint Robert, MO (65584)	7417
Fredericktown, MO (63645)	8598
Freeman, MO (64746)	1230
Frohna, MO (63748)	811
Gainesville, MO (65655)	2279
Galena, MO (65656)	3639
Gallatin, MO (64640)	2538
Galt, MO (64641)	483
Garden City, MO (64747)	3189
Gideon, MO (63848)	1072
Gilman City, MO (64642)	700
Glenallen, MO (63751)	933
Golden, MO (65658)	871
Golden City, MO (64748)	1169
Goodman, MO (64843)	2401
Gower, MO (64454)	2233
Grain Valley, MO (64029)	13841
Granby, MO (64844)	3267
Grandin, MO (63943)	586
Grandview, MO (64030)	18797
Grant City, MO (64456)	1206
Greenfield, MO (65661)	1868
Greenville, MO (63944)	1174
Greenwood, MO (64034)	6619
Grovespring, MO (65662)	958
Hale, MO (64643)	839
Half Way, MO (65663)	1662
Hamilton, MO (64644)	2331
Hardin, MO (64035)	781
Harrisonville, MO (64701)	11809
Hartville, MO (65667)	2215
Harviell, MO (63945)	934
Hayti, MO (63851)	2912
Hermitage, MO (65668)	1222
Higginsville, MO (64037)	4973
Highlandville, MO (65669)	1899
Holcomb, MO (63852)	1044
Holden, MO (64040)	5296
Hollister, MO (65672)	5195
Holt, MO (64048)	3698
Hopkins, MO (64461)	740
Hornersville, MO (63855)	798
Houston, MO (65483)	3682
Humansville, MO (65674)	1798
Hume, MO (64752)	617
Iberia, MO (65486)	2552
Independence, MO (64050)	16169
Independence, MO (64052)	15883
Independence, MO (64053)	3704
Independence, MO (64054)	2941
Independence, MO (64055)	28806
Independence, MO (64056)	13063
Independence, MO (64057)	11396
Independence, MO (64058)	5480
Irondale, MO (63648)	1159
Ironton, MO (63650)	3118
Jackson, MO (63755)	20568
Jamesport, MO (64648)	1430
Jasper, MO (64755)	2096
Jerico Springs, MO (64756)	484
Joplin, MO (64801)	23939
Joplin, MO (64804)	28240
Kansas City, MO (64105)	2349
Kansas City, MO (64106)	4035
Kansas City, MO (64108)	5109
Kansas City, MO (64109)	6026
Kansas City, MO (64110)	9801
Kansas City, MO (64111)	10803
Kansas City, MO (64112)	6441
Kansas City, MO (64113)	10513
Kansas City, MO (64114)	19663
Kansas City, MO (64116)	12764
Kansas City, MO (64117)	11001
Kansas City, MO (64118)	32787
Kansas City, MO (64119)	24389
Kansas City, MO (64123)	6554
Kansas City, MO (64124)	7580
Kansas City, MO (64125)	1190
Kansas City, MO (64126)	3659
Kansas City, MO (64127)	10391
Kansas City, MO (64128)	7551
Kansas City, MO (64129)	6727
Kansas City, MO (64130)	14296
Kansas City, MO (64131)	15969
Kansas City, MO (64132)	9437
Kansas City, MO (64133)	27498
Kansas City, MO (64134)	16466
Kansas City, MO (64136)	1554
Kansas City, MO (64137)	7597
Kansas City, MO (64138)	20286
Kansas City, MO (64139)	1443
Kansas City, MO (64145)	4416
Kansas City, MO (64146)	1110
Riverside, MO (64150)	2249
Kansas City, MO (64151)	20650
Kansas City, MO (64152)	22715
Kansas City, MO (64153)	4340
Kansas City, MO (64154)	7128
Kansas City, MO (64155)	19520
Kansas City, MO (64156)	3126
Kansas City, MO (64157)	13173
Kansas City, MO (64158)	3842
Kansas City, MO (64163)	564
Kearney, MO (64060)	11430
Kennett, MO (63857)	9013
Kidder, MO (64649)	736
Kimberling City, MO (65686)	4050
King City, MO (64463)	1314
Kingston, MO (64650)	519
Kingsville, MO (64061)	2878
Kirbyville, MO (65679)	2016
Kissee Mills, MO (65680)	845
Koshkonong, MO (65692)	1016
Laclede, MO (64651)	475
Lamar, MO (64759)	6533
Lampe, MO (65681)	1764
Laquey, MO (65534)	909
La Russell, MO (64848)	500
Lathrop, MO (64465)	3572
Lawson, MO (64062)	5249
Leasburg, MO (65535)	1269
Lebanon, MO (65536)	22561
Lees Summit, MO (64063)	17404
Lees Summit, MO (64064)	13693
Lees Summit, MO (64081)	19652
Lees Summit, MO (64082)	12007
Lees Summit, MO (64086)	18539
Leeton, MO (64761)	1136
Leopold, MO (63760)	536
Lesterville, MO (63654)	553
Lexington, MO (64067)	4431
Liberal, MO (64762)	1309
Liberty, MO (64068)	29483
Licking, MO (65542)	3752
Lilbourn, MO (63862)	1201
Linneus, MO (64653)	584
Lockwood, MO (65682)	1546
Lone Jack, MO (64070)	2831
Long Lane, MO (65590)	1065
Louisburg, MO (65685)	657
Lowry City, MO (64763)	1093
Macks Creek, MO (65786)	1587
Maitland, MO (64466)	486
Malden, MO (63863)	4284
Mansfield, MO (65704)	2763
Marble Hill, MO (63764)	4423
Marceline, MO (64658)	2731
Marionville, MO (65705)	2945
Marquand, MO (63655)	1063
Marshfield, MO (65706)	11534
Maryville, MO (64468)	9225
Matthews, MO (63867)	779
Maysville, MO (64469)	1784
Mayview, MO (64071)	714
Meadville, MO (64659)	785
Mercer, MO (64661)	676
Miller, MO (65707)	1770
Millersville, MO (63766)	1103
Milo, MO (64767)	641
Mineral Point, MO (63660)	2365
Monett, MO (65708)	9595
Montreal, MO (65591)	1020
Montrose, MO (64770)	867
Morrisville, MO (65710)	947
Mound City, MO (64470)	1334
Mountain Grove, MO (65711)	7045
Mountain View, MO (65548)	4305
Mount Vernon, MO (65712)	6219
Napoleon, MO (64074)	638
Naylor, MO (63953)	1179
Neelyville, MO (63954)	821
Neosho, MO (64850)	18271
Nevada, MO (64772)	10261
Newburg, MO (65550)	2093
New Madrid, MO (63869)	2677
Niangua, MO (65713)	1808
Nixa, MO (65714)	24610
Noel, MO (64854)	3040
Norborne, MO (64668)	1237
Norwood, MO (65717)	1833
Oak Grove, MO (64075)	9342
Oak Ridge, MO (63769)	1203
Odessa, MO (64076)	7765
Oldfield, MO (65720)	536
Oran, MO (63771)	2256
Oregon, MO (64473)	1296
Oronogo, MO (64855)	2186
Orrick, MO (64077)	1617
Osborn, MO (64474)	724
Osceola, MO (64776)	2724
Ozark, MO (65721)	22596
Parma, MO (63870)	683
Patterson, MO (63956)	740
Patton, MO (63662)	950
Pattonsburg, MO (64670)	837
Peculiar, MO (64078)	7608
Perryville, MO (63775)	13585
Phillipsburg, MO (65722)	1493
Piedmont, MO (63957)	4070
Pierce City, MO (65723)	2885
Pineville, MO (64856)	2929
Pittsburg, MO (65724)	960
Plato, MO (65552)	1532
Platte City, MO (64079)	10383
Plattsburg, MO (64477)	2846
Pleasant Hill, MO (64080)	10810
Pleasant Hope, MO (65725)	1961
Polo, MO (64671)	1650
Pomona, MO (65789)	1451
Poplar Bluff, MO (63901)	24265
Portageville, MO (63873)	3700
Potosi, MO (63664)	6610
Pottersville, MO (65790)	604
Preston, MO (65732)	701
Princeton, MO (64673)	1902
Purdy, MO (65734)	2559
Puxico, MO (63960)	2301
Qulin, MO (63961)	1155
Ravenwood, MO (64479)	724
Raymondville, MO (65555)	776
Raymore, MO (64083)	17550
Rayville, MO (64084)	1333
Reeds, MO (64859)	920
Reeds Spring, MO (65737)	6567
Republic, MO (65738)	13596
Rich Hill, MO (64779)	1909
Richland, MO (65556)	4343
Richmond, MO (64085)	7051
Ridgedale, MO (65739)	1185
Ridgeway, MO (64481)	888
Roach, MO (65787)	1301
Rockaway Beach, MO (65740)	2385
Rock Port, MO (64482)	1756
Rockville, MO (64780)	529
Rocky Comfort, MO (64861)	895
Rogersville, MO (65742)	9333
Rolla, MO (65401)	20451
Rosendale, MO (64483)	558
Rushville, MO (64484)	988
Sainte Genevieve, MO (63670)	9502
Saint James, MO (65559)	7033
Saint Joseph, MO (64501)	8500
Saint Joseph, MO (64503)	10238
Saint Joseph, MO (64504)	8913
Saint Joseph, MO (64505)	10868
Saint Joseph, MO (64506)	17076
Saint Joseph, MO (64507)	10647
Saint Mary, MO (63673)	1907
Salem, MO (65560)	10301
Sarcoxie, MO (64862)	2487
Savannah, MO (64485)	6969
Schell City, MO (64783)	597
Scott City, MO (63780)	5311
Sedgewickville, MO (63781)	1015
Seligman, MO (65745)	1847
Senath, MO (63876)	1519
Seneca, MO (64865)	4624
Seymour, MO (65746)	5400
Sheldon, MO (64784)	1187
Shell Knob, MO (65747)	2843
Sibley, MO (64088)	1080
Sikeston, MO (63801)	18169
Silva, MO (63964)	561
Skidmore, MO (64487)	655
Smithville, MO (64089)	10153
South West City, MO (64863)	1260
Sparta, MO (65753)	3764
Spickard, MO (64679)	594
Spokane, MO (65754)	803
Springfield, MO (65802)	30388
Springfield, MO (65803)	31813
Springfield, MO (65804)	29912
Springfield, MO (65806)	4884
Springfield, MO (65807)	38062
Springfield, MO (65809)	9876
Springfield, MO (65810)	17974
Stanberry, MO (64489)	1533
Stark City, MO (64866)	1016
Steele, MO (63877)	2603
Steelville, MO (65565)	4107
Viburnum, MO (65566)	726
Stella, MO (64867)	1014
Stewartsville, MO (64490)	1814
Stockton, MO (65785)	3984
Stotts City, MO (65756)	529
Stoutland, MO (65567)	913
Strafford, MO (65757)	5818
Summersville, MO (65571)	1569
Taneyville, MO (65759)	918
Tarkio, MO (64491)	1518
Tecumseh, MO (65760)	491
Thayer, MO (65791)	3079
Theodosia, MO (65761)	961
Trenton, MO (64683)	6297
Trimble, MO (64492)	1469
Tunas, MO (65764)	878
Turney, MO (64493)	472
Union Star, MO (64494)	871
Urbana, MO (65767)	1527
Urich, MO (64788)	1119
Van Buren, MO (63965)	2132
Verona, MO (65769)	2268
Vichy, MO (65580)	665
Vienna, MO (65582)	1725
Walker, MO (64790)	651
Walnut Grove, MO (65770)	2475
Walnut Shade, MO (65771)	999
Wappapello, MO (63966)	1763
Wardell, MO (63879)	564
Warrensburg, MO (64093)	17943
Washburn, MO (65772)	1638
Waverly, MO (64096)	894
Waynesville, MO (65583)	9896
Weatherby, MO (64497)	480
Weaubleau, MO (65774)	709
Webb City, MO (64870)	11188
Wellington, MO (64097)	1175
Wentworth, MO (64873)	804
Weston, MO (64098)	2484
West Plains, MO (65775)	18146
Wheatland, MO (65779)	1552
Wheeling, MO (64688)	465
Whitewater, MO (63785)	863
Willard, MO (65781)	7060
Williamsville, MO (63967)	1477
Willow Springs, MO (65793)	4622
Winona, MO (65588)	1865
Winston, MO (64689)	530
Zalma, MO (63787)	527
Avoca, IA (51521)	1838
Carson, IA (51525)	995
Clarinda, IA (51632)	5062
Council Bluffs, IA (51501)	26343
Council Bluffs, IA (51503)	29102
Crescent, IA (51526)	1667
Honey Creek, IA (51542)	874
Defiance, IA (51527)	514
Dow City, IA (51528)	798
Dunlap, IA (51529)	1409
Earling, IA (51530)	729
Elk Horn, IA (51531)	762
Elliott, IA (51532)	544
Emerson, IA (51533)	786
Essex, IA (51638)	1118
Farragut, IA (51639)	736
Glenwood, IA (51534)	7277
Griswold, IA (51535)	1610
Hamburg, IA (51640)	1339
Harlan, IA (51537)	5729
Lewis, IA (51544)	594
Logan, IA (51546)	2474
Malvern, IA (51551)	1493
Minden, IA (51553)	877
Missouri Valley, IA (51555)	4338
Mondamin, IA (51557)	791
Moorhead, IA (51558)	471
Neola, IA (51559)	1561
New Market, IA (51646)	658
Oakland, IA (51560)	1724
Pacific Junction, IA (51561)	1152
Persia, IA (51563)	651
Portsmouth, IA (51565)	479
Red Oak, IA (51566)	5664
Shelby, IA (51570)	876
Shenandoah, IA (51601)	4712
Sidney, IA (51652)	1496
Silver City, IA (51571)	537
Stanton, IA (51573)	946
Tabor, IA (51653)	1082
Thurman, IA (51654)	466
Treynor, IA (51575)	1483
Underwood, IA (51576)	1682
Walnut, IA (51577)	979
Woodbine, IA (51579)	1912
Carter Lake, IA (51510)	2746
Abilene, KS (67410)	8929
Allen, KS (66833)	478
Alma, KS (66401)	1563
Almena, KS (67622)	476
Altamont, KS (67330)	1376
Alta Vista, KS (66834)	803
Americus, KS (66835)	1082
Andale, KS (67001)	1359
Andover, KS (67002)	11299
Anthony, KS (67003)	2231
Argonia, KS (67004)	705
Arkansas City, KS (67005)	13101
Arlington, KS (67514)	571
Ashland, KS (67831)	917
Assaria, KS (67416)	1075
Attica, KS (67009)	651
Atwood, KS (67730)	1367
Auburn, KS (66402)	2643
Augusta, KS (67010)	11494
Axtell, KS (66403)	636
Baileyville, KS (66404)	489
Belle Plaine, KS (67013)	2673
Belleville, KS (66935)	2216
Beloit, KS (67420)	3984
Bennington, KS (67422)	1236
Benton, KS (67017)	1909
Berryton, KS (66409)	2989
Bird City, KS (67731)	546
Blue Rapids, KS (66411)	1056
Brewster, KS (67732)	465
Brookville, KS (67425)	598
Bucklin, KS (67834)	792
Buhler, KS (67522)	1748
Burden, KS (67019)	770
Burlingame, KS (66413)	1548
Burlington, KS (66839)	3448
Burns, KS (66840)	597
Burrton, KS (67020)	1474
Caldwell, KS (67022)	1183
Caney, KS (67333)	2530
Canton, KS (67428)	1317
Carbondale, KS (66414)	2441
Cawker City, KS (67430)	587
Cedar Vale, KS (67024)	650
Centralia, KS (66415)	740
Chapman, KS (67431)	2172
Chase, KS (67524)	513
Cheney, KS (67025)	3266
Cherryvale, KS (67335)	2921
Chetopa, KS (67336)	1298
Cimarron, KS (67835)	2471
Claflin, KS (67525)	1008
Clay Center, KS (67432)	5384
Clearwater, KS (67026)	4095
Clifton, KS (66937)	718
Clyde, KS (66938)	913
Coffeyville, KS (67337)	10213
Colby, KS (67701)	5266
Coldwater, KS (67029)	896
Colwich, KS (67030)	2275
Concordia, KS (66901)	5325
Conway Springs, KS (67031)	1800
Copeland, KS (67837)	703
Cottonwood Falls, KS (66845)	946
Council Grove, KS (66846)	2987
Courtland, KS (66939)	511
Cunningham, KS (67035)	841
Deerfield, KS (67838)	862
Delia, KS (66418)	493
Delphos, KS (67436)	579
Derby, KS (67037)	22917
Dighton, KS (67839)	1317
Dodge City, KS (67801)	23849
Douglass, KS (67039)	2884
Downs, KS (67437)	1025
Dwight, KS (66849)	471
Edna, KS (67342)	853
El Dorado, KS (67042)	12980
Elk City, KS (67344)	804
Elkhart, KS (67950)	2105
Ellinwood, KS (67526)	2382
Ellis, KS (67637)	2237
Ellsworth, KS (67439)	2510
Emporia, KS (66801)	21385
Enterprise, KS (67441)	912
Eskridge, KS (66423)	817
Eureka, KS (67045)	2932
Everest, KS (66424)	528
Fall River, KS (67047)	526
Florence, KS (66851)	489
Fowler, KS (67844)	774
Frankfort, KS (66427)	1182
Galva, KS (67443)	1629
Garden City, KS (67846)	28121
Garden Plain, KS (67050)	1615
Geneseo, KS (67444)	476
Glasco, KS (67445)	595
Glen Elder, KS (67446)	544
Goddard, KS (67052)	6870
Goodland, KS (67735)	4491
Grantville, KS (66429)	525
Great Bend, KS (67530)	15932
Greensburg, KS (67054)	991
Gridley, KS (66852)	557
Grinnell, KS (67738)	505
Gypsum, KS (67448)	1146
Halstead, KS (67056)	2539
Hanover, KS (66945)	978
Harper, KS (67058)	1740
Hartford, KS (66854)	653
Harveyville, KS (66431)	555
Haven, KS (67543)	1709
Haviland, KS (67059)	778
Hays, KS (67601)	18500
Haysville, KS (67060)	11466
Herington, KS (67449)	2585
Hesston, KS (67062)	3443
Hiawatha, KS (66434)	4045
Hill City, KS (67642)	1565
Hillsboro, KS (67063)	3000
Hoisington, KS (67544)	2783
Holcomb, KS (67851)	2241
Holton, KS (66436)	4826
Holyrood, KS (67450)	494
Hope, KS (67451)	873
Horton, KS (66439)	2124
Howard, KS (67349)	850
Hoxie, KS (67740)	1606
Hoyt, KS (66440)	1819
Hugoton, KS (67951)	4016
Hutchinson, KS (67501)	18924
Hutchinson, KS (67502)	20537
South Hutchinson, KS (67505)	1953
Independence, KS (67301)	10945
Ingalls, KS (67853)	724
Inman, KS (67546)	2230
Jamestown, KS (66948)	447
Jetmore, KS (67854)	1175
Jewell, KS (66949)	560
Johnson, KS (67855)	1734
Junction City, KS (66441)	21681
Fort Riley, KS (66442)	10468
Kanopolis, KS (67454)	566
Kechi, KS (67067)	1486
Kensington, KS (66951)	650
Kingman, KS (67068)	3714
Kinsley, KS (67547)	1596
Kiowa, KS (67070)	1008
Kismet, KS (67859)	519
La Crosse, KS (67548)	1258
Lakin, KS (67860)	2494
Larned, KS (67550)	4354
Lebanon, KS (66952)	421
Lebo, KS (66856)	1447
Leon, KS (67074)	1463
Leonardville, KS (66449)	687
Leoti, KS (67861)	1696
Le Roy, KS (66857)	802
Lewis, KS (67552)	609
Liberal, KS (67901)	16375
Lincoln, KS (67455)	1630
Lindsborg, KS (67456)	3760
Linn, KS (66953)	579
Little River, KS (67457)	705
Logan, KS (67646)	625
Longton, KS (67352)	481
Lyndon, KS (66451)	1512
Lyons, KS (67554)	3585
Mcpherson, KS (67460)	13317
Macksville, KS (67557)	624
Madison, KS (66860)	1037
Maize, KS (67101)	2961
Manhattan, KS (66502)	26941
Manhattan, KS (66503)	10934
Mankato, KS (66956)	1059
Maple Hill, KS (66507)	1000
Marion, KS (66861)	2655
Marquette, KS (67464)	922
Marysville, KS (66508)	3760
Mayetta, KS (66509)	2120
Meade, KS (67864)	1859
Medicine Lodge, KS (67104)	2198
Melvern, KS (66510)	661
Meriden, KS (66512)	3007
Milford, KS (66514)	1497
Norwich, KS (67118)	648
Miltonvale, KS (67466)	601
Minneapolis, KS (67467)	2491
Minneola, KS (67865)	883
Moline, KS (67353)	493
Montezuma, KS (67867)	1322
Moscow, KS (67952)	609
Moundridge, KS (67107)	2495
Mound Valley, KS (67354)	636
Mount Hope, KS (67108)	1432
Mulvane, KS (67110)	7257
Natoma, KS (67651)	452
Ness City, KS (67560)	1484
New Cambria, KS (67470)	461
Newton, KS (67114)	18192
Nickerson, KS (67561)	1282
North Newton, KS (67117)	1347
Norton, KS (67654)	3218
Oakley, KS (67748)	2180
Oberlin, KS (67749)	1946
Ogden, KS (66517)	1690
Olpe, KS (66865)	991
Olsburg, KS (66520)	534
Onaga, KS (66521)	1344
Osage City, KS (66523)	3095
Osborne, KS (67473)	1506
Oswego, KS (67356)	2218
Overbrook, KS (66524)	2211
Oxford, KS (67119)	1255
Parsons, KS (67357)	10910
Partridge, KS (67566)	528
Pawnee Rock, KS (67567)	492
Paxico, KS (66526)	645
Peabody, KS (66866)	1457
Peck, KS (67120)	1217
Phillipsburg, KS (67661)	3069
Plains, KS (67869)	1184
Plainville, KS (67663)	2245
Potwin, KS (67123)	598
Pratt, KS (67124)	6731
Pretty Prairie, KS (67570)	1183
Protection, KS (67127)	596
Quenemo, KS (66528)	724
Quinter, KS (67752)	1245
Randolph, KS (66554)	492
Reading, KS (66868)	657
Riley, KS (66531)	1172
Robinson, KS (66532)	585
Rolla, KS (67954)	638
Rose Hill, KS (67133)	5593
Rossville, KS (66533)	1455
Russell, KS (67665)	4301
Sabetha, KS (66534)	3099
Saint Francis, KS (67756)	1780
Saint George, KS (66535)	2152
Saint John, KS (67576)	1606
Saint Marys, KS (66536)	2583
Salina, KS (67401)	42461
Satanta, KS (67870)	1412
Scandia, KS (66966)	564
Scott City, KS (67871)	4292
Scranton, KS (66537)	1237
Sedan, KS (67361)	1445
Sedgwick, KS (67135)	2782
Seneca, KS (66538)	2930
Severy, KS (67137)	491
Sharon Springs, KS (67758)	880
Silver Lake, KS (66539)	2598
Smith Center, KS (66967)	1957
Solomon, KS (67480)	1560
South Haven, KS (67140)	664
Spearville, KS (67876)	1082
Stafford, KS (67578)	1175
Sterling, KS (67579)	2239
Stockton, KS (67669)	1502
Strong City, KS (66869)	625
Sublette, KS (67877)	1846
Sylvan Grove, KS (67481)	515
Syracuse, KS (67878)	1942
Tecumseh, KS (66542)	3223
Tescott, KS (67484)	749
Topeka, KS (66603)	1106
Topeka, KS (66604)	18933
Topeka, KS (66605)	15815
Topeka, KS (66606)	8719
Topeka, KS (66607)	6464
Topeka, KS (66608)	4527
Topeka, KS (66609)	5875
Topeka, KS (66610)	8273
Topeka, KS (66611)	8035
Topeka, KS (66612)	1353
Topeka, KS (66614)	27021
Topeka, KS (66615)	2576
Topeka, KS (66616)	4783
Topeka, KS (66617)	7898
Topeka, KS (66618)	8145
Topeka, KS (66619)	2387
Towanda, KS (67144)	2410
Tribune, KS (67879)	1105
Turon, KS (67583)	818
Udall, KS (67146)	1545
Ulysses, KS (67880)	6342
Valley Center, KS (67147)	8379
Vassar, KS (66543)	610
Victoria, KS (67671)	1406
Viola, KS (67149)	930
Wakarusa, KS (66546)	952
Wakeeney, KS (67672)	2142
Wakefield, KS (67487)	1221
Wamego, KS (66547)	6632
Washington, KS (66968)	1485
Waterville, KS (66548)	865
Waverly, KS (66871)	1128
Wellington, KS (67152)	7839
Westmoreland, KS (66549)	1425
Wetmore, KS (66550)	497
White City, KS (66872)	916
Whitewater, KS (67154)	1252
Wichita, KS (67202)	1056
Wichita, KS (67203)	22662
Wichita, KS (67204)	17109
Wichita, KS (67205)	14309
Wichita, KS (67206)	13290
Wichita, KS (67207)	21457
Wichita, KS (67208)	14041
Wichita, KS (67209)	11671
Wichita, KS (67210)	6778
Wichita, KS (67211)	14801
Wichita, KS (67212)	37935
Wichita, KS (67213)	15228
Wichita, KS (67214)	10109
Wichita, KS (67215)	4893
Wichita, KS (67216)	18275
Wichita, KS (67217)	23918
Wichita, KS (67218)	17272
Wichita, KS (67219)	8766
Wichita, KS (67220)	11150
Mcconnell Afb, KS (67221)	365
Wichita, KS (67226)	14772
Wichita, KS (67228)	1615
Wichita, KS (67230)	8779
Wichita, KS (67235)	9906
Wilson, KS (67490)	920
Winfield, KS (67156)	11851
Adams, NE (68301)	1242
Ainsworth, NE (69210)	2014
Albion, NE (68620)	2624
Alda, NE (68810)	875
Allen, NE (68710)	741
Alliance, NE (69301)	8573
Alma, NE (68920)	1196
Amherst, NE (68812)	702
Anselmo, NE (68813)	490
Ansley, NE (68814)	828
Arapahoe, NE (68922)	1058
Arcadia, NE (68815)	545
Arlington, NE (68002)	1922
Arnold, NE (69120)	820
Ashland, NE (68003)	3711
Atkinson, NE (68713)	1895
Auburn, NE (68305)	3453
Aurora, NE (68818)	4755
Axtell, NE (68924)	1044
Bancroft, NE (68004)	815
Bassett, NE (68714)	1063
Battle Creek, NE (68715)	1360
Bayard, NE (69334)	1846
Beatrice, NE (68310)	11815
Beaver City, NE (68926)	601
Beaver Crossing, NE (68313)	776
Beemer, NE (68716)	815
Bellevue, NE (68005)	19395
Bellevue, NE (68123)	23378
Bellevue, NE (68147)	8675
Bellwood, NE (68624)	920
Benkelman, NE (69021)	1061
Bennet, NE (68317)	1356
Bennington, NE (68007)	6539
Bertrand, NE (68927)	1031
Big Springs, NE (69122)	570
Blair, NE (68008)	10028
Bloomfield, NE (68718)	1495
Blue Hill, NE (68930)	1120
Bradshaw, NE (68319)	488
Brady, NE (69123)	808
Brainard, NE (68626)	602
Bridgeport, NE (69336)	1960
Broken Bow, NE (68822)	4012
Brule, NE (69127)	562
Burwell, NE (68823)	1813
Cairo, NE (68824)	1197
Callaway, NE (68825)	853
Cambridge, NE (69022)	1310
Carroll, NE (68723)	511
Cedar Bluffs, NE (68015)	910
Cedar Rapids, NE (68627)	594
Central City, NE (68826)	3147
Ceresco, NE (68017)	1508
Chadron, NE (69337)	4826
Chapman, NE (68827)	617
Chappell, NE (69129)	1110
Clarks, NE (68628)	734
Clarkson, NE (68629)	1210
Clay Center, NE (68933)	830
Clearwater, NE (68726)	706
Coleridge, NE (68727)	614
Columbus, NE (68601)	23426
Cook, NE (68329)	507
Cortland, NE (68331)	812
Cozad, NE (69130)	4305
Craig, NE (68019)	477
Crawford, NE (69339)	1259
Creighton, NE (68729)	1516
Creston, NE (68631)	469
Crete, NE (68333)	5949
Crofton, NE (68730)	1663
Culbertson, NE (69024)	1020
Curtis, NE (69025)	821
Dakota City, NE (68731)	2214
Dalton, NE (69131)	532
Dannebrog, NE (68831)	704
Davenport, NE (68335)	478
Davey, NE (68336)	508
David City, NE (68632)	3175
Decatur, NE (68020)	618
Denton, NE (68339)	1166
Deshler, NE (68340)	770
De Witt, NE (68341)	968
Diller, NE (68342)	500
Dodge, NE (68633)	1004
Doniphan, NE (68832)	1767
Dorchester, NE (68343)	884
Eagle, NE (68347)	2179
Edgar, NE (68935)	610
Elgin, NE (68636)	1167
Elkhorn, NE (68022)	14042
Elm Creek, NE (68836)	1508
Elmwood, NE (68349)	919
Elwood, NE (68937)	1539
Emerson, NE (68733)	1037
Eustis, NE (69028)	701
Ewing, NE (68735)	800
Exeter, NE (68351)	720
Fairbury, NE (68352)	4118
Fairfield, NE (68938)	515
Fairmont, NE (68354)	759
Falls City, NE (68355)	4164
Firth, NE (68358)	1566
Fordyce, NE (68736)	550
Fort Calhoun, NE (68023)	2323
Franklin, NE (68939)	1036
Fremont, NE (68025)	24335
Friend, NE (68359)	1280
Fullerton, NE (68638)	1437
Funk, NE (68940)	437
Garland, NE (68360)	482
Geneva, NE (68361)	2206
Genoa, NE (68640)	1322
Gering, NE (69341)	9032
Gibbon, NE (68840)	2403
Giltner, NE (68841)	590
Glenvil, NE (68941)	708
Gordon, NE (69343)	2125
Gothenburg, NE (69138)	3751
Grand Island, NE (68801)	22157
Grand Island, NE (68803)	18691
Grant, NE (69140)	1408
Greeley, NE (68842)	508
Greenwood, NE (68366)	960
Gretna, NE (68028)	9147
Hampton, NE (68843)	793
Harrison, NE (69346)	470
Hartington, NE (68739)	2596
Harvard, NE (68944)	986
Hastings, NE (68901)	19876
Hay Springs, NE (69347)	1059
Hebron, NE (68370)	1664
Hemingford, NE (69348)	1258
Henderson, NE (68371)	1329
Herman, NE (68029)	778
Hershey, NE (69143)	1317
Hickman, NE (68372)	2406
Hildreth, NE (68947)	473
Holdrege, NE (68949)	5550
Homer, NE (68030)	734
Hooper, NE (68031)	1521
Hoskins, NE (68740)	725
Howells, NE (68641)	981
Hubbard, NE (68741)	623
Humboldt, NE (68376)	1199
Humphrey, NE (68642)	1567
Imperial, NE (69033)	2141
Indianola, NE (69034)	787
Jackson, NE (68743)	609
Johnson, NE (68378)	578
Juniata, NE (68955)	1769
Kearney, NE (68845)	13594
Kearney, NE (68847)	13199
Kenesaw, NE (68956)	1010
Kennard, NE (68034)	756
Kimball, NE (69145)	2577
Laurel, NE (68745)	1351
Lawrence, NE (68957)	573
Leigh, NE (68643)	872
Lewellen, NE (69147)	496
Lexington, NE (68850)	9985
Lincoln, NE (68502)	19553
Lincoln, NE (68503)	9617
Lincoln, NE (68504)	11396
Lincoln, NE (68505)	12840
Lincoln, NE (68506)	23638
Lincoln, NE (68507)	11041
Lincoln, NE (68508)	4721
Lincoln, NE (68510)	16400
Lincoln, NE (68512)	10055
Lincoln, NE (68516)	34278
Lincoln, NE (68517)	476
Lincoln, NE (68520)	1261
Lincoln, NE (68521)	24205
Lincoln, NE (68522)	9044
Lincoln, NE (68523)	1269
Lincoln, NE (68524)	4631
Lincoln, NE (68526)	4025
Lincoln, NE (68527)	716
Lincoln, NE (68528)	4436
Lindsay, NE (68644)	752
Litchfield, NE (68852)	499
Lodgepole, NE (69149)	640
Loomis, NE (68958)	565
Louisville, NE (68037)	1908
Loup City, NE (68853)	1253
Lyman, NE (69352)	529
Lyons, NE (68038)	1175
Mc Cook, NE (69001)	7788
Mc Cool Junction, NE (68401)	650
Macy, NE (68039)	825
Madison, NE (68748)	2609
Madrid, NE (69150)	457
Malcolm, NE (68402)	1044
Marquette, NE (68854)	662
Martell, NE (68404)	863
Maxwell, NE (69151)	665
Mead, NE (68041)	827
Meadow Grove, NE (68752)	716
Merna, NE (68856)	545
Milford, NE (68405)	2503
Minatare, NE (69356)	1500
Minden, NE (68959)	3260
Mitchell, NE (69357)	3018
Monroe, NE (68647)	583
Morrill, NE (69358)	1617
Mullen, NE (69152)	749
Murdock, NE (68407)	713
Murray, NE (68409)	773
Nebraska City, NE (68410)	7021
Nehawka, NE (68413)	500
Neligh, NE (68756)	1639
Nelson, NE (68961)	688
Newcastle, NE (68757)	628
Newman Grove, NE (68758)	967
Nickerson, NE (68044)	578
Niobrara, NE (68760)	895
Norfolk, NE (68701)	24172
Ames, NE (68621)	470
North Bend, NE (68649)	1508
North Platte, NE (69101)	23774
Oakland, NE (68045)	1533
Odell, NE (68415)	614
Ogallala, NE (69153)	5063
Papillion, NE (68046)	21562
Omaha, NE (68102)	2704
Omaha, NE (68104)	26121
Omaha, NE (68105)	16032
Omaha, NE (68106)	15966
Omaha, NE (68107)	21226
Omaha, NE (68108)	10024
Omaha, NE (68110)	4845
Omaha, NE (68111)	15273
Omaha, NE (68112)	8919
Offutt A F B, NE (68113)	1228
Omaha, NE (68114)	14210
Omaha, NE (68116)	21909
Omaha, NE (68117)	6635
Omaha, NE (68118)	8987
Omaha, NE (68122)	8107
Omaha, NE (68124)	13211
Omaha, NE (68127)	18498
La Vista, NE (68128)	14841
Omaha, NE (68130)	15806
Omaha, NE (68131)	7864
Omaha, NE (68132)	10396
Papillion, NE (68133)	8116
Omaha, NE (68134)	22964
Omaha, NE (68135)	22616
Omaha, NE (68136)	11570
Omaha, NE (68137)	21523
Omaha, NE (68138)	10485
Omaha, NE (68142)	2634
Omaha, NE (68144)	21163
Omaha, NE (68152)	5267
Omaha, NE (68154)	20155
Omaha, NE (68157)	4512
Omaha, NE (68164)	23747
Oneill, NE (68763)	4043
Orchard, NE (68764)	678
Ord, NE (68862)	2496
Orleans, NE (68966)	561
Osceola, NE (68651)	1251
Oshkosh, NE (69154)	1032
Osmond, NE (68765)	1159
Overton, NE (68863)	958
Oxford, NE (68967)	907
Palisade, NE (69040)	508
Palmer, NE (68864)	885
Palmyra, NE (68418)	952
Pawnee City, NE (68420)	1044
Paxton, NE (69155)	885
Pender, NE (68047)	1457
Peru, NE (68421)	503
Petersburg, NE (68652)	682
Phillips, NE (68865)	832
Pickrell, NE (68422)	527
Pierce, NE (68767)	2749
Pilger, NE (68768)	624
Plainview, NE (68769)	1553
Platte Center, NE (68653)	719
Plattsmouth, NE (68048)	10490
Pleasant Dale, NE (68423)	867
Pleasanton, NE (68866)	795
Plymouth, NE (68424)	691
Polk, NE (68654)	514
Ponca, NE (68770)	1403
Potter, NE (69156)	627
Prague, NE (68050)	562
Randolph, NE (68771)	1378
Ravenna, NE (68869)	1893
Raymond, NE (68428)	1352
Red Cloud, NE (68970)	1079
Rising City, NE (68658)	630
Roca, NE (68430)	1318
Rushville, NE (69360)	1036
Saint Edward, NE (68660)	915
Saint Libory, NE (68872)	781
Saint Paul, NE (68873)	2703
Sargent, NE (68874)	789
Schuyler, NE (68661)	5543
Scotia, NE (68875)	497
Scottsbluff, NE (69361)	13012
Scribner, NE (68057)	1354
Seward, NE (68434)	6581
Shelby, NE (68662)	1005
Shelton, NE (68876)	1397
Shickley, NE (68436)	532
Sidney, NE (69162)	6464
Silver Creek, NE (68663)	676
South Sioux City, NE (68776)	12182
Spalding, NE (68665)	729
Spencer, NE (68777)	648
Springfield, NE (68059)	2817
Springview, NE (68778)	491
Stanton, NE (68779)	2022
Stapleton, NE (69163)	763
Sterling, NE (68443)	882
Stratton, NE (69043)	468
Stromsburg, NE (68666)	1355
Stuart, NE (68780)	894
Superior, NE (68978)	1993
Sutherland, NE (69165)	1559
Sutton, NE (68979)	1607
Syracuse, NE (68446)	2330
Tecumseh, NE (68450)	2029
Tekamah, NE (68061)	2127
Thedford, NE (69166)	490
Tilden, NE (68781)	1239
Trenton, NE (69044)	647
Unadilla, NE (68454)	603
Union, NE (68455)	634
Utica, NE (68456)	983
Valentine, NE (69201)	3502
Valley, NE (68064)	2831
Valparaiso, NE (68065)	1315
Verdigre, NE (68783)	792
Waco, NE (68460)	812
Wahoo, NE (68066)	4436
Wakefield, NE (68784)	1748
Wallace, NE (69169)	517
Walthill, NE (68067)	942
Walton, NE (68461)	645
Waterloo, NE (68069)	2302
Wauneta, NE (69045)	821
Wausa, NE (68786)	880
Waverly, NE (68462)	3253
Wayne, NE (68787)	4222
Weeping Water, NE (68463)	1386
Western, NE (68464)	468
Weston, NE (68070)	718
West Point, NE (68788)	4233
Wilber, NE (68465)	1951
Wilcox, NE (68982)	606
Winnebago, NE (68071)	1220
Winside, NE (68790)	669
Wisner, NE (68791)	1532
Wood River, NE (68883)	1978
Wymore, NE (68466)	1563
York, NE (68467)	7574
Yutan, NE (68073)	1713
Aguilar, CO (81020)	706
Akron, CO (80720)	1970
Alamosa, CO (81101)	10239
Antonito, CO (81120)	1484
Arvada, CO (80002)	13560
Arvada, CO (80003)	28869
Arvada, CO (80004)	29600
Arvada, CO (80005)	23423
Arvada, CO (80007)	6575
Aspen, CO (81611)	5266
Ault, CO (80610)	2162
Aurora, CO (80010)	25168
Aurora, CO (80011)	33297
Aurora, CO (80012)	34064
Aurora, CO (80013)	57047
Aurora, CO (80014)	29148
Aurora, CO (80015)	52858
Aurora, CO (80016)	33336
Aurora, CO (80017)	26545
Aurora, CO (80018)	7184
Aurora, CO (80019)	1296
Aurora, CO (80047)	1362
Austin, CO (81410)	1247
Avondale, CO (81022)	1190
Bailey, CO (80421)	6320
Basalt, CO (81621)	5321
Bayfield, CO (81122)	6813
Bellvue, CO (80512)	1803
Bennett, CO (80102)	4414
Berthoud, CO (80513)	9316
Beulah, CO (81023)	1043
Black Hawk, CO (80422)	2405
Blanca, CO (81123)	518
Boone, CO (81025)	708
Boulder, CO (80301)	19036
Boulder, CO (80302)	15073
Boulder, CO (80303)	16791
Boulder, CO (80304)	21108
Boulder, CO (80305)	13065
Breckenridge, CO (80424)	7959
Briggsdale, CO (80611)	551
Brighton, CO (80601)	26250
Brighton, CO (80602)	22592
Brighton, CO (80603)	9040
Broomfield, CO (80020)	41499
Broomfield, CO (80021)	25680
Broomfield, CO (80023)	10898
Brush, CO (80723)	5212
Buena Vista, CO (81211)	5559
Burlington, CO (80807)	3497
Byers, CO (80103)	1980
Calhan, CO (80808)	4677
Canon City, CO (81212)	18781
Carbondale, CO (81623)	11557
Cascade, CO (80809)	1365
Castle Rock, CO (80104)	23257
Castle Rock, CO (80108)	18741
Castle Rock, CO (80109)	13706
Cedaredge, CO (81413)	4252
Center, CO (81125)	2508
Cheyenne Wells, CO (80810)	944
Clark, CO (80428)	541
Clifton, CO (81520)	10846
Collbran, CO (81624)	1009
Colorado Springs, CO (80902)	7625
Colorado Springs, CO (80903)	8966
Colorado Springs, CO (80904)	15460
Colorado Springs, CO (80905)	9936
Colorado Springs, CO (80906)	31430
Colorado Springs, CO (80907)	20420
Colorado Springs, CO (80908)	11859
Colorado Springs, CO (80909)	25524
Colorado Springs, CO (80910)	18303
Colorado Springs, CO (80911)	25331
Colorado Springs, CO (80913)	1537
Colorado Springs, CO (80915)	15972
Colorado Springs, CO (80916)	25232
Colorado Springs, CO (80917)	22923
Colorado Springs, CO (80918)	36906
Colorado Springs, CO (80919)	24872
Colorado Springs, CO (80920)	32159
Colorado Springs, CO (80921)	14723
Colorado Springs, CO (80922)	21906
Colorado Springs, CO (80923)	20486
Colorado Springs, CO (80924)	3164
Colorado Springs, CO (80925)	4623
Colorado Springs, CO (80926)	1099
Colorado Springs, CO (80928)	777
Colorado Springs, CO (80930)	697
Colorado Springs, CO (80951)	3286
Commerce City, CO (80022)	30981
Conifer, CO (80433)	7660
Cortez, CO (81321)	11209
Cotopaxi, CO (81223)	1220
Craig, CO (81625)	9057
Crawford, CO (81415)	1256
Creede, CO (81130)	665
Crested Butte, CO (81224)	3512
Cripple Creek, CO (80813)	1710
Dacono, CO (80514)	3217
De Beque, CO (81630)	831
Deer Trail, CO (80105)	908
Del Norte, CO (81132)	2381
Delta, CO (81416)	10421
Denver, CO (80202)	6590
Denver, CO (80203)	12810
Denver, CO (80204)	19554
Denver, CO (80205)	20189
Denver, CO (80206)	17428
Denver, CO (80207)	16074
Denver, CO (80209)	17885
Denver, CO (80210)	24620
Denver, CO (80211)	24038
Denver, CO (80212)	14083
Denver, CO (80214)	17497
Denver, CO (80215)	14911
Denver, CO (80216)	7757
Denver, CO (80218)	13313
Denver, CO (80219)	43975
Denver, CO (80220)	26623
Denver, CO (80221)	28839
Denver, CO (80222)	15441
Denver, CO (80223)	12745
Denver, CO (80224)	14019
Denver, CO (80226)	24554
Denver, CO (80227)	28159
Denver, CO (80228)	26317
Denver, CO (80229)	37272
Denver, CO (80230)	5613
Denver, CO (80231)	24423
Denver, CO (80232)	17785
Denver, CO (80233)	36739
Denver, CO (80234)	20539
Denver, CO (80235)	6000
Denver, CO (80236)	11942
Denver, CO (80237)	15048
Denver, CO (80238)	8277
Denver, CO (80239)	27586
Thornton, CO (80241)	25982
Denver, CO (80246)	9347
Denver, CO (80247)	17955
Denver, CO (80249)	17986
Denver, CO (80260)	21814
Dillon, CO (80435)	6398
Silverthorne, CO (80498)	5312
Divide, CO (80814)	3423
Dolores, CO (81323)	3741
Dove Creek, CO (81324)	1155
Drake, CO (80515)	579
Durango, CO (81301)	19639
Durango, CO (81303)	5722
Eads, CO (81036)	773
Eaton, CO (80615)	6149
Eckert, CO (81418)	1286
Edwards, CO (81632)	6273
Elbert, CO (80106)	3550
Elizabeth, CO (80107)	10224
Englewood, CO (80110)	16323
Englewood, CO (80111)	26274
Englewood, CO (80112)	24434
Englewood, CO (80113)	15932
Erie, CO (80516)	17116
Estes Park, CO (80517)	8636
Evans, CO (80620)	12673
Evergreen, CO (80439)	19290
Fairplay, CO (80440)	1773
Flagler, CO (80815)	747
Fleming, CO (80728)	711
Florence, CO (81226)	4384
Florissant, CO (80816)	3921
Fort Collins, CO (80521)	17234
Fort Collins, CO (80524)	24832
Fort Collins, CO (80525)	39562
Fort Collins, CO (80526)	34310
Fort Collins, CO (80528)	15003
Fort Garland, CO (81133)	672
Fort Lupton, CO (80621)	9897
Fort Morgan, CO (80701)	12383
Log Lane Village, CO (80705)	614
Fountain, CO (80817)	18577
Fowler, CO (81039)	1402
Franktown, CO (80116)	3865
Frederick, CO (80530)	3350
Fruita, CO (81521)	12464
Gill, CO (80624)	828
Glenwood Springs, CO (81601)	10418
Golden, CO (80401)	30678
Golden, CO (80403)	16111
Granada, CO (81041)	553
Granby, CO (80446)	3166
Grand Junction, CO (81501)	14845
Grand Junction, CO (81503)	14959
Grand Junction, CO (81504)	23098
Grand Junction, CO (81505)	7827
Grand Junction, CO (81506)	9525
Grand Junction, CO (81507)	10299
Glade Park, CO (81523)	531
Grand Lake, CO (80447)	1541
Greeley, CO (80631)	27546
Greeley, CO (80634)	42039
Guffey, CO (80820)	557
Gunnison, CO (81230)	6932
Gypsum, CO (81637)	4489
Hartsel, CO (80449)	587
Haxtun, CO (80731)	1235
Hayden, CO (81639)	1897
Henderson, CO (80640)	8194
Hesperus, CO (81326)	1702
Holly, CO (81047)	1278
Holyoke, CO (80734)	2331
Hotchkiss, CO (81419)	3028
Howard, CO (81233)	669
Hudson, CO (80642)	3136
Hugo, CO (80821)	823
Idaho Springs, CO (80452)	2672
Ignacio, CO (81137)	4293
Iliff, CO (80736)	576
Jamestown, CO (80455)	491
Johnstown, CO (80534)	9297
Julesburg, CO (80737)	1312
Keenesburg, CO (80643)	2270
Kersey, CO (80644)	2401
Kiowa, CO (80117)	2139
Kremmling, CO (80459)	1814
Lafayette, CO (80026)	22364
La Jara, CO (81140)	1673
La Junta, CO (81050)	7263
Lake City, CO (81235)	668
Lake George, CO (80827)	601
Lamar, CO (81052)	6991
Laporte, CO (80535)	2450
Larkspur, CO (80118)	4843
La Salle, CO (80645)	3083
Las Animas, CO (81054)	2487
La Veta, CO (81055)	1188
Leadville, CO (80461)	5084
Lewis, CO (81327)	547
Limon, CO (80828)	1980
Littleton, CO (80120)	22949
Littleton, CO (80121)	16032
Littleton, CO (80122)	27470
Littleton, CO (80123)	38330
Lone Tree, CO (80124)	15055
Littleton, CO (80125)	8737
Littleton, CO (80126)	34260
Littleton, CO (80127)	39353
Littleton, CO (80128)	31088
Littleton, CO (80129)	22983
Littleton, CO (80130)	22771
Livermore, CO (80536)	1466
Loma, CO (81524)	1805
Longmont, CO (80501)	48987
Longmont, CO (80503)	26346
Longmont, CO (80504)	20307
Louisville, CO (80027)	27059
Loveland, CO (80537)	32084
Loveland, CO (80538)	36633
Lyons, CO (80540)	4199
Mack, CO (81525)	694
Mancos, CO (81328)	2998
Manitou Springs, CO (80829)	4429
Manzanola, CO (81058)	717
Mead, CO (80542)	3170
Meeker, CO (81641)	3184
Merino, CO (80741)	759
Mesa, CO (81643)	689
Milliken, CO (80543)	4731
Monte Vista, CO (81144)	5917
Montrose, CO (81401)	19993
Montrose, CO (81403)	5544
Monument, CO (80132)	18806
Morrison, CO (80465)	13157
Mosca, CO (81146)	461
Nathrop, CO (81236)	822
Naturita, CO (81422)	446
Nederland, CO (80466)	3090
New Castle, CO (81647)	5351
Nucla, CO (81424)	991
Nunn, CO (80648)	772
Oak Creek, CO (80467)	1410
Olathe, CO (81425)	3946
Olney Springs, CO (81062)	570
Ordway, CO (81063)	1153
Otis, CO (80743)	874
Pagosa Springs, CO (81147)	8863
Palisade, CO (81526)	4291
Palmer Lake, CO (80133)	2112
Paonia, CO (81428)	3018
Parachute, CO (81635)	4862
Parker, CO (80134)	47361
Parker, CO (80138)	24253
Penrose, CO (81240)	3678
Peyton, CO (80831)	18313
Pierce, CO (80650)	1190
Pine, CO (80470)	3036
Platteville, CO (80651)	3452
Pueblo, CO (81001)	20170
Pueblo, CO (81003)	8575
Pueblo, CO (81004)	16750
Pueblo, CO (81005)	24381
Pueblo, CO (81006)	9410
Pueblo, CO (81007)	23997
Pueblo, CO (81008)	8861
Ramah, CO (80832)	508
Rangely, CO (81648)	2189
Red Feather Lakes, CO (80545)	619
Ridgway, CO (81432)	2359
Rifle, CO (81650)	10027
Rocky Ford, CO (81067)	4033
Rollinsville, CO (80474)	419
Rush, CO (80833)	521
Rye, CO (81069)	1523
Saguache, CO (81149)	629
Salida, CO (81201)	6998
Sanford, CO (81151)	1000
San Luis, CO (81152)	812
Sedalia, CO (80135)	3406
Silt, CO (81652)	4113
Simla, CO (80835)	703
Snowmass, CO (81654)	978
South Fork, CO (81154)	1006
Springfield, CO (81073)	1464
Steamboat Springs, CO (80487)	5369
Sterling, CO (80751)	11745
Strasburg, CO (80136)	3882
Stratton, CO (80836)	925
Telluride, CO (81435)	4319
Trinidad, CO (81082)	9220
U S A F Academy, CO (80840)	1691
Vail, CO (81657)	3068
Walden, CO (80480)	985
Walsenburg, CO (81089)	3259
Walsh, CO (81090)	785
Watkins, CO (80137)	938
Weldona, CO (80653)	626
Wellington, CO (80549)	6912
Westcliffe, CO (81252)	2984
Westminster, CO (80030)	11249
Westminster, CO (80031)	28568
Weston, CO (81091)	631
Wheat Ridge, CO (80033)	19035
Whitewater, CO (81527)	1724
Wiggins, CO (80654)	1988
Wiley, CO (81092)	718
Windsor, CO (80550)	17389
Woodland Park, CO (80863)	8758
Wray, CO (80758)	3019
Yoder, CO (80864)	1039
Yuma, CO (80759)	3498
Afton, WY (83110)	3543
Bedford, WY (83112)	492
Etna, WY (83118)	612
Alpine, WY (83128)	1355
Baggs, WY (82321)	632
Basin, WY (82410)	1386
Big Piney, WY (83113)	2256
Boulder, WY (82923)	519
Buffalo, WY (82834)	6456
Burns, WY (82053)	1157
Carpenter, WY (82054)	668
Casper, WY (82601)	19758
Casper, WY (82604)	19989
Casper, WY (82609)	12694
Cheyenne, WY (82001)	26842
Fe Warren Afb, WY (82005)	442
Cheyenne, WY (82007)	14152
Cheyenne, WY (82009)	27411
Cody, WY (82414)	13606
Cokeville, WY (83114)	624
Daniel, WY (83115)	546
Dayton, WY (82836)	966
Douglas, WY (82633)	8296
Dubois, WY (82513)	1693
Encampment, WY (82325)	787
Evanston, WY (82930)	10825
Evansville, WY (82636)	3484
Farson, WY (82932)	663
Fort Bridger, WY (82933)	706
Fort Washakie, WY (82514)	2266
Freedom, WY (83120)	482
Gillette, WY (82716)	13217
Gillette, WY (82718)	16911
Glendo, WY (82213)	488
Glenrock, WY (82637)	3384
Green River, WY (82935)	11450
Greybull, WY (82426)	2176
Guernsey, WY (82214)	1100
Hanna, WY (82327)	724
Hulett, WY (82720)	802
Jackson, WY (83001)	7421
Kaycee, WY (82639)	695
Kemmerer, WY (83101)	2676
Kinnear, WY (82516)	586
La Barge, WY (83123)	646
Lander, WY (82520)	9746
Laramie, WY (82070)	12507
Laramie, WY (82072)	9514
Lingle, WY (82223)	857
Lovell, WY (82431)	2714
Lusk, WY (82225)	1674
Lyman, WY (82937)	2698
Meeteetse, WY (82433)	706
Moorcroft, WY (82721)	2553
Newcastle, WY (82701)	4410
Pavillion, WY (82523)	673
Pine Bluffs, WY (82082)	1433
Pinedale, WY (82941)	4227
Powell, WY (82435)	9162
Ranchester, WY (82839)	1078
Rawlins, WY (82301)	7606
Riverton, WY (82501)	14724
Rock Springs, WY (82901)	21310
Rozet, WY (82727)	1227
Saratoga, WY (82331)	2096
Sheridan, WY (82801)	20321
Shoshoni, WY (82649)	849
Banner, WY (82832)	459
Story, WY (82842)	683
Sundance, WY (82729)	2031
Ten Sleep, WY (82442)	668
Thayne, WY (83127)	2225
Thermopolis, WY (82443)	3975
Torrington, WY (82240)	7515
Upton, WY (82730)	1321
Wheatland, WY (82201)	5433
Wilson, WY (83014)	2334
Worland, WY (82401)	6629
Yellowstone National Park, WY (82190)	515
Aberdeen, ID (83210)	2511
American Falls, ID (83211)	4993
Arco, ID (83213)	1187
Ashton, ID (83420)	2011
Bancroft, ID (83217)	641
Bellevue, ID (83313)	2491
Blackfoot, ID (83221)	19761
Bliss, ID (83314)	688
Boise, ID (83702)	16631
Boise, ID (83703)	13203
Boise, ID (83704)	29687
Boise, ID (83705)	20030
Boise, ID (83706)	22175
Boise, ID (83709)	40418
Boise, ID (83712)	6689
Boise, ID (83713)	22198
Garden City, ID (83714)	16431
Boise, ID (83716)	11898
Bruneau, ID (83604)	557
Buhl, ID (83316)	7618
Burley, ID (83318)	12718
Caldwell, ID (83605)	22255
Caldwell, ID (83607)	19697
Cambridge, ID (83610)	780
Carey, ID (83320)	741
Cascade, ID (83611)	1919
Castleford, ID (83321)	487
Challis, ID (83226)	2080
Council, ID (83612)	1488
Declo, ID (83323)	1394
Donnelly, ID (83615)	1101
Downey, ID (83234)	864
Driggs, ID (83422)	3227
Dubois, ID (83423)	627
Eagle, ID (83616)	19058
Eden, ID (83325)	729
Emmett, ID (83617)	12006
Fairfield, ID (83327)	750
Filer, ID (83328)	4254
Firth, ID (83236)	1783
Franklin, ID (83237)	902
Fruitland, ID (83619)	5762
Garden Valley, ID (83622)	1383
Glenns Ferry, ID (83623)	1237
Gooding, ID (83330)	4929
Grace, ID (83241)	1600
Grand View, ID (83624)	886
Greenleaf, ID (83626)	1057
Hagerman, ID (83332)	1848
Hailey, ID (83333)	8542
Hammett, ID (83627)	522
Hansen, ID (83334)	1501
Hazelton, ID (83335)	1639
Heyburn, ID (83336)	3950
Homedale, ID (83628)	3392
Horseshoe Bend, ID (83629)	1338
Idaho City, ID (83631)	1010
Idaho Falls, ID (83401)	27628
Idaho Falls, ID (83402)	19686
Idaho Falls, ID (83404)	17939
Idaho Falls, ID (83406)	11575
Inkom, ID (83245)	1845
Iona, ID (83427)	1313
Island Park, ID (83429)	659
Jerome, ID (83338)	15083
Ketchum, ID (83340)	6204
Kimberly, ID (83341)	5210
Kuna, ID (83634)	14859
Lava Hot Springs, ID (83246)	863
Lewisville, ID (83431)	805
Mccall, ID (83638)	5138
Mccammon, ID (83250)	1292
Mackay, ID (83251)	882
Malad City, ID (83252)	3274
Malta, ID (83342)	876
Marsing, ID (83639)	2455
Melba, ID (83641)	2669
Menan, ID (83434)	1335
Meridian, ID (83642)	29511
Meridian, ID (83646)	34900
Middleton, ID (83644)	7321
Midvale, ID (83645)	485
Montpelier, ID (83254)	2861
Moore, ID (83255)	848
Mountain Home, ID (83647)	16417
Mountain Home A F B, ID (83648)	2558
Murtaugh, ID (83344)	870
Nampa, ID (83651)	20252
Nampa, ID (83686)	34372
Nampa, ID (83687)	21027
New Meadows, ID (83654)	1226
New Plymouth, ID (83655)	3448
Oakley, ID (83346)	1411
Parma, ID (83660)	4460
Paul, ID (83347)	2688
Payette, ID (83661)	7524
Pingree, ID (83262)	1086
Pocatello, ID (83201)	27114
Pocatello, ID (83202)	15116
Pocatello, ID (83204)	12953
Preston, ID (83263)	7033
Rexburg, ID (83440)	19264
Richfield, ID (83349)	799
Rigby, ID (83442)	14070
Ririe, ID (83443)	1111
Roberts, ID (83444)	992
Rupert, ID (83350)	9622
Saint Anthony, ID (83445)	5226
Salmon, ID (83467)	4938
Shelley, ID (83274)	7410
Dietrich, ID (83324)	528
Shoshone, ID (83352)	2411
Soda Springs, ID (83276)	3418
Star, ID (83669)	6028
Sugar City, ID (83448)	1900
Terreton, ID (83450)	874
Teton, ID (83451)	642
Tetonia, ID (83452)	1021
Twin Falls, ID (83301)	37918
Victor, ID (83455)	3100
Weiser, ID (83672)	6216
Wendell, ID (83355)	4319
Weston, ID (83286)	921
Wilder, ID (83676)	3316
Altamont, UT (84001)	787
American Fork, UT (84003)	31217
Alpine, UT (84004)	7291
Beaver, UT (84713)	2983
Bingham Canyon, UT (84006)	662
Blanding, UT (84511)	2906
Bluebell, UT (84007)	534
Bountiful, UT (84010)	35442
North Salt Lake, UT (84054)	12482
Woods Cross, UT (84087)	11264
Brigham City, UT (84302)	18927
Mantua, UT (84324)	608
Castle Dale, UT (84513)	1281
Cedar City, UT (84720)	15570
Cedar City, UT (84721)	11771
Cedar Valley, UT (84013)	791
Centerville, UT (84014)	13142
Clearfield, UT (84015)	47051
Hill Afb, UT (84056)	3122
Syracuse, UT (84075)	18186
Coalville, UT (84017)	2897
Corinne, UT (84307)	1142
Delta, UT (84624)	4311
Draper, UT (84020)	29089
Duchesne, UT (84021)	2345
Dugway, UT (84022)	665
East Carbon, UT (84520)	885
Eden, UT (84310)	3291
Elsinore, UT (84724)	894
Ephraim, UT (84627)	3049
Fairview, UT (84629)	1912
Farmington, UT (84025)	13580
Fielding, UT (84311)	624
Fillmore, UT (84631)	2287
Fort Duchesne, UT (84026)	1533
Garden City, UT (84028)	541
Garland, UT (84312)	2960
Grantsville, UT (84029)	7277
Green River, UT (84525)	890
Heber City, UT (84032)	13213
Helper, UT (84526)	3159
Hinckley, UT (84635)	638
Honeyville, UT (84314)	846
Hooper, UT (84315)	5926
Huntington, UT (84528)	2133
Huntsville, UT (84317)	1857
Hurricane, UT (84737)	10249
Hyde Park, UT (84318)	3090
Hyrum, UT (84319)	6063
Jensen, UT (84035)	718
Kamas, UT (84036)	4649
Kanab, UT (84741)	4079
Kaysville, UT (84037)	26068
Lapoint, UT (84039)	772
La Verkin, UT (84745)	3057
Layton, UT (84040)	19063
Layton, UT (84041)	34435
Eagle Mountain, UT (84005)	13404
Lehi, UT (84043)	34837
Saratoga Springs, UT (84045)	10503
Lewiston, UT (84320)	1737
Loa, UT (84747)	764
Logan, UT (84321)	28147
Logan, UT (84341)	14269
Magna, UT (84044)	20906
Manila, UT (84046)	508
Manti, UT (84642)	2456
Mendon, UT (84325)	1532
Midvale, UT (84047)	24947
Midway, UT (84049)	3291
Milford, UT (84751)	1354
Moab, UT (84532)	7719
Mona, UT (84645)	1716
Monroe, UT (84754)	2726
Monticello, UT (84535)	1880
Morgan, UT (84050)	7401
Mount Pleasant, UT (84647)	2718
Myton, UT (84052)	1024
Neola, UT (84053)	638
Nephi, UT (84648)	4378
New Harmony, UT (84757)	848
Oakley, UT (84055)	1227
Ogden, UT (84401)	24720
Ogden, UT (84403)	27668
Ogden, UT (84404)	43129
Ogden, UT (84405)	23956
Ogden, UT (84414)	21986
Orem, UT (84057)	27897
Orem, UT (84058)	21588
Orem, UT (84097)	17366
Panguitch, UT (84759)	1556
Paradise, UT (84328)	1339
Park City, UT (84060)	7337
Park City, UT (84098)	14558
Payson, UT (84651)	17332
Lindon, UT (84042)	7404
Pleasant Grove, UT (84062)	30358
Price, UT (84501)	10223
Providence, UT (84332)	5592
Provo, UT (84601)	22642
Provo, UT (84604)	25456
Provo, UT (84606)	16611
Randolph, UT (84064)	604
Richfield, UT (84701)	6237
Richmond, UT (84333)	2128
Riverton, UT (84065)	28981
South Jordan, UT (84095)	39612
Herriman, UT (84096)	22274
Roosevelt, UT (84066)	8673
Roy, UT (84067)	30456
Salem, UT (84653)	6136
Salina, UT (84654)	2053
Salt Lake City, UT (84101)	3015
Salt Lake City, UT (84102)	11317
Salt Lake City, UT (84103)	16096
Salt Lake City, UT (84104)	18478
Salt Lake City, UT (84105)	17035
Salt Lake City, UT (84106)	25105
Salt Lake City, UT (84107)	24075
Salt Lake City, UT (84108)	16475
Salt Lake City, UT (84109)	19819
Salt Lake City, UT (84111)	6605
Salt Lake City, UT (84112)	565
Salt Lake City, UT (84115)	18218
Salt Lake City, UT (84116)	26849
Salt Lake City, UT (84117)	19613
Salt Lake City, UT (84118)	55272
Salt Lake City, UT (84119)	39848
Salt Lake City, UT (84120)	39538
Salt Lake City, UT (84121)	34252
Salt Lake City, UT (84123)	29345
Salt Lake City, UT (84124)	17562
Salt Lake City, UT (84128)	22771
Sandy, UT (84070)	19331
Sandy, UT (84092)	24913
Sandy, UT (84093)	20126
Sandy, UT (84094)	22288
Ivins, UT (84738)	5083
Santa Clara, UT (84765)	4898
Santaquin, UT (84655)	7277
Smithfield, UT (84335)	8714
Spanish Fork, UT (84660)	26963
Springville, UT (84663)	22010
Mapleton, UT (84664)	5877
Saint George, UT (84770)	28268
Veyo, UT (84782)	584
Dammeron Valley, UT (84783)	644
Saint George, UT (84790)	26068
Stockton, UT (84071)	863
Tooele, UT (84074)	33037
Toquerville, UT (84774)	1053
Tremonton, UT (84337)	8749
Vernal, UT (84078)	19357
Wallsburg, UT (84082)	573
Washington, UT (84780)	13546
Wellington, UT (84542)	1455
Wellsville, UT (84339)	3781
Wendover, UT (84083)	1265
West Jordan, UT (84081)	20763
West Jordan, UT (84084)	35582
West Jordan, UT (84088)	32736
Willard, UT (84340)	2755
Ajo, AZ (85321)	2352
Gold Canyon, AZ (85118)	815
Apache Junction, AZ (85119)	1207
Apache Junction, AZ (85120)	1439
Arlington, AZ (85322)	524
Avondale, AZ (85323)	27847
Goodyear, AZ (85338)	33013
Avondale, AZ (85392)	23916
Goodyear, AZ (85395)	15752
Bagdad, AZ (86321)	1674
Benson, AZ (85602)	6950
Bisbee, AZ (85603)	4970
Black Canyon City, AZ (85324)	2150
Buckeye, AZ (85326)	33935
Buckeye, AZ (85396)	8428
Fort Mohave, AZ (86426)	9583
Bullhead City, AZ (86429)	4921
Mohave Valley, AZ (86440)	4524
Bullhead City, AZ (86442)	21885
Camp Verde, AZ (86322)	8381
Casa Grande, AZ (85122)	2773
Cave Creek, AZ (85331)	20574
Chandler, AZ (85224)	34850
Chandler, AZ (85225)	50692
Chandler, AZ (85226)	30752
Chandler, AZ (85248)	27354
Chandler, AZ (85249)	30246
Chandler, AZ (85286)	25373
Chinle, AZ (86503)	6331
Chino Valley, AZ (86323)	13396
Clarkdale, AZ (86324)	3241
Clifton, AZ (85533)	1699
Cochise, AZ (85606)	634
Concho, AZ (85924)	1320
Coolidge, AZ (85128)	712
Cornville, AZ (86325)	4018
Cottonwood, AZ (86326)	17399
Dewey, AZ (86327)	6987
Douglas, AZ (85607)	11382
Duncan, AZ (85534)	1741
Eagar, AZ (85925)	3030
Elfrida, AZ (85610)	845
El Mirage, AZ (85335)	23175
Flagstaff, AZ (86001)	27443
Flagstaff, AZ (86004)	27305
Happy Jack, AZ (86024)	535
Florence, AZ (85132)	1082
Fredonia, AZ (86022)	1382
Ganado, AZ (86505)	2610
Gila Bend, AZ (85337)	2013
Gilbert, AZ (85233)	30501
Gilbert, AZ (85234)	38062
Gilbert, AZ (85295)	25179
Gilbert, AZ (85296)	29919
Gilbert, AZ (85297)	19933
Gilbert, AZ (85298)	13876
Glendale, AZ (85301)	40197
Glendale, AZ (85302)	26533
Glendale, AZ (85303)	21416
Glendale, AZ (85304)	21080
Glendale, AZ (85305)	8030
Glendale, AZ (85306)	18367
Glendale, AZ (85307)	6667
Glendale, AZ (85308)	51636
Glendale Luke Afb, AZ (85309)	575
Glendale, AZ (85310)	16787
Globe, AZ (85501)	5795
Green Valley, AZ (85614)	17378
Green Valley, AZ (85622)	4216
Heber, AZ (85928)	1006
Hereford, AZ (85615)	7576
Higley, AZ (85236)	1406
Holbrook, AZ (86025)	3916
Huachuca City, AZ (85616)	4080
Kingman, AZ (86401)	16930
Kingman, AZ (86409)	16728
Golden Valley, AZ (86413)	6208
Dolan Springs, AZ (86441)	1055
Meadview, AZ (86444)	726
Kirkland, AZ (86332)	1010
Lake Havasu City, AZ (86403)	10771
Lake Havasu City, AZ (86404)	10968
Lake Havasu City, AZ (86406)	16549
Lakeside, AZ (85929)	5963
Laveen, AZ (85339)	25447
Litchfield Park, AZ (85340)	20735
Mc Neal, AZ (85617)	841
Mammoth, AZ (85618)	1262
Marana, AZ (85653)	10578
Marana, AZ (85658)	5442
Maricopa, AZ (85138)	2649
Maricopa, AZ (85139)	1309
Mayer, AZ (86333)	3607
Mesa, AZ (85201)	30719
Mesa, AZ (85202)	27400
Mesa, AZ (85203)	25043
Mesa, AZ (85204)	42421
Mesa, AZ (85205)	28740
Mesa, AZ (85206)	24538
Mesa, AZ (85207)	32936
Mesa, AZ (85208)	24285
Mesa, AZ (85209)	26883
Mesa, AZ (85210)	25446
Mesa, AZ (85212)	18236
Mesa, AZ (85213)	23194
Mesa, AZ (85215)	12633
Miami, AZ (85539)	1998
Morenci, AZ (85540)	2357
Morristown, AZ (85342)	1034
Nogales, AZ (85621)	16600
Rio Rico, AZ (85648)	14156
Oracle, AZ (85623)	2936
Parker, AZ (85344)	6771
Patagonia, AZ (85624)	949
Paulden, AZ (86334)	3113
Payson, AZ (85541)	15160
Peach Springs, AZ (86434)	1042
Pearce, AZ (85625)	1462
Peoria, AZ (85345)	40652
Peoria, AZ (85381)	19629
Peoria, AZ (85382)	31710
Peoria, AZ (85383)	28344
Peridot, AZ (85542)	1481
Phoenix, AZ (85003)	4814
Phoenix, AZ (85004)	2892
Phoenix, AZ (85006)	15463
Phoenix, AZ (85007)	7993
Phoenix, AZ (85008)	35650
Phoenix, AZ (85009)	28868
Phoenix, AZ (85012)	5072
Phoenix, AZ (85013)	13679
Phoenix, AZ (85014)	17060
Phoenix, AZ (85015)	27408
Phoenix, AZ (85016)	24352
Phoenix, AZ (85017)	23596
Phoenix, AZ (85018)	27860
Phoenix, AZ (85019)	17750
Phoenix, AZ (85020)	23961
Phoenix, AZ (85021)	25348
Phoenix, AZ (85022)	34997
Phoenix, AZ (85023)	24296
Phoenix, AZ (85024)	18426
Phoenix, AZ (85027)	27772
Phoenix, AZ (85028)	17187
Phoenix, AZ (85029)	30711
Phoenix, AZ (85031)	19654
Phoenix, AZ (85032)	49539
Phoenix, AZ (85033)	35334
Phoenix, AZ (85034)	3698
Phoenix, AZ (85035)	30272
Phoenix, AZ (85037)	30898
Phoenix, AZ (85040)	19518
Phoenix, AZ (85041)	38762
Phoenix, AZ (85042)	28006
Phoenix, AZ (85043)	20852
Phoenix, AZ (85044)	31181
Phoenix, AZ (85045)	6165
Phoenix, AZ (85048)	27952
Phoenix, AZ (85050)	20980
Phoenix, AZ (85051)	29114
Phoenix, AZ (85053)	21328
Phoenix, AZ (85054)	3389
Phoenix, AZ (85083)	12433
Phoenix, AZ (85085)	14158
Phoenix, AZ (85086)	29056
New River, AZ (85087)	5792
Pima, AZ (85543)	2521
Pine, AZ (85544)	2051
Pinetop, AZ (85935)	3965
Prescott, AZ (86301)	15643
Prescott, AZ (86303)	12808
Prescott, AZ (86305)	13591
Prescott Valley, AZ (86314)	25283
Prescott Valley, AZ (86315)	4348
San Tan Valley, AZ (85140)	2120
Queen Creek, AZ (85142)	3802
San Tan Valley, AZ (85143)	2579
Rimrock, AZ (86335)	2751
Safford, AZ (85546)	10849
Sahuarita, AZ (85629)	17772
Saint David, AZ (85630)	1787
Saint Johns, AZ (85936)	2764
Salome, AZ (85348)	1141
San Manuel, AZ (85631)	2582
San Simon, AZ (85632)	487
Scottsdale, AZ (85250)	13190
Scottsdale, AZ (85251)	25419
Paradise Valley, AZ (85253)	14478
Scottsdale, AZ (85254)	39463
Scottsdale, AZ (85255)	32485
Scottsdale, AZ (85256)	3237
Scottsdale, AZ (85257)	20217
Scottsdale, AZ (85258)	19998
Scottsdale, AZ (85259)	18820
Scottsdale, AZ (85260)	29865
Scottsdale, AZ (85262)	9741
Rio Verde, AZ (85263)	1452
Fort Mcdowell, AZ (85264)	925
Scottsdale, AZ (85266)	7745
Fountain Hills, AZ (85268)	18597
Sedona, AZ (86336)	7881
Sedona, AZ (86351)	4563
Sells, AZ (85634)	3638
Show Low, AZ (85901)	8799
Fort Huachuca, AZ (85613)	3284
Sierra Vista, AZ (85635)	26074
Sierra Vista, AZ (85650)	12112
Snowflake, AZ (85937)	5823
Somerton, AZ (85350)	12819
Elgin, AZ (85611)	566
Sonoita, AZ (85637)	1225
Springerville, AZ (85938)	2078
Sun City, AZ (85351)	21289
Sun City, AZ (85373)	13008
Surprise, AZ (85374)	35954
Sun City West, AZ (85375)	22764
Surprise, AZ (85379)	28969
Surprise, AZ (85387)	8103
Surprise, AZ (85388)	16775
Teec Nos Pos, AZ (86514)	952
Tempe, AZ (85281)	27888
Tempe, AZ (85282)	34790
Tempe, AZ (85283)	33298
Tempe, AZ (85284)	16526
Thatcher, AZ (85552)	4487
Tolleson, AZ (85353)	22522
Tombstone, AZ (85638)	1578
Tonalea, AZ (86044)	2634
Tonopah, AZ (85354)	4251
Topock, AZ (86436)	1291
Tucson, AZ (85701)	3370
Tucson, AZ (85704)	24722
Tucson, AZ (85705)	35072
Tucson, AZ (85706)	42504
Tucson, AZ (85708)	2435
Tucson, AZ (85710)	41204
Tucson, AZ (85711)	29028
Tucson, AZ (85712)	21914
Tucson, AZ (85713)	31479
Tucson, AZ (85714)	10183
Tucson, AZ (85715)	15265
Tucson, AZ (85716)	21232
Tucson, AZ (85718)	23069
Tucson, AZ (85719)	21278
Tucson, AZ (85730)	30004
Tucson, AZ (85735)	7943
Tucson, AZ (85736)	2676
Tucson, AZ (85737)	18767
Tucson, AZ (85739)	14012
Tucson, AZ (85741)	25062
Tucson, AZ (85742)	20908
Tucson, AZ (85743)	22093
Tucson, AZ (85745)	26509
Tucson, AZ (85746)	30332
Tucson, AZ (85747)	18812
Tucson, AZ (85748)	15719
Tucson, AZ (85749)	16821
Tucson, AZ (85750)	20875
Tucson, AZ (85755)	12081
Tucson, AZ (85756)	14665
Tucson, AZ (85757)	11335
Tumacacori, AZ (85640)	582
Amado, AZ (85645)	1524
Vail, AZ (85641)	17291
Waddell, AZ (85355)	6748
Wellton, AZ (85356)	2480
Wickenburg, AZ (85390)	4469
Willcox, AZ (85643)	5166
Williams, AZ (86046)	4238
Winslow, AZ (86047)	9122
Wittmann, AZ (85361)	4400
Youngtown, AZ (85363)	4323
Yuma, AZ (85364)	51977
Yuma, AZ (85365)	29774
Yuma, AZ (85367)	12188
Abiquiu, NM (87510)	887
Alamogordo, NM (88310)	25636
Albuquerque, NM (87102)	13214
Albuquerque, NM (87104)	8849
Albuquerque, NM (87105)	39863
Albuquerque, NM (87106)	16176
Albuquerque, NM (87107)	23016
Albuquerque, NM (87108)	25037
Albuquerque, NM (87109)	30267
Albuquerque, NM (87110)	31331
Albuquerque, NM (87111)	46340
Albuquerque, NM (87112)	35026
Albuquerque, NM (87113)	11523
Albuquerque, NM (87114)	46220
Albuquerque, NM (87116)	2952
Albuquerque, NM (87120)	44810
Albuquerque, NM (87121)	51438
Albuquerque, NM (87122)	15148
Albuquerque, NM (87123)	30443
Rio Rancho, NM (87124)	40802
Rio Rancho, NM (87144)	28607
Alto, NM (88312)	2086
Animas, NM (88020)	712
Anthony, NM (88021)	12366
Chaparral, NM (88081)	8763
Anton Chico, NM (87711)	512
Arrey, NM (87930)	551
Artesia, NM (88210)	11703
Aztec, NM (87410)	11695
Bayard, NM (88023)	2300
Belen, NM (87002)	15051
Algodones, NM (87001)	2456
Bernalillo, NM (87004)	8129
Blanco, NM (87412)	579
Bloomfield, NM (87413)	10596
Bluewater, NM (87005)	493
Bosque, NM (87006)	937
Capitan, NM (88316)	1853
Carlsbad, NM (88220)	24538
Carrizozo, NM (88301)	993
Cedar Crest, NM (87008)	2477
Cerrillos, NM (87010)	803
Chama, NM (87520)	1199
Chamisal, NM (87521)	637
Chimayo, NM (87522)	2265
Cimarron, NM (87714)	866
Clayton, NM (88415)	2441
Cleveland, NM (87715)	429
Cloudcroft, NM (88317)	1496
Clovis, NM (88101)	32423
Corrales, NM (87048)	8101
Cuba, NM (87013)	2392
Cubero, NM (87014)	528
Datil, NM (87821)	493
Deming, NM (88030)	15410
Dexter, NM (88230)	3689
Dulce, NM (87528)	1678
Edgewood, NM (87015)	10942
El Prado, NM (87529)	3356
El Rito, NM (87530)	815
Espanola, NM (87532)	11670
Hernandez, NM (87537)	675
Estancia, NM (87016)	1903
Farmington, NM (87401)	30882
Farmington, NM (87402)	8137
Flora Vista, NM (87415)	2179
Fort Sumner, NM (88119)	1519
Fruitland, NM (87416)	1734
Gallup, NM (87301)	11110
Gamerco, NM (87317)	988
Glenwood, NM (88039)	395
Glorieta, NM (87535)	1177
Grants, NM (87020)	7368
Hagerman, NM (88232)	1457
Hanover, NM (88041)	557
Hatch, NM (87937)	2521
Hobbs, NM (88240)	25221
Hobbs, NM (88242)	4547
Holloman Air Force Base, NM (88330)	2368
Hurley, NM (88043)	1183
Jal, NM (88252)	1625
Jarales, NM (87023)	791
Jemez Pueblo, NM (87024)	1800
Jemez Springs, NM (87025)	1067
Kirtland, NM (87417)	5126
Laguna, NM (87026)	2400
Lake Arthur, NM (88253)	714
La Luz, NM (88337)	2200
La Mesa, NM (88044)	2440
La Plata, NM (87418)	790
Las Cruces, NM (88001)	24215
White Sands Missile Range, NM (88002)	1312
Las Cruces, NM (88005)	18755
Las Cruces, NM (88007)	15153
Las Cruces, NM (88011)	19905
Las Cruces, NM (88012)	16772
Las Vegas, NM (87701)	13858
Sapello, NM (87745)	484
Lemitar, NM (87823)	538
Logan, NM (88426)	949
Lordsburg, NM (88045)	2798
Los Alamos, NM (87544)	16811
Los Lunas, NM (87031)	29693
Loving, NM (88256)	1422
Lovington, NM (88260)	10877
Magdalena, NM (87825)	1898
Melrose, NM (88124)	829
Mescalero, NM (88340)	2663
Mesilla Park, NM (88047)	4097
Mesquite, NM (88048)	3476
Vado, NM (88072)	616
Mimbres, NM (88049)	715
Mora, NM (87732)	1246
Moriarty, NM (87035)	5396
Stanley, NM (87056)	654
Mountainair, NM (87036)	1623
Nogal, NM (88341)	454
Ojo Caliente, NM (87549)	664
Pecos, NM (87552)	2212
Pena Blanca, NM (87041)	797
Penasco, NM (87553)	1059
Peralta, NM (87042)	3547
Bosque Farms, NM (87068)	3733
Placitas, NM (87043)	4415
Portales, NM (88130)	13035
Prewitt, NM (87045)	1003
Quemado, NM (87829)	572
Questa, NM (87556)	1823
Ramah, NM (87321)	1297
Ranchos De Taos, NM (87557)	5241
Raton, NM (87740)	6506
Reserve, NM (87830)	695
Ribera, NM (87560)	919
Roswell, NM (88201)	17830
Roswell, NM (88203)	20372
Ruidoso, NM (88345)	3843
Ruidoso Downs, NM (88346)	2591
Salem, NM (87941)	1264
San Antonio, NM (87832)	589
Sandia Park, NM (87047)	4138
Ohkay Owingeh, NM (87566)	2147
Santa Cruz, NM (87567)	3675
Santa Fe, NM (87501)	12352
Santa Fe, NM (87505)	23843
Santa Fe, NM (87506)	8870
Santa Fe, NM (87507)	31449
Santa Fe, NM (87508)	13360
Lamy, NM (87540)	717
Santa Rosa, NM (88435)	2373
Santo Domingo Pueblo, NM (87052)	1970
San Ysidro, NM (87053)	800
Shiprock, NM (87420)	5236
Arenas Valley, NM (88022)	450
Silver City, NM (88061)	10361
Socorro, NM (87801)	8072
Springer, NM (87747)	1062
Santa Teresa, NM (88008)	4196
Sunland Park, NM (88063)	9070
Taos, NM (87571)	8543
Tatum, NM (88267)	923
Texico, NM (88135)	1298
Thoreau, NM (87323)	1809
Tierra Amarilla, NM (87575)	507
Tijeras, NM (87059)	8247
Tohatchi, NM (87325)	1112
Truth Or Consequences, NM (87901)	4730
Tucumcari, NM (88401)	5225
Tularosa, NM (88352)	3822
Vadito, NM (87579)	555
Veguita, NM (87062)	1255
Waterflow, NM (87421)	1141
Williamsburg, NM (87942)	886
Anthony, TX (79821)	3335
Alturas, CA (96101)	3969
Blairsden-graeagle, CA (96103)	1434
Cedarville, CA (96104)	627
Coleville, CA (96107)	903
Doyle, CA (96109)	622
Janesville, CA (96114)	2530
Loyalton, CA (96118)	1177
Markleeville, CA (96120)	676
Portola, CA (96122)	3165
South Lake Tahoe, CA (96150)	9905
Standish, CA (96128)	541
Susanville, CA (96130)	11282
Olympic Valley, CA (96146)	1088
Truckee, CA (96161)	7896
Tulelake, CA (96134)	1711
Westwood, CA (96137)	2564
Alamo, NV (89001)	769
Amargosa Valley, NV (89020)	898
Battle Mountain, NV (89820)	4238
Boulder City, NV (89005)	12140
Caliente, NV (89008)	920
Carlin, NV (89822)	1909
Carson City, NV (89701)	19125
Carson City, NV (89703)	8118
Washoe Valley, NV (89704)	3575
Carson City, NV (89705)	4197
Carson City, NV (89706)	14414
Incline Village, NV (89451)	3216
Dayton, NV (89403)	11859
Elko, NV (89801)	16721
Spring Creek, NV (89815)	10509
Ely, NV (89301)	3864
Eureka, NV (89316)	1019
Fallon, NV (89406)	18212
Fernley, NV (89408)	15515
Gardnerville, NV (89410)	9160
Gardnerville, NV (89460)	9790
Hawthorne, NV (89415)	2981
Henderson, NV (89002)	24976
Henderson, NV (89011)	14840
Henderson, NV (89012)	23313
Henderson, NV (89014)	30076
Henderson, NV (89015)	30967
Henderson, NV (89044)	12009
Henderson, NV (89052)	38648
Henderson, NV (89074)	38386
Jackpot, NV (89825)	863
Jean, NV (89019)	2184
Las Vegas, NV (89101)	29222
Las Vegas, NV (89102)	28031
Las Vegas, NV (89103)	36409
Las Vegas, NV (89104)	31514
Las Vegas, NV (89106)	18467
Las Vegas, NV (89107)	28148
Las Vegas, NV (89108)	51274
Las Vegas, NV (89109)	5441
Las Vegas, NV (89110)	54825
Las Vegas, NV (89113)	18126
Las Vegas, NV (89115)	40398
Las Vegas, NV (89117)	43411
Las Vegas, NV (89118)	14459
Las Vegas, NV (89119)	33393
Las Vegas, NV (89120)	18410
Las Vegas, NV (89121)	47506
Las Vegas, NV (89122)	33634
Las Vegas, NV (89123)	42113
Las Vegas, NV (89124)	695
Las Vegas, NV (89128)	28310
Las Vegas, NV (89129)	39230
Las Vegas, NV (89130)	25893
Las Vegas, NV (89131)	33847
Las Vegas, NV (89134)	21619
Las Vegas, NV (89135)	19020
Las Vegas, NV (89138)	8709
Las Vegas, NV (89139)	23107
Las Vegas, NV (89141)	17821
Las Vegas, NV (89142)	25006
Las Vegas, NV (89143)	8980
Las Vegas, NV (89144)	14989
Las Vegas, NV (89145)	18928
Las Vegas, NV (89146)	14469
Las Vegas, NV (89147)	38172
Las Vegas, NV (89148)	29574
Las Vegas, NV (89149)	22963
Las Vegas, NV (89156)	19494
Las Vegas, NV (89166)	5582
Las Vegas, NV (89169)	16547
Las Vegas, NV (89178)	19056
Las Vegas, NV (89179)	2329
Las Vegas, NV (89183)	23952
Laughlin, NV (89029)	4587
Lovelock, NV (89419)	2670
Mesquite, NV (89027)	9418
Mesquite, NV (89034)	567
Minden, NV (89423)	10249
North Las Vegas, NV (89030)	37689
North Las Vegas, NV (89031)	48996
North Las Vegas, NV (89032)	31235
North Las Vegas, NV (89033)	877
North Las Vegas, NV (89081)	21281
North Las Vegas, NV (89084)	16445
North Las Vegas, NV (89085)	2431
North Las Vegas, NV (89086)	3482
Overton, NV (89040)	2610
Pahrump, NV (89048)	12946
Pahrump, NV (89060)	7106
Pahrump, NV (89061)	3343
Pioche, NV (89043)	752
Reno, NV (89501)	2231
Reno, NV (89502)	32168
Reno, NV (89503)	17866
Reno, NV (89506)	30429
Reno, NV (89508)	8388
Reno, NV (89509)	26407
Reno, NV (89510)	2972
Reno, NV (89511)	22966
Reno, NV (89512)	15838
Reno, NV (89519)	7428
Reno, NV (89521)	19942
Reno, NV (89523)	23996
Round Mountain, NV (89045)	1397
Searchlight, NV (89046)	476
Silver Springs, NV (89429)	5499
Sparks, NV (89431)	26558
Sun Valley, NV (89433)	15015
Sparks, NV (89434)	20166
Sparks, NV (89436)	30132
Sparks, NV (89441)	9340
Tonopah, NV (89049)	2059
Wellington, NV (89444)	2207
Wells, NV (89835)	1489
Winnemucca, NV (89445)	10697
Yerington, NV (89447)	5924
Adams, OR (97810)	607
Adrian, OR (97901)	483
Albany, OR (97321)	21662
Albany, OR (97322)	24504
Alsea, OR (97324)	844
Amity, OR (97101)	3083
Arlington, OR (97812)	661
Ashland, OR (97520)	19338
Astoria, OR (97103)	13122
Athena, OR (97813)	1110
Aumsville, OR (97325)	5293
Aurora, OR (97002)	5009
Azalea, OR (97410)	569
Baker City, OR (97814)	9500
Bandon, OR (97411)	5451
Banks, OR (97106)	3967
Beavercreek, OR (97004)	3878
Beaverton, OR (97005)	18387
Beaverton, OR (97006)	50291
Beaverton, OR (97007)	54304
Beaverton, OR (97008)	22687
Bend, OR (97701)	45428
Bend, OR (97702)	31666
Bend, OR (97707)	4839
Blodgett, OR (97326)	627
Blue River, OR (97413)	733
Boardman, OR (97818)	3229
Bonanza, OR (97623)	1736
Boring, OR (97009)	7429
Damascus, OR (97089)	9159
Brightwood, OR (97011)	736
Brookings, OR (97415)	11363
Brownsville, OR (97327)	2356
Burns, OR (97720)	3288
Butte Falls, OR (97522)	529
Canby, OR (97013)	18537
Canyon City, OR (97820)	976
Canyonville, OR (97417)	1877
Carlton, OR (97111)	2646
Cascade Locks, OR (97014)	1028
Cave Junction, OR (97523)	4309
Cheshire, OR (97419)	996
Chiloquin, OR (97624)	2459
Clackamas, OR (97015)	17233
Happy Valley, OR (97086)	19321
Clatskanie, OR (97016)	4880
Beaver, OR (97108)	513
Cloverdale, OR (97112)	1341
Colton, OR (97017)	2445
Columbia City, OR (97018)	1834
Condon, OR (97823)	807
Coos Bay, OR (97420)	19802
Coquille, OR (97423)	5124
Corbett, OR (97019)	2664
Cornelius, OR (97113)	11114
Corvallis, OR (97330)	29082
Corvallis, OR (97333)	13876
Cottage Grove, OR (97424)	13152
Cove, OR (97824)	1321
Crescent, OR (97733)	517
Creswell, OR (97426)	7662
Culver, OR (97734)	2182
Dallas, OR (97338)	15696
Days Creek, OR (97429)	575
Dayton, OR (97114)	3869
Depoe Bay, OR (97341)	1844
Dexter, OR (97431)	1800
Donald, OR (97020)	883
Drain, OR (97435)	1836
Dufur, OR (97021)	902
Dundee, OR (97115)	3619
Eagle Creek, OR (97022)	2910
Eagle Point, OR (97524)	11363
Echo, OR (97826)	867
Elgin, OR (97827)	2019
Elkton, OR (97436)	688
Elmira, OR (97437)	2065
Enterprise, OR (97828)	2575
Estacada, OR (97023)	7838
Eugene, OR (97401)	25718
Eugene, OR (97402)	37798
Eugene, OR (97403)	5658
Eugene, OR (97404)	26524
Eugene, OR (97405)	36017
Eugene, OR (97408)	9671
Pleasant Hill, OR (97455)	2179
Fairview, OR (97024)	8825
Falls City, OR (97344)	740
Florence, OR (97439)	11366
Forest Grove, OR (97116)	17563
Gales Creek, OR (97117)	476
Fossil, OR (97830)	484
Foster, OR (97345)	603
Gaston, OR (97119)	3648
Gervais, OR (97026)	2889
Gladstone, OR (97027)	9808
Glendale, OR (97442)	1478
Glide, OR (97443)	1829
Gold Beach, OR (97444)	3697
Gold Hill, OR (97525)	4095
Grand Ronde, OR (97347)	1301
Grants Pass, OR (97526)	24106
Grants Pass, OR (97527)	24158
Wilderville, OR (97543)	656
Gresham, OR (97030)	28011
Gresham, OR (97080)	31971
Haines, OR (97833)	814
Halfway, OR (97834)	823
Halsey, OR (97348)	1231
Hammond, OR (97121)	1038
Harrisburg, OR (97446)	3959
Heppner, OR (97836)	1620
Hermiston, OR (97838)	18893
Hillsboro, OR (97123)	35299
Hillsboro, OR (97124)	37231
Hines, OR (97738)	1618
Hood River, OR (97031)	14373
Hubbard, OR (97032)	3828
Idleyld Park, OR (97447)	531
Imbler, OR (97841)	480
Summerville, OR (97876)	683
Independence, OR (97351)	6983
Ione, OR (97843)	600
Irrigon, OR (97844)	2819
Jacksonville, OR (97530)	6416
Jefferson, OR (97352)	4876
John Day, OR (97845)	2019
Jordan Valley, OR (97910)	526
Joseph, OR (97846)	1748
Junction City, OR (97448)	9209
Keno, OR (97627)	1256
Klamath Falls, OR (97601)	16078
Klamath Falls, OR (97603)	22250
Lafayette, OR (97127)	3031
La Grande, OR (97850)	12642
Lake Oswego, OR (97034)	17530
Lake Oswego, OR (97035)	20935
Lakeside, OR (97449)	1335
Lakeview, OR (97630)	3712
Langlois, OR (97450)	544
La Pine, OR (97739)	8679
Lebanon, OR (97355)	21576
Lincoln City, OR (97367)	6778
Fall Creek, OR (97438)	1032
Lowell, OR (97452)	1127
Lyons, OR (97358)	2087
Mcminnville, OR (97128)	26304
Madras, OR (97741)	8373
Malin, OR (97632)	1055
Mapleton, OR (97453)	749
Marcola, OR (97454)	1283
Maupin, OR (97037)	717
Medford, OR (97501)	31960
Central Point, OR (97502)	22002
White City, OR (97503)	8234
Medford, OR (97504)	35337
Merlin, OR (97532)	2777
Merrill, OR (97633)	1285
Gates, OR (97346)	543
Mill City, OR (97360)	1603
Milton Freewater, OR (97862)	8481
Molalla, OR (97038)	11465
Monmouth, OR (97361)	7320
Monroe, OR (97456)	2319
Moro, OR (97039)	420
Mosier, OR (97040)	1045
Mount Angel, OR (97362)	3443
Mount Hood Parkdale, OR (97041)	2595
Mount Vernon, OR (97865)	812
Mulino, OR (97042)	2388
Myrtle Creek, OR (97457)	7128
Myrtle Point, OR (97458)	3374
Nehalem, OR (97131)	1652
Neotsu, OR (97364)	960
Newberg, OR (97132)	21540
Newport, OR (97365)	8626
South Beach, OR (97366)	1319
North Bend, OR (97459)	11172
North Plains, OR (97133)	3506
North Powder, OR (97867)	613
Noti, OR (97461)	573
Nyssa, OR (97913)	3893
Oakland, OR (97462)	2849
Oakridge, OR (97463)	2670
O Brien, OR (97534)	434
Ontario, OR (97914)	11440
Oregon City, OR (97045)	41314
Otis, OR (97368)	2205
Pendleton, OR (97801)	15535
Philomath, OR (97370)	7180
Phoenix, OR (97535)	4050
Pilot Rock, OR (97868)	1627
Portland, OR (97201)	9601
Portland, OR (97202)	29321
Portland, OR (97203)	19921
Portland, OR (97204)	836
Portland, OR (97205)	4492
Portland, OR (97206)	35891
Portland, OR (97209)	8987
Portland, OR (97210)	8602
Portland, OR (97211)	23730
Portland, OR (97212)	20362
Portland, OR (97213)	23750
Portland, OR (97214)	18351
Portland, OR (97215)	13485
Portland, OR (97216)	11628
Portland, OR (97217)	24399
Portland, OR (97218)	10497
Portland, OR (97219)	31603
Portland, OR (97220)	21235
Portland, OR (97221)	10201
Portland, OR (97222)	27140
Portland, OR (97223)	37044
Portland, OR (97224)	26167
Portland, OR (97225)	20315
Portland, OR (97227)	2564
Portland, OR (97229)	47620
Portland, OR (97230)	28437
Portland, OR (97231)	3610
Portland, OR (97232)	9232
Portland, OR (97233)	26032
Portland, OR (97236)	26071
Portland, OR (97239)	11180
Portland, OR (97266)	23278
Portland, OR (97267)	24402
Port Orford, OR (97465)	1450
Powell Butte, OR (97753)	1748
Powers, OR (97466)	496
Prairie City, OR (97869)	780
Prineville, OR (97754)	14336
Prospect, OR (97536)	709
Rainier, OR (97048)	5182
Redmond, OR (97756)	26318
Reedsport, OR (97467)	3991
Rhododendron, OR (97049)	1135
Richland, OR (97870)	457
Rickreall, OR (97371)	679
Riddle, OR (97469)	1856
Rockaway Beach, OR (97136)	1311
Rogue River, OR (97537)	5962
Roseburg, OR (97470)	21159
Roseburg, OR (97471)	15720
Saint Helens, OR (97051)	12339
Warren, OR (97053)	2622
Deer Island, OR (97054)	1020
Saint Paul, OR (97137)	1313
Salem, OR (97301)	33441
Salem, OR (97302)	30166
Salem, OR (97303)	30109
Salem, OR (97304)	23469
Salem, OR (97305)	28948
Salem, OR (97306)	21702
Salem, OR (97317)	15947
Sandy, OR (97055)	13811
Scappoose, OR (97056)	9718
Scio, OR (97374)	3998
Scotts Mills, OR (97375)	1003
Seaside, OR (97138)	7774
Selma, OR (97538)	1455
Shady Cove, OR (97539)	2763
Shedd, OR (97377)	777
Sheridan, OR (97378)	5041
Sherwood, OR (97140)	19211
Siletz, OR (97380)	1647
Silverton, OR (97381)	11898
Sisters, OR (97759)	5901
Springfield, OR (97477)	26525
Springfield, OR (97478)	26964
Stanfield, OR (97875)	2203
Stayton, OR (97383)	7512
Sublimity, OR (97385)	2808
Sutherlin, OR (97479)	7099
Sweet Home, OR (97386)	9095
Talent, OR (97540)	6328
Tangent, OR (97389)	1272
Tenmile, OR (97481)	540
Terrebonne, OR (97760)	5621
The Dalles, OR (97058)	15168
Bay City, OR (97107)	1189
Tillamook, OR (97141)	10032
Toledo, OR (97391)	4019
Trail, OR (97541)	1049
Troutdale, OR (97060)	16184
Tualatin, OR (97062)	23437
Turner, OR (97392)	4418
Tygh Valley, OR (97063)	880
Umatilla, OR (97882)	4622
Umpqua, OR (97486)	704
Union, OR (97883)	1979
Vale, OR (97918)	3367
Veneta, OR (97487)	6528
Vernonia, OR (97064)	2703
Vida, OR (97488)	758
Seal Rock, OR (97376)	927
Waldport, OR (97394)	3855
Wallowa, OR (97885)	1129
Walterville, OR (97489)	1272
Warrenton, OR (97146)	4913
Wasco, OR (97065)	550
Welches, OR (97067)	1966
West Linn, OR (97068)	24311
Weston, OR (97886)	881
Willamina, OR (97396)	2516
Williams, OR (97544)	1616
Wilsonville, OR (97070)	16252
Winchester, OR (97495)	1754
Camas Valley, OR (97416)	650
Winston, OR (97496)	5636
Wolf Creek, OR (97497)	948
Woodburn, OR (97071)	20539
Yachats, OR (97498)	1201
Yamhill, OR (97148)	2831
Yoncalla, OR (97499)	1482
Amboy, WA (98601)	2412
Ariel, WA (98603)	689
Battle Ground, WA (98604)	27301
Bingen, WA (98605)	1164
Brush Prairie, WA (98606)	8043
Camas, WA (98607)	22466
Carson, WA (98610)	2186
Castle Rock, WA (98611)	7651
Cathlamet, WA (98612)	2283
Goldendale, WA (98620)	5416
Ilwaco, WA (98624)	1058
Kalama, WA (98625)	5183
Kelso, WA (98626)	18401
La Center, WA (98629)	6806
Long Beach, WA (98631)	2596
Longview, WA (98632)	36879
Lyle, WA (98635)	1308
Naselle, WA (98638)	1203
Ocean Park, WA (98640)	3126
Ridgefield, WA (98642)	12904
Stevenson, WA (98648)	2339
Silverlake, WA (98645)	964
Toutle, WA (98649)	924
Trout Lake, WA (98650)	796
Underwood, WA (98651)	689
Vancouver, WA (98660)	7929
Vancouver, WA (98661)	30103
Vancouver, WA (98662)	24052
Vancouver, WA (98663)	10514
Vancouver, WA (98664)	16635
Vancouver, WA (98665)	19493
Vancouver, WA (98682)	42457
Vancouver, WA (98683)	24653
Vancouver, WA (98684)	21725
Vancouver, WA (98685)	22222
Vancouver, WA (98686)	14277
Washougal, WA (98671)	17158
White Salmon, WA (98672)	4714
Woodland, WA (98674)	9761
Yacolt, WA (98675)	4171
Athol, ID (83801)	4652
Bayview, ID (83803)	661
Blanchard, ID (83804)	929
Bonners Ferry, ID (83805)	6090
Cataldo, ID (83810)	987
Clark Fork, ID (83811)	1065
Cocolalla, ID (83813)	961
Coeur D Alene, ID (83814)	16915
Coeur D Alene, ID (83815)	23869
Cottonwood, ID (83522)	1502
Craigmont, ID (83523)	625
Culdesac, ID (83524)	813
Deary, ID (83823)	1109
Fernwood, ID (83830)	526
Genesee, ID (83832)	1314
Grangeville, ID (83530)	4346
Harrison, ID (83833)	1101
Hayden, ID (83835)	17972
Hope, ID (83836)	905
Juliaetta, ID (83535)	877
Kamiah, ID (83536)	2821
Kellogg, ID (83837)	2180
Kendrick, ID (83537)	917
Kingston, ID (83839)	1005
Kooskia, ID (83539)	1456
Lapwai, ID (83540)	1587
Lenore, ID (83541)	752
Lewiston, ID (83501)	27415
Moscow, ID (83843)	17155
Moyie Springs, ID (83845)	1000
Mullan, ID (83846)	606
Naples, ID (83847)	1120
Nezperce, ID (83543)	577
Orofino, ID (83544)	4411
Pierce, ID (83546)	468
Pinehurst, ID (83850)	1809
Plummer, ID (83851)	1336
Ponderay, ID (83852)	1291
Post Falls, ID (83854)	28064
Potlatch, ID (83855)	1716
Oldtown, ID (83822)	1125
Priest River, ID (83856)	4642
Princeton, ID (83857)	615
Rathdrum, ID (83858)	10870
Riggins, ID (83549)	682
Sagle, ID (83860)	4981
Saint Maries, ID (83861)	4934
Sandpoint, ID (83864)	13303
Smelterville, ID (83868)	653
Spirit Lake, ID (83869)	3295
Stites, ID (83552)	722
Troy, ID (83871)	1709
Viola, ID (83872)	575
Wallace, ID (83873)	1157
Weippe, ID (83553)	742
White Bird, ID (83554)	480
Worley, ID (83876)	1148
Aberdeen, WA (98520)	15882
Acme, WA (98220)	637
Addy, WA (99101)	1110
Airway Heights, WA (99001)	3318
Allyn, WA (98524)	3019
Anacortes, WA (98221)	18209
Arlington, WA (98223)	33446
Ashford, WA (98304)	577
Asotin, WA (99402)	1529
Auburn, WA (98001)	26341
Auburn, WA (98002)	23795
Federal Way, WA (98003)	33131
Federal Way, WA (98023)	38887
Pacific, WA (98047)	4987
Auburn, WA (98092)	31804
Belfair, WA (98528)	8469
Bellevue, WA (98004)	23399
Bellevue, WA (98005)	15676
Bellevue, WA (98006)	32889
Bellevue, WA (98007)	20351
Bellevue, WA (98008)	21220
Bellingham, WA (98225)	28537
Bellingham, WA (98226)	31902
Bellingham, WA (98229)	23484
Benton City, WA (99320)	7087
Beverly, WA (99321)	814
Black Diamond, WA (98010)	4572
Blaine, WA (98230)	11933
Bothell, WA (98011)	24565
Bothell, WA (98012)	45281
Bothell, WA (98021)	22499
Kenmore, WA (98028)	17666
Bow, WA (98232)	3469
Bremerton, WA (98310)	14449
Bremerton, WA (98311)	19895
Bremerton, WA (98312)	22706
Bremerton, WA (98337)	4860
Brewster, WA (98812)	4161
Bridgeport, WA (98813)	1762
Brinnon, WA (98320)	924
Buckley, WA (98321)	12347
Burbank, WA (99323)	3056
Burlington, WA (98233)	12236
Carbonado, WA (98323)	578
Carnation, WA (98014)	6247
Cashmere, WA (98815)	5537
Centralia, WA (98531)	17980
Chattaroy, WA (99003)	4308
Chehalis, WA (98532)	17358
Chelan, WA (98816)	5685
Cheney, WA (99004)	11862
Chewelah, WA (99109)	4092
Chimacum, WA (98325)	1791
Clarkston, WA (99403)	15046
Clayton, WA (99110)	1180
Cle Elum, WA (98922)	4322
Clinton, WA (98236)	4930
Colbert, WA (99005)	7473
Colfax, WA (99111)	3403
College Place, WA (99324)	6391
Colton, WA (99113)	684
Colville, WA (99114)	9752
Concrete, WA (98237)	2891
Connell, WA (99326)	2409
Cosmopolis, WA (98537)	1859
Coulee City, WA (99115)	860
Coulee Dam, WA (99116)	1070
Coupeville, WA (98239)	5841
Cowiche, WA (98923)	1380
Curlew, WA (99118)	548
Cusick, WA (99119)	685
Custer, WA (98240)	2684
Darrington, WA (98241)	1835
Davenport, WA (99122)	2941
Dayton, WA (99328)	2896
Deer Park, WA (99006)	9407
Deming, WA (98244)	2162
Anderson Island, WA (98303)	845
Dupont, WA (98327)	6798
Duvall, WA (98019)	9481
Eastsound, WA (98245)	3173
Eatonville, WA (98328)	7993
Edmonds, WA (98020)	17301
Edmonds, WA (98026)	30510
Electric City, WA (99123)	874
Elk, WA (99009)	2991
Ellensburg, WA (98926)	19321
Elma, WA (98541)	7129
Eltopia, WA (99330)	1213
Endicott, WA (99125)	482
Entiat, WA (98822)	1565
Enumclaw, WA (98022)	18217
Ephrata, WA (98823)	8394
Ethel, WA (98542)	467
Everett, WA (98201)	19653
Everett, WA (98203)	27475
Everett, WA (98204)	29113
Everett, WA (98205)	9914
Everett, WA (98208)	42115
Everson, WA (98247)	7112
Fairchild Air Force Base, WA (99011)	2244
Fairfield, WA (99012)	847
Fall City, WA (98024)	4965
Ferndale, WA (98248)	18428
Ford, WA (99013)	715
Forks, WA (98331)	3851
Fox Island, WA (98333)	3350
Freeland, WA (98249)	4262
Friday Harbor, WA (98250)	6795
Garfield, WA (99130)	668
Gig Harbor, WA (98329)	6993
Gig Harbor, WA (98332)	12061
Gig Harbor, WA (98335)	23324
Glenoma, WA (98336)	704
Gold Bar, WA (98251)	3652
Graham, WA (98338)	19914
Grand Coulee, WA (99133)	1235
Grandview, WA (98930)	11026
Granger, WA (98932)	3725
Granite Falls, WA (98252)	7091
Grapeview, WA (98546)	2093
Grayland, WA (98547)	959
Greenacres, WA (99016)	10495
Greenbank, WA (98253)	1522
Hansville, WA (98340)	2039
Harrah, WA (98933)	1112
Harrington, WA (99134)	483
Hoodsport, WA (98548)	1820
Hoquiam, WA (98550)	8013
Inchelium, WA (99138)	779
Indianola, WA (98342)	1287
Ione, WA (99139)	961
Issaquah, WA (98027)	24023
Issaquah, WA (98029)	19671
Sammamish, WA (98075)	17972
Kennewick, WA (99336)	34356
Kennewick, WA (99337)	23718
Kennewick, WA (99338)	9534
Kent, WA (98030)	25258
Kent, WA (98031)	30530
Kent, WA (98032)	24958
Kent, WA (98042)	37667
Evans, WA (99126)	557
Kettle Falls, WA (99141)	4191
Kingston, WA (98346)	8165
Kirkland, WA (98033)	29136
Kirkland, WA (98034)	33874
La Conner, WA (98257)	3632
Lacrosse, WA (99143)	560
Lakebay, WA (98349)	3534
Longbranch, WA (98351)	689
Lake Stevens, WA (98258)	24933
Langley, WA (98260)	4698
Leavenworth, WA (98826)	5523
Liberty Lake, WA (99019)	7886
Lilliwaup, WA (98555)	411
Lind, WA (99341)	642
Loon Lake, WA (99148)	1752
Lopez Island, WA (98261)	2042
Lummi Island, WA (98262)	777
Lynden, WA (98264)	15856
Lynnwood, WA (98036)	29598
Lynnwood, WA (98037)	21505
Lynnwood, WA (98087)	22536
Mccleary, WA (98557)	2526
Mabton, WA (98935)	3063
Malaga, WA (98828)	1767
Manson, WA (98831)	2465
Maple Falls, WA (98266)	2736
Maple Valley, WA (98038)	26284
Marblemount, WA (98267)	396
Marysville, WA (98270)	37794
Marysville, WA (98271)	21105
Mead, WA (99021)	8208
Medical Lake, WA (99022)	7073
Medina, WA (98039)	2795
Mercer Island, WA (98040)	21568
Mesa, WA (99343)	2005
Milton, WA (98354)	7118
Monroe, WA (98272)	21336
Montesano, WA (98563)	6399
Morton, WA (98356)	1846
Moses Lake, WA (98837)	30008
Mossyrock, WA (98564)	1840
Mountlake Terrace, WA (98043)	16807
Mount Vernon, WA (98273)	22770
Mount Vernon, WA (98274)	12941
Moxee, WA (98936)	4738
Mukilteo, WA (98275)	18276
Naches, WA (98937)	3478
Newman Lake, WA (99025)	4605
Newport, WA (99156)	6127
Nine Mile Falls, WA (99026)	7893
Nordland, WA (98358)	672
North Bend, WA (98045)	12164
Northport, WA (99157)	584
Oakesdale, WA (99158)	515
Oak Harbor, WA (98277)	31260
Oakville, WA (98568)	1966
Ocean Shores, WA (98569)	4354
Odessa, WA (99159)	1157
Okanogan, WA (98840)	3339
Olalla, WA (98359)	4171
Olga, WA (98279)	459
Olympia, WA (98501)	31077
Olympia, WA (98502)	22992
Lacey, WA (98503)	28782
Olympia, WA (98506)	14357
Olympia, WA (98512)	22068
Olympia, WA (98513)	25697
Olympia, WA (98516)	17177
Omak, WA (98841)	7180
Onalaska, WA (98570)	3103
Orondo, WA (98843)	1290
Oroville, WA (98844)	3319
Orting, WA (98360)	10462
Othello, WA (99344)	12525
Mattawa, WA (99349)	5573
Otis Orchards, WA (99027)	5348
Outlook, WA (98938)	1505
Packwood, WA (98361)	893
Palouse, WA (99161)	1243
Pasco, WA (99301)	49028
Pateros, WA (98846)	957
Pe Ell, WA (98572)	692
Peshastin, WA (98847)	1607
Point Roberts, WA (98281)	1227
Pomeroy, WA (99347)	1875
Port Angeles, WA (98362)	18956
Port Angeles, WA (98363)	9317
Port Hadlock, WA (98339)	3007
Port Ludlow, WA (98365)	3985
Port Orchard, WA (98366)	26363
Port Orchard, WA (98367)	20745
Port Townsend, WA (98368)	12489
Poulsbo, WA (98370)	23896
Prescott, WA (99348)	946
Prosser, WA (99350)	9838
Pullman, WA (99163)	15193
Puyallup, WA (98371)	18146
Puyallup, WA (98372)	17550
Puyallup, WA (98373)	19875
Puyallup, WA (98374)	29998
Puyallup, WA (98375)	21412
Quilcene, WA (98376)	1574
Quincy, WA (98848)	8293
Rainier, WA (98576)	3937
Randle, WA (98377)	1440
Ravensdale, WA (98051)	3087
Raymond, WA (98577)	4517
Reardan, WA (99029)	1320
Redmond, WA (98052)	49321
Redmond, WA (98053)	16209
Sammamish, WA (98074)	22999
Renton, WA (98055)	17802
Renton, WA (98056)	26638
Renton, WA (98057)	8649
Renton, WA (98058)	36288
Renton, WA (98059)	28941
Republic, WA (99166)	2235
Rice, WA (99167)	479
Richland, WA (99352)	24152
West Richland, WA (99353)	11303
Richland, WA (99354)	16864
Ritzville, WA (99169)	2202
Riverside, WA (98849)	744
Rochester, WA (98579)	9937
Rockford, WA (99030)	835
Rock Island, WA (98850)	1295
Rosalia, WA (99170)	929
Roy, WA (98580)	7358
Royal City, WA (99357)	3548
Saint John, WA (99171)	831
Salkum, WA (98582)	591
Seabeck, WA (98380)	4452
Seattle, WA (98101)	7771
Seattle, WA (98102)	16877
Seattle, WA (98103)	37725
Seattle, WA (98104)	7625
Seattle, WA (98105)	22817
Seattle, WA (98106)	17861
Seattle, WA (98107)	17933
Seattle, WA (98108)	17606
Seattle, WA (98109)	16733
Bainbridge Island, WA (98110)	20524
Seattle, WA (98112)	17540
Seattle, WA (98115)	39262
Seattle, WA (98116)	19561
Seattle, WA (98117)	27190
Seattle, WA (98118)	35182
Seattle, WA (98119)	16067
Seattle, WA (98121)	8766
Seattle, WA (98122)	22658
Seattle, WA (98125)	28991
Seattle, WA (98126)	15597
Seattle, WA (98133)	34567
Seattle, WA (98134)	639
Seattle, WA (98136)	12841
Seattle, WA (98144)	20806
Seattle, WA (98146)	21285
Seattle, WA (98148)	7657
Seattle, WA (98155)	28326
Seattle, WA (98166)	17814
Seattle, WA (98168)	27301
Seattle, WA (98177)	17778
Seattle, WA (98178)	18999
Seattle, WA (98188)	19239
Seattle, WA (98198)	28071
Seattle, WA (98199)	17099
Sedro Woolley, WA (98284)	18797
Selah, WA (98942)	14027
Sequim, WA (98382)	22435
Shelton, WA (98584)	26249
Silver Creek, WA (98585)	561
Silverdale, WA (98315)	3705
Silverdale, WA (98383)	18398
Snohomish, WA (98290)	26061
Snohomish, WA (98296)	21459
Snoqualmie, WA (98065)	10415
Soap Lake, WA (98851)	2789
South Bend, WA (98586)	1730
Spanaway, WA (98387)	35229
Spangle, WA (99031)	1065
Spokane, WA (99201)	7482
Spokane, WA (99202)	11755
Spokane, WA (99203)	17768
Spokane, WA (99204)	4689
Spokane, WA (99205)	32785
Spokane, WA (99206)	27742
Spokane, WA (99207)	21588
Spokane, WA (99208)	39208
Spokane, WA (99212)	15459
Spokane, WA (99216)	18131
Spokane, WA (99217)	13345
Spokane, WA (99218)	10594
Spokane, WA (99223)	24703
Spokane, WA (99224)	13713
Sprague, WA (99032)	557
Springdale, WA (99173)	1085
Camano Island, WA (98282)	12962
Stanwood, WA (98292)	18408
Sultan, WA (98294)	5432
Sumas, WA (98295)	2062
Sumner, WA (98390)	10101
Bonney Lake, WA (98391)	36407
Sunnyside, WA (98944)	15433
Suquamish, WA (98392)	2482
Steilacoom, WA (98388)	5407
Tacoma, WA (98402)	3129
Tacoma, WA (98403)	5759
Tacoma, WA (98404)	23625
Tacoma, WA (98405)	15592
Tacoma, WA (98406)	17048
Tacoma, WA (98407)	16446
Tacoma, WA (98408)	15122
Tacoma, WA (98409)	17561
Tacoma, WA (98418)	7646
Tacoma, WA (98422)	17021
Tacoma, WA (98424)	8155
Tacoma, WA (98433)	13450
Lakewood, WA (98439)	3171
Tacoma, WA (98443)	4614
Tacoma, WA (98444)	24124
Tacoma, WA (98445)	23358
Tacoma, WA (98446)	8283
Tacoma, WA (98465)	4986
Tacoma, WA (98466)	22026
University Place, WA (98467)	12487
Lakewood, WA (98498)	21759
Lakewood, WA (98499)	21500
Tahuya, WA (98588)	1161
Tekoa, WA (99033)	704
Tenino, WA (98589)	6175
Thorp, WA (98946)	452
Tieton, WA (98947)	2111
Toledo, WA (98591)	3330
Tonasket, WA (98855)	4299
Toppenish, WA (98948)	9422
Touchet, WA (99360)	1149
Twisp, WA (98856)	1952
Union, WA (98592)	1587
Usk, WA (99180)	827
Vader, WA (98593)	861
Valley, WA (99181)	1386
Valleyford, WA (99036)	1321
Vashon, WA (98070)	8856
Vaughn, WA (98394)	1739
Veradale, WA (99037)	11858
Waitsburg, WA (99361)	1495
Walla Walla, WA (99362)	30329
Wapato, WA (98951)	9224
Warden, WA (98857)	3207
Waterville, WA (98858)	1287
Wellpinit, WA (99040)	784
Wenatchee, WA (98801)	30299
East Wenatchee, WA (98802)	22456
Westport, WA (98595)	2384
White Swan, WA (98952)	1401
Wilbur, WA (99185)	1111
Winlock, WA (98596)	4748
Winthrop, WA (98862)	2073
Woodinville, WA (98072)	21605
Woodinville, WA (98077)	11516
Yakima, WA (98901)	18927
Yakima, WA (98902)	31952
Yakima, WA (98903)	11510
Yakima, WA (98908)	29357
Yelm, WA (98597)	17154
Zillah, WA (98953)	5004
Anchorage, AK (99501)	11113
Anchorage, AK (99502)	18918
Anchorage, AK (99503)	11361
Anchorage, AK (99504)	31110
Jber, AK (99505)	4647
Jber, AK (99506)	6290
Anchorage, AK (99507)	30403
Anchorage, AK (99508)	24660
Anchorage, AK (99515)	18877
Anchorage, AK (99516)	17313
Anchorage, AK (99517)	12984
Anchorage, AK (99518)	8070
Anchor Point, AK (99556)	1802
Chugiak, AK (99567)	7692
Copper Center, AK (99573)	878
Fort Greely, AK (99731)	645
Delta Junction, AK (99737)	3603
Eagle River, AK (99577)	23726
Fairbanks, AK (99701)	12139
Eielson Afb, AK (99702)	2579
Fort Wainwright, AK (99703)	5033
North Pole, AK (99705)	16064
Fairbanks, AK (99709)	16606
Fairbanks, AK (99712)	7262
Salcha, AK (99714)	823
Fairbanks, AK (99775)	1061
Gakona, AK (99586)	455
Glennallen, AK (99588)	1151
Haines, AK (99827)	2152
Healy, AK (99743)	914
Homer, AK (99603)	8774
Juneau, AK (99801)	18213
Douglas, AK (99824)	1782
Kasilof, AK (99610)	1973
Kenai, AK (99611)	11185
Ketchikan, AK (99901)	10392
Kodiak, AK (99615)	11442
Nenana, AK (99760)	618
Ninilchik, AK (99639)	1011
Palmer, AK (99645)	21020
Seward, AK (99664)	3718
Sitka, AK (99835)	7498
Soldotna, AK (99669)	12970
Sterling, AK (99672)	2713
Talkeetna, AK (99676)	1375
Tok, AK (99780)	1362
Valdez, AK (99686)	3567
Wasilla, AK (99654)	27809
Willow, AK (99688)	2175
Bell Gardens, CA (90201)	67468
Maywood, CA (90270)	19023
Beverly Hills, CA (90210)	16984
Beverly Hills, CA (90211)	8596
Beverly Hills, CA (90212)	12548
Compton, CA (90220)	34287
Compton, CA (90221)	36005
Compton, CA (90222)	20801
Culver City, CA (90230)	25528
Culver City, CA (90232)	13073
Downey, CA (90240)	19687
Downey, CA (90241)	32425
Downey, CA (90242)	31123
El Segundo, CA (90245)	15421
Gardena, CA (90247)	35920
Gardena, CA (90248)	8825
Gardena, CA (90249)	21361
Hawthorne, CA (90250)	68109
Huntington Park, CA (90255)	54716
Inglewood, CA (90301)	25753
Inglewood, CA (90302)	20745
Inglewood, CA (90303)	18370
Inglewood, CA (90304)	20300
Inglewood, CA (90305)	12037
Lawndale, CA (90260)	25618
Los Angeles, CA (90001)	36200
Los Angeles, CA (90002)	30920
Los Angeles, CA (90003)	41878
Los Angeles, CA (90004)	41632
Los Angeles, CA (90005)	22281
Los Angeles, CA (90006)	34995
Los Angeles, CA (90007)	20179
Los Angeles, CA (90008)	21174
Los Angeles, CA (90010)	3294
Los Angeles, CA (90011)	63123
Los Angeles, CA (90012)	13839
Los Angeles, CA (90013)	3973
Los Angeles, CA (90014)	3272
Los Angeles, CA (90015)	10390
Los Angeles, CA (90016)	34391
Los Angeles, CA (90017)	11309
Los Angeles, CA (90018)	33029
Los Angeles, CA (90019)	43752
Los Angeles, CA (90020)	25029
Los Angeles, CA (90021)	1621
Los Angeles, CA (90022)	46198
Los Angeles, CA (90023)	30786
Los Angeles, CA (90024)	22009
Los Angeles, CA (90025)	34463
Los Angeles, CA (90026)	46916
Los Angeles, CA (90027)	33916
Los Angeles, CA (90028)	18687
Los Angeles, CA (90029)	26270
Los Angeles, CA (90031)	26797
Los Angeles, CA (90032)	32538
Los Angeles, CA (90033)	28923
Los Angeles, CA (90034)	42620
Los Angeles, CA (90035)	20647
Los Angeles, CA (90036)	26227
Los Angeles, CA (90037)	37811
Los Angeles, CA (90038)	18877
Los Angeles, CA (90039)	22944
Los Angeles, CA (90040)	9350
Los Angeles, CA (90041)	20920
Los Angeles, CA (90042)	43949
Los Angeles, CA (90043)	32064
Los Angeles, CA (90044)	56462
Los Angeles, CA (90045)	29336
Los Angeles, CA (90046)	34474
Los Angeles, CA (90047)	36265
Los Angeles, CA (90048)	17194
Los Angeles, CA (90049)	29275
Los Angeles, CA (90056)	7060
Los Angeles, CA (90057)	21531
Los Angeles, CA (90058)	2407
Los Angeles, CA (90059)	25507
Los Angeles, CA (90061)	18477
Los Angeles, CA (90062)	22057
Los Angeles, CA (90063)	35693
Los Angeles, CA (90064)	22483
Los Angeles, CA (90065)	34536
Los Angeles, CA (90066)	43203
Los Angeles, CA (90067)	5575
Los Angeles, CA (90068)	15853
West Hollywood, CA (90069)	17126
Los Angeles, CA (90071)	964
Los Angeles, CA (90077)	7412
Playa Vista, CA (90094)	3903
Lynwood, CA (90262)	47895
Malibu, CA (90265)	12992
Manhattan Beach, CA (90266)	30505
Pacific Palisades, CA (90272)	19526
Palos Verdes Peninsula, CA (90274)	24008
Rancho Palos Verdes, CA (90275)	35895
Hermosa Beach, CA (90254)	16137
Redondo Beach, CA (90277)	30038
Redondo Beach, CA (90278)	33427
Santa Monica, CA (90401)	4953
Santa Monica, CA (90402)	9702
Santa Monica, CA (90403)	20118
Santa Monica, CA (90404)	16220
Santa Monica, CA (90405)	22070
South Gate, CA (90280)	70212
Topanga, CA (90290)	5072
Venice, CA (90291)	20638
Marina Del Rey, CA (90292)	16888
Playa Del Rey, CA (90293)	9536
Acton, CA (93510)	6716
Agoura Hills, CA (91301)	22555
Oak Park, CA (91377)	12293
Altadena, CA (91001)	28725
Arcadia, CA (91006)	28021
Arcadia, CA (91007)	26674
Armona, CA (93202)	3054
Arroyo Grande, CA (93420)	22308
Arvin, CA (93203)	14589
Atascadero, CA (93422)	22551
Avenal, CA (93204)	6674
Bakersfield, CA (93301)	7620
Bakersfield, CA (93304)	30415
Bakersfield, CA (93305)	20671
Bakersfield, CA (93306)	43761
Bakersfield, CA (93307)	49152
Bakersfield, CA (93308)	34003
Bakersfield, CA (93309)	40902
Bakersfield, CA (93311)	30317
Bakersfield, CA (93312)	43353
Bakersfield, CA (93313)	31082
Bakersfield, CA (93314)	17646
Big Pine, CA (93513)	1370
Bishop, CA (93514)	10011
Bodfish, CA (93205)	1286
Boron, CA (93516)	1337
Bradley, CA (93426)	851
Bridgeport, CA (93517)	665
Buellton, CA (93427)	4914
Burbank, CA (91501)	16002
Burbank, CA (91502)	8245
Burbank, CA (91504)	20413
Burbank, CA (91505)	25892
Burbank, CA (91506)	15393
Buttonwillow, CA (93206)	1766
Caliente, CA (93518)	828
Camarillo, CA (93010)	34198
Camarillo, CA (93012)	28348
Cambria, CA (93428)	5624
Canoga Park, CA (91303)	17718
Canoga Park, CA (91304)	37168
Winnetka, CA (91306)	34013
West Hills, CA (91307)	20778
Carpinteria, CA (93013)	12862
Cayucos, CA (93430)	2539
Chatsworth, CA (91311)	29782
Coalinga, CA (93210)	9762
Corcoran, CA (93212)	9472
Creston, CA (93432)	1200
Delano, CA (93215)	29597
Duarte, CA (91008)	879
Duarte, CA (91010)	20593
Earlimart, CA (93219)	6744
Edwards, CA (93523)	2354
Exeter, CA (93221)	10596
Farmersville, CA (93223)	6716
Fillmore, CA (93015)	12620
Frazier Park, CA (93225)	3778
Glendale, CA (91201)	17448
Glendale, CA (91202)	17687
Glendale, CA (91203)	10833
Glendale, CA (91204)	11153
Glendale, CA (91205)	27150
Glendale, CA (91206)	25063
Glendale, CA (91207)	8398
Glendale, CA (91208)	13555
La Crescenta, CA (91214)	25651
Grover Beach, CA (93433)	8974
Guadalupe, CA (93434)	5126
Hanford, CA (93230)	45031
Huron, CA (93234)	4538
Independence, CA (93526)	544
Inyokern, CA (93527)	1719
Ivanhoe, CA (93235)	3130
June Lake, CA (93529)	491
Keene, CA (93531)	484
Kernville, CA (93238)	1354
Kettleman City, CA (93239)	1229
La Canada Flintridge, CA (91011)	18197
Lake Hughes, CA (93532)	2088
Lake Isabella, CA (93240)	4066
Lamont, CA (93241)	11327
Lancaster, CA (93534)	24548
Lancaster, CA (93535)	45851
Lancaster, CA (93536)	48248
Laton, CA (93242)	2736
Lebec, CA (93243)	1151
Lemoore, CA (93245)	26596
Lindsay, CA (93247)	11680
Littlerock, CA (93543)	9046
Llano, CA (93544)	767
Lompoc, CA (93436)	36741
Lompoc, CA (93437)	2943
Lone Pine, CA (93545)	1557
Lost Hills, CA (93249)	2120
Mc Farland, CA (93250)	8129
Mammoth Lakes, CA (93546)	6723
Maricopa, CA (93252)	1110
Mojave, CA (93501)	3030
California City, CA (93505)	7123
Monrovia, CA (91016)	31187
Montrose, CA (91020)	5930
Moorpark, CA (93021)	30875
Morro Bay, CA (93442)	7761
New Cuyama, CA (93254)	626
Nipomo, CA (93444)	15501
North Hollywood, CA (91601)	25821
North Hollywood, CA (91602)	13969
Studio City, CA (91604)	23076
North Hollywood, CA (91605)	39700
North Hollywood, CA (91606)	32275
Valley Village, CA (91607)	21208
Northridge, CA (91324)	20401
Northridge, CA (91325)	24201
Porter Ranch, CA (91326)	28058
Oak View, CA (93022)	5190
Oceano, CA (93445)	4497
Ojai, CA (93023)	15623
Oxnard, CA (93030)	45834
Oxnard, CA (93033)	65653
Oxnard, CA (93035)	21701
Oxnard, CA (93036)	29528
Pacoima, CA (91331)	72872
Palmdale, CA (93550)	48104
Palmdale, CA (93551)	39678
Palmdale, CA (93552)	26212
Palmdale, CA (93591)	4371
Pasadena, CA (91101)	13258
Pasadena, CA (91103)	18714
Pasadena, CA (91104)	27268
Pasadena, CA (91105)	9563
Pasadena, CA (91106)	17783
Pasadena, CA (91107)	26912
San Marino, CA (91108)	12520
Paso Robles, CA (93446)	32009
Pearblossom, CA (93553)	1419
Pismo Beach, CA (93449)	6223
Pixley, CA (93256)	3390
Porterville, CA (93257)	46960
Port Hueneme, CA (93041)	16854
Reseda, CA (91335)	54011
Ridgecrest, CA (93555)	24004
Rosamond, CA (93560)	13552
San Fernando, CA (91340)	25093
Sylmar, CA (91342)	66238
North Hills, CA (91343)	41190
Granada Hills, CA (91344)	41602
Mission Hills, CA (91345)	14142
San Luis Obispo, CA (93401)	19714
Los Osos, CA (93402)	11297
San Luis Obispo, CA (93405)	11172
San Miguel, CA (93451)	2916
Santa Barbara, CA (93101)	21615
Santa Barbara, CA (93103)	13621
Santa Barbara, CA (93105)	19652
Santa Barbara, CA (93108)	8500
Santa Barbara, CA (93109)	8228
Santa Barbara, CA (93110)	12594
Santa Barbara, CA (93111)	15066
Goleta, CA (93117)	26958
Newhall, CA (91321)	24843
Santa Clarita, CA (91350)	27783
Canyon Country, CA (91351)	25962
Valencia, CA (91354)	22704
Valencia, CA (91355)	26548
Stevenson Ranch, CA (91381)	15678
Castaic, CA (91384)	18686
Canyon Country, CA (91387)	30434
Santa Clarita, CA (91390)	15765
Santa Margarita, CA (93453)	2396
Santa Maria, CA (93454)	24768
Santa Maria, CA (93455)	33212
Santa Maria, CA (93458)	35006
Santa Paula, CA (93060)	24908
Santa Ynez, CA (93460)	5209
Shafter, CA (93263)	12989
Shandon, CA (93461)	1254
Sierra Madre, CA (91024)	8990
Simi Valley, CA (93063)	45423
Simi Valley, CA (93065)	59551
Solvang, CA (93463)	5699
Somis, CA (93066)	2974
South Pasadena, CA (91030)	20953
Springville, CA (93265)	3031
Stratford, CA (93266)	1255
Strathmore, CA (93267)	4456
Sunland, CA (91040)	16036
Sun Valley, CA (91352)	35055
Taft, CA (93268)	10210
Tarzana, CA (91356)	23015
Tehachapi, CA (93561)	21006
Templeton, CA (93465)	8127
Terra Bella, CA (93270)	4678
Newbury Park, CA (91320)	37943
Thousand Oaks, CA (91360)	35014
Westlake Village, CA (91361)	18019
Thousand Oaks, CA (91362)	31759
Three Rivers, CA (93271)	1879
Tipton, CA (93272)	2780
Trona, CA (93562)	1017
Tujunga, CA (91042)	20436
Tulare, CA (93274)	46216
Encino, CA (91316)	21973
Van Nuys, CA (91401)	28864
Panorama City, CA (91402)	45198
Sherman Oaks, CA (91403)	19914
Van Nuys, CA (91405)	34500
Van Nuys, CA (91406)	37193
Van Nuys, CA (91411)	15715
Sherman Oaks, CA (91423)	24736
Encino, CA (91436)	15771
Ventura, CA (93001)	23874
Ventura, CA (93003)	39626
Ventura, CA (93004)	23167
Visalia, CA (93277)	36340
Visalia, CA (93291)	33290
Visalia, CA (93292)	26810
Wasco, CA (93280)	14256
Weldon, CA (93283)	1178
Wofford Heights, CA (93285)	1528
Woodlake, CA (93286)	6406
Calabasas, CA (91302)	22015
Woodland Hills, CA (91364)	21888
Woodland Hills, CA (91367)	31168
Adelanto, CA (92301)	18944
Aguanga, CA (92536)	2501
Alpine, CA (91901)	12512
Angelus Oaks, CA (92305)	521
Anza, CA (92539)	2965
Apple Valley, CA (92307)	28280
Apple Valley, CA (92308)	26211
Baker, CA (92309)	597
Banning, CA (92220)	21934
Fort Irwin, CA (92310)	6090
Barstow, CA (92311)	21613
Beaumont, CA (92223)	31758
Big Bear City, CA (92314)	6104
Big Bear Lake, CA (92315)	6550
Bloomington, CA (92316)	22380
Blythe, CA (92225)	10038
Bonita, CA (91902)	14985
Bonsall, CA (92003)	4661
Borrego Springs, CA (92004)	2493
Boulevard, CA (91905)	1106
Brawley, CA (92227)	18589
Cabazon, CA (92230)	1532
Whitewater, CA (92282)	526
Calexico, CA (92231)	46865
Calimesa, CA (92320)	6035
Calipatria, CA (92233)	2671
Campo, CA (91906)	2441
Carlsbad, CA (92008)	22311
Carlsbad, CA (92009)	34502
Carlsbad, CA (92010)	11702
Carlsbad, CA (92011)	18094
Cathedral City, CA (92234)	34119
Chula Vista, CA (91910)	60383
Chula Vista, CA (91911)	66861
Chula Vista, CA (91913)	31558
Chula Vista, CA (91914)	12078
Chula Vista, CA (91915)	19456
Coachella, CA (92236)	28536
Grand Terrace, CA (92313)	9454
Colton, CA (92324)	40776
Daggett, CA (92327)	457
Del Mar, CA (92014)	12635
Descanso, CA (91916)	1514
Desert Hot Springs, CA (92240)	22246
Desert Hot Springs, CA (92241)	4216
Dulzura, CA (91917)	812
Earp, CA (92242)	796
El Cajon, CA (92019)	33606
El Cajon, CA (92020)	39637
El Cajon, CA (92021)	47937
El Centro, CA (92243)	34586
Cardiff By The Sea, CA (92007)	9394
Encinitas, CA (92024)	40737
Escondido, CA (92025)	32894
Escondido, CA (92026)	37252
Escondido, CA (92027)	39399
Escondido, CA (92029)	15470
Fallbrook, CA (92028)	35647
Fontana, CA (92335)	65832
Fontana, CA (92336)	66178
Fontana, CA (92337)	27988
Forest Falls, CA (92339)	792
Heber, CA (92249)	5698
Helendale, CA (92342)	4734
Hemet, CA (92543)	19884
Hemet, CA (92544)	30633
Hemet, CA (92545)	26648
Hesperia, CA (92344)	13963
Hesperia, CA (92345)	52569
Highland, CA (92346)	40992
Hinkley, CA (92347)	996
Holtville, CA (92250)	6337
Homeland, CA (92548)	4175
Idyllwild, CA (92549)	3099
Imperial, CA (92251)	12786
Imperial Beach, CA (91932)	19955
Indio, CA (92201)	41028
Indio, CA (92203)	16919
Jacumba, CA (91934)	495
Jamul, CA (91935)	7716
Joshua Tree, CA (92252)	6160
Julian, CA (92036)	2805
La Jolla, CA (92037)	30981
Lake Elsinore, CA (92530)	33145
Lake Elsinore, CA (92532)	12454
Lakeside, CA (92040)	32995
La Mesa, CA (91941)	35288
La Mesa, CA (91942)	19254
La Quinta, CA (92253)	26303
Lemon Grove, CA (91945)	19359
Loma Linda, CA (92354)	15275
Lucerne Valley, CA (92356)	3770
Lytle Creek, CA (92358)	603
Mecca, CA (92254)	11107
Mentone, CA (92359)	6159
Moreno Valley, CA (92551)	21024
Moreno Valley, CA (92553)	48194
Moreno Valley, CA (92555)	26702
Moreno Valley, CA (92557)	36328
Morongo Valley, CA (92256)	2399
Mountain Center, CA (92561)	936
Murrieta, CA (92562)	45927
Murrieta, CA (92563)	41578
National City, CA (91950)	41162
Needles, CA (92363)	3538
Newberry Springs, CA (92365)	1494
Niland, CA (92257)	1055
Nuevo, CA (92567)	6743
Oceanside, CA (92054)	29573
Camp Pendleton, CA (92055)	6130
Oceanside, CA (92056)	42843
Oceanside, CA (92057)	43857
Oceanside, CA (92058)	27368
Oro Grande, CA (92368)	552
Indian Wells, CA (92210)	3236
Palm Desert, CA (92211)	18234
Palm Desert, CA (92260)	21470
Palm Springs, CA (92262)	17175
Palm Springs, CA (92264)	12753
Pala, CA (92059)	1305
Pauma Valley, CA (92061)	2444
Perris, CA (92570)	33297
Perris, CA (92571)	33736
Phelan, CA (92371)	6321
Pine Valley, CA (91962)	1651
Pinon Hills, CA (92372)	3747
Potrero, CA (91963)	1054
Poway, CA (92064)	40359
Ramona, CA (92065)	28767
Rancho Mirage, CA (92270)	12970
Rancho Santa Fe, CA (92091)	890
Redlands, CA (92373)	26330
Redlands, CA (92374)	29406
Rialto, CA (92376)	55471
Rialto, CA (92377)	16892
Riverside, CA (92501)	13444
Riverside, CA (92503)	61219
Riverside, CA (92504)	37665
Riverside, CA (92505)	32679
Riverside, CA (92506)	35060
Riverside, CA (92507)	32114
Riverside, CA (92508)	26006
Riverside, CA (92509)	53031
March Air Reserve Base, CA (92518)	1020
San Bernardino, CA (92401)	1426
San Bernardino, CA (92404)	37086
San Bernardino, CA (92405)	18868
San Bernardino, CA (92407)	37108
San Bernardino, CA (92408)	8883
San Bernardino, CA (92410)	29872
San Bernardino, CA (92411)	17344
San Diego, CA (92101)	21606
San Diego, CA (92102)	29464
San Diego, CA (92103)	24568
San Diego, CA (92104)	32533
San Diego, CA (92105)	45433
San Diego, CA (92106)	15576
San Diego, CA (92107)	21395
San Diego, CA (92108)	14070
San Diego, CA (92109)	32741
San Diego, CA (92110)	18233
San Diego, CA (92111)	34112
San Diego, CA (92113)	32148
San Diego, CA (92114)	50254
San Diego, CA (92115)	36221
San Diego, CA (92116)	24400
San Diego, CA (92117)	40891
Coronado, CA (92118)	13928
San Diego, CA (92119)	19213
San Diego, CA (92120)	22173
San Diego, CA (92121)	3933
San Diego, CA (92122)	29139
San Diego, CA (92123)	21442
San Diego, CA (92124)	23756
San Diego, CA (92126)	57845
San Diego, CA (92127)	30553
San Diego, CA (92128)	40522
San Diego, CA (92129)	43907
San Diego, CA (92130)	40642
San Diego, CA (92131)	30124
San Diego, CA (92135)	523
San Diego, CA (92139)	28551
San Diego, CA (92154)	67736
San Ysidro, CA (92173)	37591
San Jacinto, CA (92582)	9984
San Jacinto, CA (92583)	18842
San Marcos, CA (92069)	34357
San Marcos, CA (92078)	31603
Santa Ysabel, CA (92070)	972
Santee, CA (92071)	42808
Solana Beach, CA (92075)	10911
Spring Valley, CA (91977)	44239
Spring Valley, CA (91978)	7267
Menifee, CA (92584)	28269
Sun City, CA (92585)	12616
Sun City, CA (92586)	15299
Sun City, CA (92587)	12535
Tecate, CA (91980)	1985
Temecula, CA (92590)	2592
Temecula, CA (92591)	29508
Temecula, CA (92592)	53769
Thermal, CA (92274)	11251
Thousand Palms, CA (92276)	5380
Twentynine Palms, CA (92277)	16226
Twentynine Palms, CA (92278)	2701
Valley Center, CA (92082)	15502
Victorville, CA (92392)	37842
Victorville, CA (92394)	18928
Victorville, CA (92395)	26559
Vista, CA (92081)	21220
Vista, CA (92083)	25707
Vista, CA (92084)	34654
Warner Springs, CA (92086)	1068
Westmorland, CA (92281)	1694
Wildomar, CA (92595)	23090
Winchester, CA (92596)	16229
Winterhaven, CA (92283)	2269
Wrightwood, CA (92397)	4357
Yucaipa, CA (92399)	39430
Yucca Valley, CA (92284)	15762
Landers, CA (92285)	1274
Alhambra, CA (91801)	41211
Alhambra, CA (91803)	24399
Anaheim, CA (92801)	45683
Anaheim, CA (92802)	29583
Anaheim, CA (92804)	61315
Anaheim, CA (92805)	50587
Anaheim, CA (92806)	28271
Anaheim, CA (92807)	31116
Anaheim, CA (92808)	16631
Anaheim, CA (92809)	495
Artesia, CA (90701)	12730
Cerritos, CA (90703)	44208
Azusa, CA (91702)	42119
Baldwin Park, CA (91706)	57507
Bellflower, CA (90706)	54431
Brea, CA (92821)	29617
Brea, CA (92823)	3045
Buena Park, CA (90620)	36788
Buena Park, CA (90621)	26086
La Palma, CA (90623)	13178
Chino, CA (91708)	4617
Chino, CA (91710)	56083
Chino Hills, CA (91709)	62987
Claremont, CA (91711)	27155
Corona, CA (92879)	34375
Corona, CA (92880)	42387
Corona, CA (92881)	23308
Corona, CA (92882)	50624
Corona, CA (92883)	22253
Corona Del Mar, CA (92625)	10985
Costa Mesa, CA (92626)	37365
Costa Mesa, CA (92627)	44941
Covina, CA (91722)	28046
Covina, CA (91723)	13780
Covina, CA (91724)	20668
Cypress, CA (90630)	41132
Capistrano Beach, CA (92624)	6064
Dana Point, CA (92629)	22860
El Monte, CA (91731)	20017
El Monte, CA (91732)	43596
South El Monte, CA (91733)	31052
Lake Forest, CA (92630)	50173
Fullerton, CA (92831)	24136
Fullerton, CA (92832)	17075
Fullerton, CA (92833)	39597
Fullerton, CA (92835)	20003
Garden Grove, CA (92840)	40332
Garden Grove, CA (92841)	24588
Garden Grove, CA (92843)	33276
Garden Grove, CA (92844)	17495
Garden Grove, CA (92845)	14081
Glendora, CA (91740)	20434
Glendora, CA (91741)	21524
Harbor City, CA (90710)	19537
Huntington Beach, CA (92646)	47363
Huntington Beach, CA (92647)	44920
Huntington Beach, CA (92648)	36978
Huntington Beach, CA (92649)	27766
Irvine, CA (92602)	17238
Irvine, CA (92603)	16155
Irvine, CA (92604)	22273
Irvine, CA (92606)	16267
Irvine, CA (92612)	16945
Irvine, CA (92614)	19513
Irvine, CA (92617)	4977
Irvine, CA (92618)	12059
Irvine, CA (92620)	31192
Laguna Woods, CA (92637)	13491
Laguna Beach, CA (92651)	19615
Laguna Hills, CA (92653)	26019
Aliso Viejo, CA (92656)	39419
Laguna Niguel, CA (92677)	53608
La Habra, CA (90631)	52341
Lakewood, CA (90712)	25989
Lakewood, CA (90713)	23966
Lakewood, CA (90715)	15741
Hawaiian Gardens, CA (90716)	10379
La Mirada, CA (90638)	37827
La Puente, CA (91744)	63301
Hacienda Heights, CA (91745)	44875
La Puente, CA (91746)	23468
Rowland Heights, CA (91748)	37487
La Verne, CA (91750)	27750
Lomita, CA (90717)	16628
Carson, CA (90745)	46022
Carson, CA (90746)	20834
Signal Hill, CA (90755)	8468
Long Beach, CA (90802)	25106
Long Beach, CA (90803)	25619
Long Beach, CA (90804)	26726
Long Beach, CA (90805)	66158
Long Beach, CA (90806)	29624
Long Beach, CA (90807)	26420
Long Beach, CA (90808)	33131
Long Beach, CA (90810)	27824
Long Beach, CA (90813)	34994
Long Beach, CA (90814)	13995
Long Beach, CA (90815)	31234
Los Alamitos, CA (90720)	19065
Mira Loma, CA (91752)	21577
Montclair, CA (91763)	27063
Montebello, CA (90640)	46577
Monterey Park, CA (91754)	28166
Monterey Park, CA (91755)	21491
Newport Coast, CA (92657)	8448
Newport Beach, CA (92660)	28529
Newport Beach, CA (92661)	2915
Newport Beach, CA (92662)	2438
Newport Beach, CA (92663)	15815
Norco, CA (92860)	18965
Norwalk, CA (90650)	78458
Ontario, CA (91761)	44442
Ontario, CA (91762)	42661
Ontario, CA (91764)	38261
Villa Park, CA (92861)	5228
Orange, CA (92865)	15604
Orange, CA (92866)	11381
Orange, CA (92867)	34563
Orange, CA (92868)	16174
Orange, CA (92869)	31173
Paramount, CA (90723)	38558
Pico Rivera, CA (90660)	48568
Placentia, CA (92870)	41874
Diamond Bar, CA (91765)	41453
Pomona, CA (91766)	49778
Pomona, CA (91767)	33720
Pomona, CA (91768)	22349
Rancho Cucamonga, CA (91701)	33269
Rancho Cucamonga, CA (91730)	48152
Rancho Cucamonga, CA (91737)	20165
Rancho Cucamonga, CA (91739)	25587
Rosemead, CA (91770)	49163
San Clemente, CA (92672)	29908
San Clemente, CA (92673)	24536
San Dimas, CA (91773)	28256
San Gabriel, CA (91775)	19902
San Gabriel, CA (91776)	30178
San Juan Capistrano, CA (92675)	27693
Mission Viejo, CA (92691)	40492
Mission Viejo, CA (92692)	40945
Ladera Ranch, CA (92694)	17998
San Pedro, CA (90731)	40560
San Pedro, CA (90732)	17285
Santa Ana, CA (92701)	35900
Santa Ana, CA (92703)	48715
Santa Ana, CA (92704)	67361
Santa Ana, CA (92705)	36122
Santa Ana, CA (92706)	27773
Santa Ana, CA (92707)	48517
Fountain Valley, CA (92708)	46913
Santa Ana, CA (92799)	977
Santa Fe Springs, CA (90670)	12163
Seal Beach, CA (90740)	20646
Silverado, CA (92676)	1608
Stanton, CA (90680)	23093
Temple City, CA (91780)	29368
Torrance, CA (90501)	33170
Torrance, CA (90502)	14193
Torrance, CA (90503)	36775
Torrance, CA (90504)	27310
Torrance, CA (90505)	31058
Foothill Ranch, CA (92610)	9499
Trabuco Canyon, CA (92679)	28044
Rancho Santa Margarita, CA (92688)	36571
Tustin, CA (92780)	42492
Tustin, CA (92782)	19295
Upland, CA (91784)	22685
Upland, CA (91786)	36960
Walnut, CA (91789)	37363
West Covina, CA (91790)	33820
West Covina, CA (91791)	25715
West Covina, CA (91792)	23683
Midway City, CA (92655)	6304
Westminster, CA (92683)	70715
Whittier, CA (90601)	24177
Whittier, CA (90602)	17609
Whittier, CA (90603)	16292
Whittier, CA (90604)	29676
Whittier, CA (90605)	30900
Whittier, CA (90606)	24569
Wilmington, CA (90744)	37822
Yorba Linda, CA (92886)	39360
Yorba Linda, CA (92887)	18153
Albion, CA (95410)	676
Mckinleyville, CA (95519)	12766
Arcata, CA (95521)	10982
Bayside, CA (95524)	1740
Belmont, CA (94002)	23092
Belvedere Tiburon, CA (94920)	10900
Blue Lake, CA (95525)	1405
Bodega Bay, CA (94923)	1169
Bolinas, CA (94924)	1151
Boonville, CA (95415)	1236
Brisbane, CA (94005)	4345
Burlingame, CA (94010)	35172
Carlotta, CA (95528)	754
Cazadero, CA (95421)	1034
Clearlake, CA (95422)	7530
Clearlake Oaks, CA (95423)	2370
Cloverdale, CA (95425)	8841
Corte Madera, CA (94925)	8134
Rohnert Park, CA (94928)	30371
Cotati, CA (94931)	7260
Covelo, CA (95428)	1328
Crescent City, CA (95531)	14062
Daly City, CA (94014)	36989
Daly City, CA (94015)	49650
Eureka, CA (95501)	14321
Eureka, CA (95503)	16695
Fairfax, CA (94930)	6948
Ferndale, CA (95536)	2338
Forestville, CA (95436)	4585
Fort Bragg, CA (95437)	11000
Fortuna, CA (95540)	9910
Fulton, CA (95439)	838
Garberville, CA (95542)	1468
Gasquet, CA (95543)	494
Geyserville, CA (95441)	2362
Glen Ellen, CA (95442)	2862
Graton, CA (95444)	1154
Gualala, CA (95445)	2247
Guerneville, CA (95446)	3558
Half Moon Bay, CA (94019)	12963
Healdsburg, CA (95448)	14838
Hoopa, CA (95546)	1777
Hopland, CA (95449)	1330
Hydesville, CA (95547)	1029
Inverness, CA (94937)	867
Kelseyville, CA (95451)	8100
Kenwood, CA (95452)	1581
Klamath, CA (95548)	716
Kneeland, CA (95549)	635
La Honda, CA (94020)	1307
Lakeport, CA (95453)	7976
Larkspur, CA (94939)	5652
Laytonville, CA (95454)	1687
Little River, CA (95456)	540
Loleta, CA (95551)	1088
Los Altos, CA (94022)	17620
Los Altos, CA (94024)	20665
Lower Lake, CA (95457)	2786
Lucerne, CA (95458)	1687
Mendocino, CA (95460)	2343
Menlo Park, CA (94025)	32613
Atherton, CA (94027)	6145
Portola Valley, CA (94028)	6281
Middletown, CA (95461)	2984
Hidden Valley Lake, CA (95467)	3858
Millbrae, CA (94030)	18869
Mill Valley, CA (94941)	25742
Monte Rio, CA (95462)	836
Moss Beach, CA (94038)	2425
Mountain View, CA (94040)	26205
Mountain View, CA (94041)	10999
Mountain View, CA (94043)	22824
Nicasio, CA (94946)	551
Nice, CA (95464)	1536
Novato, CA (94945)	14293
Novato, CA (94947)	19940
Novato, CA (94949)	14246
Occidental, CA (95465)	1774
Pacifica, CA (94044)	32334
Palo Alto, CA (94301)	14401
Palo Alto, CA (94303)	34099
Palo Alto, CA (94304)	2781
Stanford, CA (94305)	5084
Palo Alto, CA (94306)	22810
Penngrove, CA (94951)	3579
Pescadero, CA (94060)	1410
Petaluma, CA (94952)	25794
Petaluma, CA (94954)	31071
Philo, CA (95466)	1058
Point Arena, CA (95468)	978
Point Reyes Station, CA (94956)	1406
Potter Valley, CA (95469)	1399
Redway, CA (95560)	1680
Redwood City, CA (94061)	27970
Redwood City, CA (94062)	22552
Redwood City, CA (94063)	21866
Redwood City, CA (94065)	10134
Redwood Valley, CA (95470)	4791
Rio Dell, CA (95562)	2147
San Anselmo, CA (94960)	12561
San Bruno, CA (94066)	35122
San Carlos, CA (94070)	26469
San Francisco, CA (94102)	16733
San Francisco, CA (94103)	16260
San Francisco, CA (94104)	1959
San Francisco, CA (94105)	5271
San Francisco, CA (94107)	19741
San Francisco, CA (94108)	10020
San Francisco, CA (94109)	38763
San Francisco, CA (94110)	53093
San Francisco, CA (94111)	3905
San Francisco, CA (94112)	64941
San Francisco, CA (94114)	26380
San Francisco, CA (94115)	24064
San Francisco, CA (94116)	37668
San Francisco, CA (94117)	27878
San Francisco, CA (94118)	30630
San Francisco, CA (94121)	34786
San Francisco, CA (94122)	46850
San Francisco, CA (94123)	19132
San Francisco, CA (94124)	24380
San Francisco, CA (94127)	17250
San Francisco, CA (94128)	683
San Francisco, CA (94129)	2542
San Francisco, CA (94130)	1387
San Francisco, CA (94131)	22759
San Francisco, CA (94132)	19425
San Francisco, CA (94133)	20583
San Francisco, CA (94134)	32983
San Francisco, CA (94158)	2706
San Mateo, CA (94401)	25273
San Mateo, CA (94402)	21898
San Mateo, CA (94403)	33305
San Mateo, CA (94404)	29611
San Rafael, CA (94901)	33561
San Rafael, CA (94903)	23974
Greenbrae, CA (94904)	10158
Santa Rosa, CA (95401)	26704
Santa Rosa, CA (95403)	33257
Santa Rosa, CA (95404)	29799
Santa Rosa, CA (95405)	18155
Santa Rosa, CA (95407)	26764
Santa Rosa, CA (95409)	21790
Sausalito, CA (94965)	9393
Scotia, CA (95565)	853
Sebastopol, CA (95472)	21680
Smith River, CA (95567)	1663
Sonoma, CA (95476)	24893
South San Francisco, CA (94080)	53242
Stinson Beach, CA (94970)	583
Sunnyvale, CA (94085)	16831
Sunnyvale, CA (94086)	37637
Sunnyvale, CA (94087)	46300
Sunnyvale, CA (94089)	16628
Trinidad, CA (95570)	1922
Ukiah, CA (95482)	21879
Upper Lake, CA (95485)	1933
Whitethorn, CA (95589)	712
Willits, CA (95490)	9434
Willow Creek, CA (95573)	1299
Windsor, CA (95492)	23814
Alameda, CA (94501)	48387
Alameda, CA (94502)	12235
Alamo, CA (94507)	14041
Angwin, CA (94508)	2362
Antioch, CA (94509)	45524
Antioch, CA (94531)	31488
Aptos, CA (95003)	18954
Aromas, CA (95004)	3420
Benicia, CA (94510)	23802
Ben Lomond, CA (95005)	5137
Berkeley, CA (94702)	12254
Berkeley, CA (94703)	13904
Berkeley, CA (94704)	6826
Berkeley, CA (94705)	10879
Albany, CA (94706)	15637
Berkeley, CA (94707)	11820
Berkeley, CA (94708)	10062
Berkeley, CA (94709)	6899
Berkeley, CA (94710)	5142
Big Sur, CA (93920)	1072
Boulder Creek, CA (95006)	7182
Brentwood, CA (94513)	42684
Discovery Bay, CA (94505)	9925
Byron, CA (94514)	1729
Calistoga, CA (94515)	5845
Campbell, CA (95008)	36168
Capitola, CA (95010)	7918
Carmel, CA (93923)	8358
Carmel Valley, CA (93924)	5275
Castroville, CA (95012)	8542
Chualar, CA (93925)	1743
Clayton, CA (94517)	11352
Concord, CA (94518)	21464
Concord, CA (94519)	14804
Concord, CA (94520)	26131
Concord, CA (94521)	34763
Pleasant Hill, CA (94523)	27947
Crockett, CA (94525)	2510
Cupertino, CA (95014)	51349
Danville, CA (94506)	20743
Danville, CA (94526)	28860
Davenport, CA (95017)	718
El Cerrito, CA (94530)	21140
Fairfield, CA (94533)	51145
Fairfield, CA (94534)	30105
Travis Afb, CA (94535)	4193
Felton, CA (95018)	6114
Freedom, CA (95019)	7068
Fremont, CA (94536)	55569
Fremont, CA (94538)	49149
Fremont, CA (94539)	44440
Fremont, CA (94555)	28222
Gilroy, CA (95020)	41952
Gonzales, CA (93926)	8139
Greenfield, CA (93927)	12788
Hayward, CA (94541)	44424
Hayward, CA (94542)	9246
Hayward, CA (94544)	55190
Hayward, CA (94545)	24681
Castro Valley, CA (94546)	35351
Castro Valley, CA (94552)	13039
Hollister, CA (95023)	35971
King City, CA (93930)	12376
Lafayette, CA (94549)	24865
Livermore, CA (94550)	40153
Livermore, CA (94551)	32376
Los Gatos, CA (95030)	11508
Los Gatos, CA (95032)	21990
Los Gatos, CA (95033)	7196
Marina, CA (93933)	16444
Martinez, CA (94553)	38654
Milpitas, CA (95035)	54420
Monterey, CA (93940)	22581
Moraga, CA (94556)	13735
Morgan Hill, CA (95037)	35452
Moss Landing, CA (95039)	1267
Napa, CA (94558)	54496
Napa, CA (94559)	21017
Newark, CA (94560)	35570
Oakland, CA (94601)	33456
Oakland, CA (94602)	22480
Oakland, CA (94603)	21407
Oakland, CA (94605)	28141
Oakland, CA (94606)	25875
Oakland, CA (94607)	14897
Emeryville, CA (94608)	18425
Oakland, CA (94609)	14227
Oakland, CA (94610)	24162
Oakland, CA (94611)	32155
Oakland, CA (94612)	8710
Oakland, CA (94618)	13888
Oakland, CA (94619)	18775
Oakland, CA (94621)	18680
Oakley, CA (94561)	27185
Orinda, CA (94563)	17132
Pacific Grove, CA (93950)	12550
Paicines, CA (95043)	494
Pebble Beach, CA (93953)	3861
Pinole, CA (94564)	15898
Pittsburg, CA (94565)	61968
Pleasanton, CA (94566)	37329
Dublin, CA (94568)	34457
Pleasanton, CA (94588)	28137
Pope Valley, CA (94567)	537
Richmond, CA (94801)	18180
El Sobrante, CA (94803)	20102
Richmond, CA (94804)	26686
Richmond, CA (94805)	10551
San Pablo, CA (94806)	43290
Rio Vista, CA (94571)	6699
Hercules, CA (94547)	20527
Rodeo, CA (94572)	6725
Saint Helena, CA (94574)	7143
Salinas, CA (93901)	19097
Salinas, CA (93905)	49791
Salinas, CA (93906)	42006
Salinas, CA (93907)	16466
Salinas, CA (93908)	11306
San Jose, CA (95110)	12621
San Jose, CA (95111)	43578
San Jose, CA (95112)	34111
San Jose, CA (95113)	1049
San Jose, CA (95116)	35357
San Jose, CA (95117)	22030
San Jose, CA (95118)	26249
San Jose, CA (95119)	8171
San Jose, CA (95120)	33486
San Jose, CA (95121)	30427
San Jose, CA (95122)	41936
San Jose, CA (95123)	50481
San Jose, CA (95124)	39234
San Jose, CA (95125)	41048
San Jose, CA (95126)	23076
San Jose, CA (95127)	46641
San Jose, CA (95128)	25327
San Jose, CA (95129)	32839
San Jose, CA (95130)	10841
San Jose, CA (95131)	24403
San Jose, CA (95132)	34344
San Jose, CA (95133)	20337
San Jose, CA (95134)	12670
San Jose, CA (95135)	17221
San Jose, CA (95136)	35078
San Jose, CA (95138)	15421
San Jose, CA (95139)	5634
San Jose, CA (95148)	37541
San Juan Bautista, CA (95045)	3345
San Leandro, CA (94577)	37421
San Leandro, CA (94578)	28085
San Leandro, CA (94579)	17524
San Lorenzo, CA (94580)	22564
San Martin, CA (95046)	5514
San Ramon, CA (94582)	29033
San Ramon, CA (94583)	40007
Santa Clara, CA (95050)	26714
Santa Clara, CA (95051)	45397
Santa Clara, CA (95054)	20797
Santa Cruz, CA (95060)	29968
Santa Cruz, CA (95062)	26530
Santa Cruz, CA (95064)	890
Santa Cruz, CA (95065)	6525
Scotts Valley, CA (95066)	11926
Saratoga, CA (95070)	29525
Seaside, CA (93955)	24162
Soledad, CA (93960)	12698
Soquel, CA (95073)	9169
Suisun City, CA (94585)	22796
Sunol, CA (94586)	937
Tres Pinos, CA (95075)	603
Union City, CA (94587)	57184
American Canyon, CA (94503)	15188
Vallejo, CA (94589)	22142
Vallejo, CA (94590)	25368
Vallejo, CA (94591)	42764
Vallejo, CA (94592)	553
Walnut Creek, CA (94595)	14774
Walnut Creek, CA (94596)	18125
Walnut Creek, CA (94597)	16977
Walnut Creek, CA (94598)	23862
Watsonville, CA (95076)	63437
Yountville, CA (94599)	2713
Acampo, CA (95220)	5450
Ahwahnee, CA (93601)	1527
Anderson, CA (96007)	16199
Angels Camp, CA (95222)	2943
Applegate, CA (95703)	1447
Arbuckle, CA (95912)	4260
Arnold, CA (95223)	3417
Atwater, CA (95301)	25056
Auberry, CA (93602)	2778
Auburn, CA (95602)	13927
Auburn, CA (95603)	20376
Ballico, CA (95303)	789
Bangor, CA (95914)	691
Bass Lake, CA (93604)	662
Bella Vista, CA (96008)	1500
Berry Creek, CA (95916)	931
Biggs, CA (95917)	2534
Browns Valley, CA (95918)	1810
Brownsville, CA (95919)	914
Burney, CA (96013)	3131
Camino, CA (95709)	4150
Cantua Creek, CA (93608)	1102
Carmichael, CA (95608)	45450
Caruthers, CA (93609)	4374
Catheys Valley, CA (95306)	781
Shasta Lake, CA (96019)	6917
Ceres, CA (95307)	30984
Chester, CA (96020)	2304
Chico, CA (95926)	22651
Chico, CA (95928)	22333
Chico, CA (95973)	23889
Chowchilla, CA (93610)	11048
Citrus Heights, CA (95610)	32886
Citrus Heights, CA (95621)	31963
Clarksburg, CA (95612)	1189
Clovis, CA (93611)	36239
Clovis, CA (93612)	24053
Clovis, CA (93619)	23064
Coarsegold, CA (93614)	9131
Colfax, CA (95713)	6066
Columbia, CA (95310)	1996
Colusa, CA (95932)	6178
Cool, CA (95614)	3415
Copperopolis, CA (95228)	3161
Corning, CA (96021)	11110
Cottonwood, CA (96022)	11976
Coulterville, CA (95311)	1402
Courtland, CA (95615)	753
Crows Landing, CA (95313)	1400
Cutler, CA (93615)	4111
Davis, CA (95616)	25761
Davis, CA (95618)	17799
Delhi, CA (95315)	8952
Del Rey, CA (93616)	1990
Denair, CA (95316)	5470
Diamond Springs, CA (95619)	4471
Dinuba, CA (93618)	19322
Dixon, CA (95620)	16600
Dobbins, CA (95935)	565
Dorris, CA (96023)	858
Dos Palos, CA (93620)	6358
Douglas City, CA (96024)	632
Dunsmuir, CA (96025)	1644
Durham, CA (95938)	3566
El Dorado, CA (95623)	3901
Elk Grove, CA (95624)	48052
Elk Grove, CA (95757)	27886
Elk Grove, CA (95758)	48267
El Nido, CA (95317)	792
Elverta, CA (95626)	4879
Escalon, CA (95320)	10192
Esparto, CA (95627)	2896
Etna, CA (96027)	1656
Fair Oaks, CA (95628)	34479
Fall River Mills, CA (96028)	1223
Farmington, CA (95230)	643
Fiddletown, CA (95629)	742
Firebaugh, CA (93622)	7288
Folsom, CA (95630)	53688
El Dorado Hills, CA (95762)	33316
Foresthill, CA (95631)	5104
Forest Ranch, CA (95942)	1178
Fort Jones, CA (96032)	1733
Fowler, CA (93625)	5752
French Camp, CA (95231)	3106
Fresno, CA (93650)	2966
Fresno, CA (93701)	5872
Fresno, CA (93702)	27772
Fresno, CA (93703)	19554
Fresno, CA (93704)	19578
Fresno, CA (93705)	23426
Fresno, CA (93706)	22854
Fresno, CA (93710)	19306
Fresno, CA (93711)	30146
Fresno, CA (93720)	36614
Fresno, CA (93721)	1906
Fresno, CA (93722)	54913
Fresno, CA (93723)	6014
Fresno, CA (93725)	16278
Fresno, CA (93726)	26206
Fresno, CA (93727)	48028
Fresno, CA (93728)	9834
Fresno, CA (93730)	7681
Friant, CA (93626)	1202
Galt, CA (95632)	22306
Garden Valley, CA (95633)	2517
Georgetown, CA (95634)	2459
Gerber, CA (96035)	2202
Glenn, CA (95943)	656
Grass Valley, CA (95945)	18769
Grass Valley, CA (95949)	15758
Greenville, CA (95947)	1342
Greenwood, CA (95635)	958
Grenada, CA (96038)	551
Gridley, CA (95948)	8183
Grizzly Flats, CA (95636)	723
Groveland, CA (95321)	2806
Gustine, CA (95322)	6607
Happy Camp, CA (96039)	798
Hayfork, CA (96041)	1501
Herald, CA (95638)	1831
Hickman, CA (95323)	1119
Hilmar, CA (95324)	5825
Hornbrook, CA (96044)	643
Hughson, CA (95326)	7977
Igo, CA (96047)	708
Ione, CA (95640)	5808
Isleton, CA (95641)	1486
Jackson, CA (95642)	6104
Jamestown, CA (95327)	4629
Junction City, CA (96048)	494
Kerman, CA (93630)	13427
Keyes, CA (95328)	2288
Kingsburg, CA (93631)	12763
Knights Landing, CA (95645)	1285
La Grange, CA (95329)	1940
Lakehead, CA (96051)	902
Lathrop, CA (95330)	13248
Le Grand, CA (95333)	2167
Lewiston, CA (96052)	947
Lincoln, CA (95648)	38746
Linden, CA (95236)	4764
Live Oak, CA (95953)	7556
Livingston, CA (95334)	11811
Lockeford, CA (95237)	3187
Lodi, CA (95240)	30585
Lodi, CA (95242)	20643
Loomis, CA (95650)	10909
Los Banos, CA (93635)	27870
Los Molinos, CA (96055)	2732
Lotus, CA (95651)	625
Mcarthur, CA (96056)	1210
Mccloud, CA (96057)	1037
Macdoel, CA (96058)	489
Madera, CA (93636)	8882
Madera, CA (93637)	26109
Madera, CA (93638)	31212
Magalia, CA (95954)	8445
Manteca, CA (95336)	33056
Manteca, CA (95337)	22663
Mariposa, CA (95338)	8172
Marysville, CA (95901)	22529
Beale Afb, CA (95903)	1623
Meadow Vista, CA (95722)	4202
Mendota, CA (93640)	8825
Merced, CA (95340)	24607
Merced, CA (95341)	17451
Merced, CA (95348)	18422
Meridian, CA (95957)	650
Midpines, CA (95345)	579
Millville, CA (96062)	977
Mi Wuk Village, CA (95346)	1069
Modesto, CA (95350)	36016
Modesto, CA (95351)	28298
Modesto, CA (95354)	16332
Modesto, CA (95355)	42666
Modesto, CA (95356)	24224
Modesto, CA (95357)	10140
Modesto, CA (95358)	22496
Mokelumne Hill, CA (95245)	1357
Montague, CA (96064)	3209
Mountain Ranch, CA (95246)	1401
Mount Shasta, CA (96067)	6226
Murphys, CA (95247)	3550
Nevada City, CA (95959)	14769
Newcastle, CA (95658)	5562
Newman, CA (95360)	8424
Nicolaus, CA (95659)	614
North Fork, CA (93643)	2422
North Highlands, CA (95660)	21675
North San Juan, CA (95960)	955
Oakdale, CA (95361)	24557
Oakhurst, CA (93644)	7289
Oak Run, CA (96069)	667
Olivehurst, CA (95961)	16912
Orange Cove, CA (93646)	6510
Squaw Valley, CA (93675)	2686
Orangevale, CA (95662)	26135
Oregon House, CA (95962)	1301
Orland, CA (95963)	11337
Orosi, CA (93647)	7372
Oroville, CA (95965)	12407
Oroville, CA (95966)	19686
Palermo, CA (95968)	1619
Palo Cedro, CA (96073)	4146
Paradise, CA (95969)	19114
Parlier, CA (93648)	10702
Patterson, CA (95363)	18121
Penryn, CA (95663)	2304
Pilot Hill, CA (95664)	1113
Pine Grove, CA (95665)	3764
Pioneer, CA (95666)	4179
Placerville, CA (95667)	28139
Planada, CA (95365)	3801
Pleasant Grove, CA (95668)	687
Plymouth, CA (95669)	2065
Pollock Pines, CA (95726)	6965
Prather, CA (93651)	1657
Quincy, CA (95971)	4865
Raisin City, CA (93652)	664
Mather, CA (95655)	3200
Rancho Cordova, CA (95670)	40655
Rancho Cordova, CA (95742)	6511
Raymond, CA (93653)	802
Red Bluff, CA (96080)	21073
Redding, CA (96001)	23744
Redding, CA (96002)	23604
Redding, CA (96003)	30950
Reedley, CA (93654)	22515
Rescue, CA (95672)	4022
Rio Linda, CA (95673)	11504
Rio Oso, CA (95674)	734
Ripon, CA (95366)	13598
Riverbank, CA (95367)	17864
Riverdale, CA (93656)	4450
Rocklin, CA (95677)	20132
Rocklin, CA (95765)	25874
Roseville, CA (95661)	24647
Roseville, CA (95678)	32889
Granite Bay, CA (95746)	19407
Roseville, CA (95747)	41545
Penn Valley, CA (95946)	8356
Rough And Ready, CA (95975)	1434
Sacramento, CA (95811)	3752
Sacramento, CA (95814)	5330
Sacramento, CA (95815)	14432
Sacramento, CA (95816)	12950
Sacramento, CA (95817)	8527
Sacramento, CA (95818)	16236
Sacramento, CA (95819)	13837
Sacramento, CA (95820)	23334
Sacramento, CA (95821)	24579
Sacramento, CA (95822)	31791
Sacramento, CA (95823)	50088
Sacramento, CA (95824)	19631
Sacramento, CA (95825)	20027
Sacramento, CA (95826)	26728
Sacramento, CA (95827)	16012
Sacramento, CA (95828)	40823
Sacramento, CA (95829)	19919
Sacramento, CA (95830)	679
Sacramento, CA (95831)	34473
Sacramento, CA (95832)	7151
Sacramento, CA (95833)	27060
Sacramento, CA (95834)	18721
Sacramento, CA (95835)	27167
Sacramento, CA (95838)	23781
Sacramento, CA (95841)	13816
Sacramento, CA (95842)	22672
Antelope, CA (95843)	34636
Sacramento, CA (95864)	19481
Salida, CA (95368)	10850
San Andreas, CA (95249)	2912
Sanger, CA (93657)	25192
San Joaquin, CA (93660)	3457
Selma, CA (93662)	22360
Shaver Lake, CA (93664)	681
Sheridan, CA (95681)	957
Shingle Springs, CA (95682)	24623
Shingletown, CA (96088)	3513
Sloughhouse, CA (95683)	5736
Smartsville, CA (95977)	1146
Snelling, CA (95369)	674
Somerset, CA (95684)	2344
Sonora, CA (95370)	19792
Soulsbyville, CA (95372)	2327
Stevinson, CA (95374)	1329
Stockton, CA (95202)	3036
Stockton, CA (95203)	9689
Stockton, CA (95204)	19838
Stockton, CA (95205)	24135
Stockton, CA (95206)	44874
Stockton, CA (95207)	31668
Stockton, CA (95209)	29459
Stockton, CA (95210)	25741
Stockton, CA (95212)	18519
Stockton, CA (95215)	15614
Stockton, CA (95219)	21236
Sutter, CA (95982)	2736
Sutter Creek, CA (95685)	3944
Tollhouse, CA (93667)	1864
Tracy, CA (95304)	8986
Tracy, CA (95376)	38068
Tracy, CA (95377)	23164
Tracy, CA (95391)	7031
Tranquillity, CA (93668)	861
Trinity Center, CA (96091)	501
Tuolumne, CA (95379)	2996
Turlock, CA (95380)	28101
Turlock, CA (95382)	26190
Twain Harte, CA (95383)	3648
Vacaville, CA (95687)	45910
Vacaville, CA (95688)	28085
Vallecito, CA (95251)	479
Valley Springs, CA (95252)	10080
Volcano, CA (95689)	1166
Walnut Grove, CA (95690)	2004
Waterford, CA (95386)	7503
Weed, CA (96094)	4766
West Point, CA (95255)	1287
West Sacramento, CA (95605)	9280
West Sacramento, CA (95691)	26437
Wheatland, CA (95692)	3917
Whitmore, CA (96096)	568
Williams, CA (95987)	5477
Willows, CA (95988)	6588
Wilton, CA (95693)	5891
Winters, CA (95694)	7665
Winton, CA (95388)	9257
Woodbridge, CA (95258)	4461
Woodland, CA (95695)	28392
Woodland, CA (95776)	18163
Yosemite National Park, CA (95389)	1136
Yreka, CA (96097)	7554
Yuba City, CA (95991)	27881
Yuba City, CA (95993)	27844
Aiea, HI (96701)	35697
Captain Cook, HI (96704)	3442
Ewa Beach, HI (96706)	48268
Haiku, HI (96708)	6042
Haleiwa, HI (96712)	5538
Hana, HI (96713)	1366
Hauula, HI (96717)	3161
Hilo, HI (96720)	37207
Holualoa, HI (96725)	2430
Honokaa, HI (96727)	4102
Honolulu, HI (96813)	18878
Honolulu, HI (96814)	14760
Honolulu, HI (96815)	21943
Honolulu, HI (96816)	41290
Honolulu, HI (96817)	44652
Honolulu, HI (96818)	40131
Honolulu, HI (96819)	38800
Honolulu, HI (96821)	16918
Honolulu, HI (96822)	32666
Honolulu, HI (96825)	26452
Honolulu, HI (96826)	22758
J B P H H, HI (96853)	904
J B P H H, HI (96860)	892
Kaaawa, HI (96730)	1235
Kahuku, HI (96731)	2303
Kahului, HI (96732)	17192
Kailua, HI (96734)	40200
M C B H Kaneohe Bay, HI (96863)	2556
Kailua Kona, HI (96740)	18960
Kalaheo, HI (96741)	3885
Waikoloa, HI (96738)	5054
Kamuela, HI (96743)	9807
Kaneohe, HI (96744)	46556
Kapaa, HI (96746)	13416
Kaunakakai, HI (96748)	3479
Keaau, HI (96749)	10325
Kealakekua, HI (96750)	4514
Kihei, HI (96753)	19553
Princeville, HI (96722)	1531
Kilauea, HI (96754)	2888
Koloa, HI (96756)	3999
Kula, HI (96790)	5940
Kurtistown, HI (96760)	2271
Lahaina, HI (96761)	15968
Laie, HI (96762)	4137
Lihue, HI (96766)	12848
Makawao, HI (96768)	12697
Mountain View, HI (96771)	2490
Naalehu, HI (96772)	1596
Pahoa, HI (96778)	8045
Paia, HI (96779)	3245
Papaikou, HI (96781)	1343
Pearl City, HI (96782)	32267
Pepeekeo, HI (96783)	1567
Wahiawa, HI (96786)	29939
Mililani, HI (96789)	46664
Schofield Barracks, HI (96857)	1215
Waialua, HI (96791)	6091
Waianae, HI (96792)	33249
Wailuku, HI (96793)	22792
Waimanalo, HI (96795)	7968
Kapolei, HI (96707)	28516
Waipahu, HI (96797)	60366
Alachua, FL (32615)	9829
Alford, FL (32420)	1710
Altha, FL (32421)	2981
Anthony, FL (32617)	3346
Apalachicola, FL (32320)	2116
Archer, FL (32618)	5306
Baker, FL (32531)	4629
Bascom, FL (32423)	1053
Bell, FL (32619)	3499
Belleview, FL (34420)	11066
Blountstown, FL (32424)	4569
Bonifay, FL (32425)	9005
Branford, FL (32008)	3941
Bristol, FL (32321)	3403
Bronson, FL (32621)	4022
Brooker, FL (32622)	1099
Bryceville, FL (32009)	2673
Callahan, FL (32011)	12069
Campbellton, FL (32426)	769
Cantonment, FL (32533)	22279
Carrabelle, FL (32322)	1948
Caryville, FL (32427)	857
Cedar Key, FL (32625)	1259
Century, FL (32535)	3572
Chattahoochee, FL (32324)	3238
Chiefland, FL (32626)	4653
Chipley, FL (32428)	11235
Clarksville, FL (32430)	966
Cottondale, FL (32431)	3732
Crawfordville, FL (32327)	17961
Crestview, FL (32536)	17433
Crestview, FL (32539)	18523
Cross City, FL (32628)	3115
Crystal River, FL (34428)	6428
Crystal River, FL (34429)	6519
Defuniak Springs, FL (32433)	10112
Defuniak Springs, FL (32435)	5338
Destin, FL (32541)	13002
Miramar Beach, FL (32550)	5708
Dunnellon, FL (34431)	5669
Dunnellon, FL (34432)	9351
Dunnellon, FL (34433)	5014
Dunnellon, FL (34434)	6076
Earleton, FL (32631)	436
Eastpoint, FL (32328)	2523
Ebro, FL (32437)	517
Eglin Afb, FL (32542)	2857
Elkton, FL (32033)	3454
Fernandina Beach, FL (32034)	24213
Floral City, FL (34436)	5715
Fort Walton Beach, FL (32547)	25777
Fort Walton Beach, FL (32548)	16634
Fort White, FL (32038)	6648
Fountain, FL (32438)	2882
Freeport, FL (32439)	5899
Gainesville, FL (32601)	8928
Gainesville, FL (32603)	2079
Gainesville, FL (32605)	18977
Gainesville, FL (32606)	17526
Gainesville, FL (32607)	18162
Gainesville, FL (32608)	27568
Gainesville, FL (32609)	11912
Gainesville, FL (32641)	9677
Gainesville, FL (32653)	10994
Glen Saint Mary, FL (32040)	6294
Graceville, FL (32440)	4119
Grand Ridge, FL (32442)	2733
Green Cove Springs, FL (32043)	21764
Greenville, FL (32331)	3029
Greenwood, FL (32443)	2383
Gretna, FL (32332)	1735
Gulf Breeze, FL (32561)	7242
Gulf Breeze, FL (32563)	18408
Navarre, FL (32566)	28125
Hampton, FL (32044)	1336
Havana, FL (32333)	9603
Hawthorne, FL (32640)	7298
Hernando, FL (34442)	11565
High Springs, FL (32643)	7400
Hilliard, FL (32046)	7443
Holt, FL (32564)	2190
Homosassa, FL (34446)	12854
Homosassa, FL (34448)	7045
Hosford, FL (32334)	1213
Inglis, FL (34449)	2173
Inverness, FL (34450)	7645
Inverness, FL (34452)	8910
Inverness, FL (34453)	7259
Jacksonville, FL (32202)	2088
Jacksonville, FL (32204)	5010
Jacksonville, FL (32205)	21738
Jacksonville, FL (32206)	12216
Jacksonville, FL (32207)	25448
Jacksonville, FL (32208)	24395
Jacksonville, FL (32209)	24803
Jacksonville, FL (32210)	47811
Jacksonville, FL (32211)	24452
Jacksonville, FL (32212)	1033
Jacksonville, FL (32216)	27172
Jacksonville, FL (32217)	15928
Jacksonville, FL (32218)	42358
Jacksonville, FL (32219)	9542
Jacksonville, FL (32220)	10815
Jacksonville, FL (32221)	22388
Jacksonville, FL (32222)	7800
Jacksonville, FL (32223)	22001
Jacksonville, FL (32224)	27462
Jacksonville, FL (32225)	45855
Jacksonville, FL (32226)	14773
Jacksonville, FL (32227)	1339
Atlantic Beach, FL (32233)	18318
Jacksonville, FL (32234)	5386
Jacksonville, FL (32244)	46151
Jacksonville, FL (32246)	38183
Jacksonville Beach, FL (32250)	21490
Jacksonville, FL (32254)	9982
Jacksonville, FL (32256)	32719
Jacksonville, FL (32257)	30774
Jacksonville, FL (32258)	22882
Saint Johns, FL (32259)	31624
Neptune Beach, FL (32266)	5895
Jacksonville, FL (32277)	23326
Jasper, FL (32052)	4624
Jay, FL (32565)	4400
Jennings, FL (32053)	2596
Keystone Heights, FL (32656)	10739
Lake Butler, FL (32054)	7144
Lake City, FL (32024)	13299
Lake City, FL (32025)	12988
Lake City, FL (32055)	11560
Lamont, FL (32336)	1082
Laurel Hill, FL (32567)	2612
Lawtey, FL (32058)	2891
Lecanto, FL (34461)	7130
Beverly Hills, FL (34465)	12110
Lee, FL (32059)	1817
Live Oak, FL (32060)	13766
Live Oak, FL (32064)	5398
Lynn Haven, FL (32444)	17512
Mc Alpin, FL (32062)	1873
Mc David, FL (32568)	2605
Macclenny, FL (32063)	9765
Madison, FL (32340)	6662
Malone, FL (32445)	1005
Marianna, FL (32446)	7003
Marianna, FL (32448)	5959
Hurlburt Field, FL (32544)	1683
Mary Esther, FL (32569)	10152
Mayo, FL (32066)	3537
Melrose, FL (32666)	4578
Micanopy, FL (32667)	2961
Middleburg, FL (32068)	40189
Midway, FL (32343)	2476
Milton, FL (32570)	22059
Milton, FL (32571)	23756
Milton, FL (32583)	16705
Molino, FL (32577)	4057
Monticello, FL (32344)	8043
Morriston, FL (32668)	3834
Newberry, FL (32669)	10060
Niceville, FL (32578)	26798
O Brien, FL (32071)	2351
Ocala, FL (34470)	13536
Ocala, FL (34471)	19283
Ocala, FL (34472)	19741
Ocala, FL (34473)	12043
Ocala, FL (34474)	10878
Ocala, FL (34475)	7532
Ocala, FL (34476)	17468
Ocala, FL (34479)	10039
Ocala, FL (34480)	14240
Ocala, FL (34481)	14319
Ocala, FL (34482)	13801
Old Town, FL (32680)	5755
Fleming Island, FL (32003)	23033
Orange Park, FL (32065)	25306
Orange Park, FL (32073)	33678
Oxford, FL (34484)	2720
Panacea, FL (32346)	1408
Panama City, FL (32401)	17014
Panama City, FL (32403)	2368
Panama City, FL (32404)	30218
Panama City, FL (32405)	21698
Panama City Beach, FL (32407)	7487
Panama City, FL (32408)	11444
Panama City, FL (32409)	7237
Panama City Beach, FL (32413)	10441
Pensacola, FL (32501)	7027
Pensacola, FL (32502)	1991
Pensacola, FL (32503)	23321
Pensacola, FL (32504)	17693
Pensacola, FL (32505)	19265
Pensacola, FL (32506)	26797
Pensacola, FL (32507)	23097
Pensacola, FL (32508)	1657
Pensacola, FL (32514)	28009
Pensacola, FL (32526)	30239
Pensacola, FL (32534)	11795
Perry, FL (32347)	5785
Perry, FL (32348)	7527
Pinetta, FL (32350)	1135
Ponce De Leon, FL (32455)	3181
Ponte Vedra, FL (32081)	3200
Ponte Vedra Beach, FL (32082)	25559
Port Saint Joe, FL (32456)	5500
Quincy, FL (32351)	11011
Quincy, FL (32352)	4494
Raiford, FL (32083)	1148
Reddick, FL (32686)	3111
Saint Augustine, FL (32080)	16244
Saint Augustine, FL (32084)	20955
Saint Augustine, FL (32086)	20134
Saint Augustine, FL (32092)	22578
Saint Augustine, FL (32095)	5641
Sanderson, FL (32087)	2933
Santa Rosa Beach, FL (32459)	9987
Shalimar, FL (32579)	9166
Silver Springs, FL (34488)	7087
Sneads, FL (32460)	3128
Sopchoppy, FL (32358)	1556
Starke, FL (32091)	11250
Steinhatchee, FL (32359)	1230
Summerfield, FL (34491)	21799
Tallahassee, FL (32301)	17380
Tallahassee, FL (32303)	33545
Tallahassee, FL (32304)	15426
Tallahassee, FL (32305)	13957
Tallahassee, FL (32308)	17687
Tallahassee, FL (32309)	25771
Tallahassee, FL (32310)	11008
Tallahassee, FL (32311)	14190
Tallahassee, FL (32312)	27615
Tallahassee, FL (32317)	13399
Trenton, FL (32693)	7632
Valparaiso, FL (32580)	3321
Vernon, FL (32462)	2540
Waldo, FL (32694)	1517
Wellborn, FL (32094)	2141
Westville, FL (32464)	2739
Wewahitchka, FL (32465)	4325
White Springs, FL (32096)	2128
Williston, FL (32696)	8811
Yankeetown, FL (34498)	427
Youngstown, FL (32466)	5105
Yulee, FL (32097)	12135
Abbeville, GA (31001)	1768
Adel, GA (31620)	7649
Adrian, GA (31002)	2119
Ailey, GA (30410)	1232
Alamo, GA (30411)	1812
Alapaha, GA (31622)	1493
Albany, GA (31701)	13470
Albany, GA (31705)	23055
Albany, GA (31707)	18766
Albany, GA (31721)	16198
Allenhurst, GA (31301)	3025
Alma, GA (31510)	6905
Ambrose, GA (31512)	1535
Americus, GA (31709)	12503
Americus, GA (31719)	6274
Andersonville, GA (31711)	681
Appling, GA (30802)	4901
Arabi, GA (31712)	880
Arlington, GA (39813)	1543
Ashburn, GA (31714)	5679
Attapulgus, GA (39815)	1308
Augusta, GA (30901)	10716
Augusta, GA (30904)	18033
Augusta, GA (30905)	4016
Augusta, GA (30906)	43560
Augusta, GA (30907)	40607
Augusta, GA (30909)	31447
Avera, GA (30803)	620
Axson, GA (31624)	908
Baconton, GA (31716)	2208
Bainbridge, GA (39817)	7751
Bainbridge, GA (39819)	7091
Barney, GA (31625)	857
Bartow, GA (30413)	1344
Baxley, GA (31513)	10567
Blackshear, GA (31516)	11146
Blakely, GA (39823)	6661
Bloomingdale, GA (31302)	6360
Blythe, GA (30805)	2036
Bonaire, GA (31005)	13040
Boston, GA (31626)	2705
Box Springs, GA (31801)	2182
Brinson, GA (39825)	1080
Bristol, GA (31518)	553
Bronwood, GA (39826)	583
Brooklet, GA (30415)	5509
Broxton, GA (31519)	2820
Brunswick, GA (31520)	15272
Saint Simons Island, GA (31522)	12342
Brunswick, GA (31523)	10672
Brunswick, GA (31525)	21149
Jekyll Island, GA (31527)	671
Buena Vista, GA (31803)	3639
Butler, GA (31006)	3344
Byromville, GA (31007)	669
Byron, GA (31008)	15420
Cadwell, GA (31009)	998
Cairo, GA (39827)	2670
Cairo, GA (39828)	10863
Camilla, GA (31730)	7294
Cataula, GA (31804)	4912
Chauncey, GA (31011)	669
Chester, GA (31012)	960
Chula, GA (31733)	1261
Claxton, GA (30417)	6867
Climax, GA (39834)	1709
Clyo, GA (31303)	1727
Cobb, GA (31735)	597
Cobbtown, GA (30420)	1319
Cochran, GA (31014)	9277
Collins, GA (30421)	2056
Colquitt, GA (39837)	4473
Upatoi, GA (31829)	1273
Columbus, GA (31901)	4573
Columbus, GA (31903)	15278
Columbus, GA (31904)	25126
Fort Benning, GA (31905)	8970
Columbus, GA (31906)	17965
Columbus, GA (31907)	44630
Columbus, GA (31909)	27967
Coolidge, GA (31738)	1727
Cordele, GA (31015)	13658
Culloden, GA (31016)	1302
Cusseta, GA (31805)	2263
Cuthbert, GA (39840)	3778
Damascus, GA (39841)	733
Danville, GA (31017)	1608
Darien, GA (31305)	4166
Davisboro, GA (31018)	978
Dawson, GA (39842)	6301
Dearing, GA (30808)	3483
Denton, GA (31532)	573
Dexter, GA (31019)	1778
Dixie, GA (31629)	683
Doerun, GA (31744)	2450
Donalsonville, GA (39845)	5868
Douglas, GA (31533)	10567
Douglas, GA (31535)	7669
Dry Branch, GA (31020)	1812
Dublin, GA (31021)	20196
East Dublin, GA (31027)	7504
Dudley, GA (31022)	1271
Eastman, GA (31023)	10663
Eatonton, GA (31024)	15971
Edison, GA (39846)	1594
Elko, GA (31025)	1095
Ellabell, GA (31308)	5852
Ellaville, GA (31806)	3117
Ellerslie, GA (31807)	2201
Enigma, GA (31749)	1696
Evans, GA (30809)	32124
Fitzgerald, GA (31750)	13709
Fleming, GA (31309)	794
Folkston, GA (31537)	5931
Forsyth, GA (31029)	11777
Fort Gaines, GA (39851)	1556
Fortson, GA (31808)	6157
Fort Valley, GA (31030)	12305
Garfield, GA (30425)	1036
Georgetown, GA (39854)	1708
Gibson, GA (30810)	1434
Girard, GA (30426)	744
Glennville, GA (30427)	7747
Glenwood, GA (30428)	1634
Gordon, GA (31031)	4822
Gray, GA (31032)	11410
Grovetown, GA (30813)	22122
Guyton, GA (31312)	13294
Haddock, GA (31033)	1844
Hahira, GA (31632)	8003
Hamilton, GA (31811)	3585
Harlem, GA (30814)	6581
Harrison, GA (31035)	1000
Hartsfield, GA (31756)	754
Hawkinsville, GA (31036)	7749
Hazlehurst, GA (31539)	9967
Helena, GA (31037)	2045
Hephzibah, GA (30815)	31052
Hillsboro, GA (31038)	697
Hinesville, GA (31313)	29104
Fort Stewart, GA (31314)	1272
Fort Stewart, GA (31315)	7225
Hoboken, GA (31542)	1858
Homerville, GA (31634)	4010
Hortense, GA (31543)	3298
Ideal, GA (31041)	576
Iron City, GA (39859)	977
Irwinton, GA (31042)	1492
Jacksonville, GA (31544)	474
Jakin, GA (39861)	706
Jeffersonville, GA (31044)	2646
Jesup, GA (31545)	11310
Jesup, GA (31546)	4341
Juliette, GA (31046)	2850
Kathleen, GA (31047)	9578
Keysville, GA (30816)	1406
Kingsland, GA (31548)	16314
Kite, GA (31049)	1258
Lakeland, GA (31635)	4432
Lake Park, GA (31636)	7161
Leary, GA (39862)	992
Leesburg, GA (31763)	20161
Lenox, GA (31637)	2212
Leslie, GA (31764)	1157
Lincolnton, GA (30817)	6077
Lizella, GA (31052)	7592
Louisville, GA (30434)	4447
Ludowici, GA (31316)	5899
Lumber City, GA (31549)	1264
Lumpkin, GA (31815)	1593
Lyons, GA (30436)	8258
Mc Intyre, GA (31054)	1365
Mc Rae, GA (31055)	3496
Macon, GA (31201)	4882
Macon, GA (31204)	22690
Macon, GA (31206)	20197
Macon, GA (31210)	25708
Macon, GA (31211)	12269
Macon, GA (31216)	12714
Macon, GA (31217)	13331
Macon, GA (31220)	10957
Manchester, GA (31816)	4362
Manor, GA (31550)	625
Marshallville, GA (31057)	1378
Mauk, GA (31058)	1172
Meigs, GA (31765)	1955
Mershon, GA (31551)	697
Metter, GA (30439)	7046
Midland, GA (31820)	7901
Midville, GA (30441)	1585
Midway, GA (31320)	7000
Milan, GA (31060)	1174
Milledgeville, GA (31061)	26542
Millen, GA (30442)	5512
Millwood, GA (31552)	724
Mitchell, GA (30820)	889
Montezuma, GA (31063)	3819
Monticello, GA (31064)	7241
Montrose, GA (31065)	993
Morven, GA (31638)	797
Moultrie, GA (31768)	15009
Moultrie, GA (31788)	5947
Mount Vernon, GA (30445)	1883
Knoxville, GA (31050)	572
Musella, GA (31066)	862
Nahunta, GA (31553)	3655
Nashville, GA (31639)	7480
Naylor, GA (31641)	1601
Newington, GA (30446)	1148
Newton, GA (39870)	1796
Nicholls, GA (31554)	3797
Norman Park, GA (31771)	3866
Norwood, GA (30821)	781
Ochlocknee, GA (31773)	2965
Ocilla, GA (31774)	4568
Odum, GA (31555)	2215
Oglethorpe, GA (31068)	2731
Omega, GA (31775)	2334
Patterson, GA (31557)	2238
Pavo, GA (31778)	2066
Pearson, GA (31642)	3525
Pelham, GA (31779)	5980
Pembroke, GA (31321)	4996
Perry, GA (31069)	14911
Pinehurst, GA (31070)	604
Pine Mountain, GA (31822)	4414
Pine Mountain Valley, GA (31823)	642
Pineview, GA (31071)	857
Pitts, GA (31072)	942
Plains, GA (31780)	1549
Pooler, GA (31322)	17553
Portal, GA (30450)	2113
Poulan, GA (31781)	1317
Preston, GA (31824)	1335
Quitman, GA (31643)	6500
Ray City, GA (31645)	3307
Rebecca, GA (31783)	841
Register, GA (30452)	1255
Reidsville, GA (30453)	4533
Rentz, GA (31075)	1931
Reynolds, GA (31076)	2389
Rhine, GA (31077)	894
Riceboro, GA (31323)	1394
Richland, GA (31825)	1730
Richmond Hill, GA (31324)	19120
Rincon, GA (31326)	15490
Roberta, GA (31078)	2784
Rochelle, GA (31079)	2069
Rockledge, GA (30454)	499
Rocky Ford, GA (30455)	493
Saint George, GA (31562)	1190
Kings Bay, GA (31547)	421
Saint Marys, GA (31558)	15544
Sale City, GA (31784)	633
Sandersville, GA (31082)	8384
Sardis, GA (30456)	1552
Savannah, GA (31401)	11609
Savannah, GA (31404)	21783
Savannah, GA (31405)	25803
Savannah, GA (31406)	26193
Savannah, GA (31407)	4623
Savannah, GA (31408)	6915
Savannah, GA (31410)	19812
Savannah, GA (31411)	7756
Savannah, GA (31415)	8593
Savannah, GA (31419)	36873
Screven, GA (31560)	2020
Shady Dale, GA (31085)	825
Shellman, GA (39886)	1257
Shiloh, GA (31826)	1509
Smithville, GA (31787)	1242
Soperton, GA (30457)	4127
Sparks, GA (31647)	2475
Sparta, GA (31087)	6213
Springfield, GA (31329)	6568
Stapleton, GA (30823)	1267
Statenville, GA (31648)	662
Statesboro, GA (30458)	19569
Statesboro, GA (30461)	9925
Stockton, GA (31649)	569
Sumner, GA (31789)	1189
Surrency, GA (31563)	1061
Swainsboro, GA (30401)	9903
Sycamore, GA (31790)	1559
Sylvania, GA (30467)	9444
Sylvester, GA (31791)	9898
Talbotton, GA (31827)	1563
Tarrytown, GA (30470)	648
Tennille, GA (31089)	3535
Thomasville, GA (31757)	7537
Thomasville, GA (31792)	16661
Thomson, GA (30824)	13759
Tifton, GA (31793)	7947
Tifton, GA (31794)	18635
Toomsboro, GA (31090)	796
Townsend, GA (31331)	3542
Twin City, GA (30471)	3118
Tybee Island, GA (31328)	2707
Ty Ty, GA (31795)	1673
Unadilla, GA (31091)	2103
Uvalda, GA (30473)	2088
Valdosta, GA (31601)	20887
Valdosta, GA (31602)	23173
Valdosta, GA (31605)	15600
Valdosta, GA (31606)	2981
Vidalia, GA (30474)	10938
Vienna, GA (31092)	4188
Wadley, GA (30477)	2840
Warm Springs, GA (31830)	1782
Centerville, GA (31028)	5013
Warner Robins, GA (31088)	40562
Warner Robins, GA (31093)	20334
Warner Robins, GA (31098)	2142
Warrenton, GA (30828)	3125
Warthen, GA (31094)	954
Warwick, GA (31796)	882
Waverly, GA (31565)	1512
Waverly Hall, GA (31831)	2504
Waycross, GA (31501)	10180
Waycross, GA (31503)	14900
Waynesboro, GA (30830)	10863
Waynesville, GA (31566)	2610
West Green, GA (31567)	672
West Point, GA (31833)	5621
Whigham, GA (39897)	2650
White Oak, GA (31568)	698
Willacoochee, GA (31650)	2220
Woodbine, GA (31569)	4306
Woodland, GA (31836)	798
Wray, GA (31798)	827
Wrens, GA (30833)	3346
Wrightsville, GA (31096)	4439
Yatesville, GA (31097)	1059
Aiken, SC (29801)	17699
Aiken, SC (29803)	30359
Aiken, SC (29805)	4367
Allendale, SC (29810)	3522
Barnwell, SC (29812)	8966
Beaufort, SC (29902)	10427
Beaufort, SC (29906)	14894
Ladys Island, SC (29907)	9271
Blackville, SC (29817)	3399
Okatie, SC (29909)	13658
Bluffton, SC (29910)	27033
Bradley, SC (29819)	1242
Brunson, SC (29911)	1271
Clarks Hill, SC (29821)	1118
Early Branch, SC (29916)	1163
Edgefield, SC (29824)	4973
Estill, SC (29918)	3351
Fairfax, SC (29827)	2342
Garnett, SC (29922)	713
Gloverville, SC (29828)	928
Graniteville, SC (29829)	6269
Hampton, SC (29924)	3231
Hardeeville, SC (29927)	5534
Hilton Head Island, SC (29926)	18627
Hilton Head Island, SC (29928)	12708
Islandton, SC (29929)	896
Jackson, SC (29831)	3125
Johnston, SC (29832)	3975
Mc Cormick, SC (29835)	5273
New Ellenton, SC (29809)	2062
North Augusta, SC (29841)	24541
Beech Island, SC (29842)	4890
North Augusta, SC (29860)	11012
Olar, SC (29843)	879
Pineland, SC (29934)	765
Plum Branch, SC (29845)	957
Port Royal, SC (29935)	3027
Ridgeland, SC (29936)	8723
Saint Helena Island, SC (29920)	7522
Seabrook, SC (29940)	2380
Sheldon, SC (29941)	651
Tillman, SC (29943)	487
Trenton, SC (29847)	3711
Troy, SC (29848)	687
Varnville, SC (29944)	3755
Warrenville, SC (29851)	4955
Williston, SC (29853)	4728
Windsor, SC (29856)	2051
Yemassee, SC (29945)	3476
Belle Glade, FL (33430)	15386
Boca Raton, FL (33428)	30741
Boca Raton, FL (33431)	13010
Boca Raton, FL (33432)	14615
Boca Raton, FL (33433)	34128
Boca Raton, FL (33434)	15728
Boca Raton, FL (33486)	17368
Boca Raton, FL (33487)	14406
Boca Raton, FL (33496)	18444
Boca Raton, FL (33498)	13101
Boynton Beach, FL (33426)	15875
Boynton Beach, FL (33435)	24322
Boynton Beach, FL (33436)	32340
Boynton Beach, FL (33437)	34957
Boynton Beach, FL (33472)	11666
Boynton Beach, FL (33473)	2439
Canal Point, FL (33438)	1088
Clewiston, FL (33440)	13752
Dania, FL (33004)	11715
Deerfield Beach, FL (33441)	19864
Deerfield Beach, FL (33442)	21365
Delray Beach, FL (33444)	16355
Delray Beach, FL (33445)	23599
Delray Beach, FL (33446)	17536
Delray Beach, FL (33483)	10800
Delray Beach, FL (33484)	17552
Fort Lauderdale, FL (33301)	10814
Fort Lauderdale, FL (33304)	12901
Fort Lauderdale, FL (33305)	8760
Fort Lauderdale, FL (33306)	2956
Fort Lauderdale, FL (33308)	23333
Fort Lauderdale, FL (33309)	28360
Fort Lauderdale, FL (33311)	51020
Fort Lauderdale, FL (33312)	37977
Fort Lauderdale, FL (33313)	42812
Fort Lauderdale, FL (33314)	16295
Fort Lauderdale, FL (33315)	9066
Fort Lauderdale, FL (33316)	8885
Fort Lauderdale, FL (33317)	29798
Fort Lauderdale, FL (33319)	35782
Fort Lauderdale, FL (33321)	37189
Fort Lauderdale, FL (33322)	31528
Fort Lauderdale, FL (33323)	16261
Fort Lauderdale, FL (33324)	34610
Fort Lauderdale, FL (33325)	22421
Fort Lauderdale, FL (33326)	27708
Fort Lauderdale, FL (33327)	17177
Fort Lauderdale, FL (33328)	21833
Fort Lauderdale, FL (33330)	12229
Fort Lauderdale, FL (33331)	19100
Fort Lauderdale, FL (33332)	8495
Fort Lauderdale, FL (33334)	22157
Fort Lauderdale, FL (33351)	27868
Fort Pierce, FL (34945)	3195
Fort Pierce, FL (34946)	4617
Fort Pierce, FL (34947)	8389
Fort Pierce, FL (34949)	5198
Fort Pierce, FL (34950)	10636
Fort Pierce, FL (34951)	10838
Fort Pierce, FL (34981)	2969
Fort Pierce, FL (34982)	18125
Port Saint Lucie, FL (34983)	29806
Port Saint Lucie, FL (34952)	28788
Port Saint Lucie, FL (34953)	47105
Port Saint Lucie, FL (34984)	11360
Port Saint Lucie, FL (34986)	19080
Port Saint Lucie, FL (34987)	4792
Hallandale, FL (33009)	28313
Hialeah, FL (33010)	32800
Hialeah, FL (33012)	55977
Hialeah, FL (33013)	26263
Hialeah, FL (33014)	33948
Hialeah, FL (33015)	48677
Hialeah, FL (33016)	37554
Hialeah, FL (33018)	38116
Hobe Sound, FL (33455)	15239
Hollywood, FL (33019)	12013
Hollywood, FL (33020)	29529
Hollywood, FL (33021)	36577
Hollywood, FL (33023)	51575
Hollywood, FL (33024)	52766
Hollywood, FL (33025)	45312
Hollywood, FL (33026)	25327
Hollywood, FL (33027)	45429
Pembroke Pines, FL (33028)	21967
Hollywood, FL (33029)	37103
Homestead, FL (33030)	20582
Homestead, FL (33031)	4588
Homestead, FL (33032)	24436
Homestead, FL (33033)	33822
Homestead, FL (33034)	12556
Homestead, FL (33035)	8449
Indiantown, FL (34956)	5538
Islamorada, FL (33036)	3184
Jensen Beach, FL (34957)	16670
Jupiter, FL (33458)	37138
Jupiter, FL (33469)	12418
Jupiter, FL (33477)	9830
Jupiter, FL (33478)	10782
Key Largo, FL (33037)	10867
Key West, FL (33040)	24190
Lake Worth, FL (33449)	6332
Lake Worth, FL (33460)	20434
Lake Worth, FL (33461)	26930
Lake Worth, FL (33462)	23019
Lake Worth, FL (33463)	40712
Lake Worth, FL (33467)	41690
Loxahatchee, FL (33470)	21581
Marathon, FL (33050)	7636
Miami, FL (33122)	781
Miami, FL (33125)	34463
Miami, FL (33126)	36254
Miami, FL (33127)	21285
Miami, FL (33128)	3969
Miami, FL (33129)	10362
Miami, FL (33130)	14200
Miami, FL (33131)	10701
Miami, FL (33132)	5392
Miami, FL (33133)	24458
Miami, FL (33134)	30083
Miami, FL (33135)	23184
Miami, FL (33136)	8801
Miami, FL (33137)	13899
Miami, FL (33138)	21082
Miami, FL (33142)	36229
Miami, FL (33143)	22921
Miami, FL (33144)	20854
Miami, FL (33145)	22151
Miami, FL (33146)	8496
Miami, FL (33147)	36261
Key Biscayne, FL (33149)	9545
Miami, FL (33150)	21206
Miami, FL (33155)	35417
Miami, FL (33156)	26260
Miami, FL (33157)	49941
Miami, FL (33158)	5688
North Miami Beach, FL (33160)	29713
Miami, FL (33161)	40161
Miami, FL (33162)	35562
Miami, FL (33165)	44352
Miami, FL (33166)	18664
Miami, FL (33167)	16123
Miami, FL (33168)	23332
Miami, FL (33169)	32158
Miami, FL (33170)	9243
Miami, FL (33172)	31099
Miami, FL (33173)	26714
Miami, FL (33174)	24096
Miami, FL (33175)	44563
Miami, FL (33176)	41094
Miami, FL (33177)	41930
Miami, FL (33178)	29365
Miami, FL (33179)	32123
Miami, FL (33180)	22712
Miami, FL (33181)	13027
Miami, FL (33182)	11730
Miami, FL (33183)	29815
Miami, FL (33184)	16555
Miami, FL (33185)	20768
Miami, FL (33186)	55342
Miami, FL (33187)	12948
Miami, FL (33189)	18318
Miami, FL (33190)	7868
Miami, FL (33193)	36477
Miami, FL (33194)	4472
Miami, FL (33196)	34617
Miami Beach, FL (33109)	470
Miami Beach, FL (33139)	25564
Miami Beach, FL (33140)	15996
Miami Beach, FL (33141)	25117
Miami Beach, FL (33154)	10881
Moore Haven, FL (33471)	3558
Okeechobee, FL (34972)	11377
Okeechobee, FL (34974)	15888
Opa Locka, FL (33054)	21961
Opa Locka, FL (33055)	36086
Miami Gardens, FL (33056)	30027
Pahokee, FL (33476)	4867
Palm Beach, FL (33480)	8579
Palm City, FL (34990)	23211
Pompano Beach, FL (33060)	24822
Pompano Beach, FL (33062)	18810
Pompano Beach, FL (33063)	40464
Pompano Beach, FL (33064)	38337
Pompano Beach, FL (33065)	40435
Pompano Beach, FL (33066)	13054
Pompano Beach, FL (33067)	22885
Pompano Beach, FL (33068)	38523
Pompano Beach, FL (33069)	17972
Pompano Beach, FL (33071)	32685
Pompano Beach, FL (33073)	21650
Pompano Beach, FL (33076)	25322
South Bay, FL (33493)	2306
Stuart, FL (34994)	10812
Stuart, FL (34996)	8039
Stuart, FL (34997)	31441
Summerland Key, FL (33042)	5056
Big Pine Key, FL (33043)	3872
Tavernier, FL (33070)	4690
West Palm Beach, FL (33401)	16307
West Palm Beach, FL (33403)	9634
West Palm Beach, FL (33404)	20858
West Palm Beach, FL (33405)	14580
West Palm Beach, FL (33406)	19029
West Palm Beach, FL (33407)	21270
North Palm Beach, FL (33408)	14440
West Palm Beach, FL (33409)	20492
Palm Beach Gardens, FL (33410)	29752
West Palm Beach, FL (33411)	52148
West Palm Beach, FL (33412)	11944
West Palm Beach, FL (33413)	11698
Wellington, FL (33414)	43745
West Palm Beach, FL (33415)	32794
West Palm Beach, FL (33417)	19843
Palm Beach Gardens, FL (33418)	30456
Altamonte Springs, FL (32701)	16440
Altamonte Springs, FL (32714)	27758
Altoona, FL (32702)	2437
Alva, FL (33920)	4227
Apopka, FL (32703)	35010
Apopka, FL (32712)	32901
Arcadia, FL (34266)	13648
Arcadia, FL (34269)	2315
Astatula, FL (34705)	2132
Astor, FL (32102)	1815
Auburndale, FL (33823)	22819
Avon Park, FL (33825)	15069
Babson Park, FL (33827)	2253
Bartow, FL (33830)	18541
Bokeelia, FL (33922)	2807
Bonita Springs, FL (34134)	11428
Bonita Springs, FL (34135)	25512
Bowling Green, FL (33834)	3967
Bradenton, FL (34201)	3187
Bradenton, FL (34202)	17023
Bradenton, FL (34203)	25432
Bradenton, FL (34205)	21830
Bradenton, FL (34207)	19379
Bradenton, FL (34208)	22553
Bradenton, FL (34209)	26294
Bradenton, FL (34210)	11326
Bradenton, FL (34211)	2522
Bradenton, FL (34212)	12027
Bradenton Beach, FL (34217)	3890
Brandon, FL (33510)	21889
Brandon, FL (33511)	41163
Brooksville, FL (34601)	14919
Brooksville, FL (34602)	5425
Brooksville, FL (34604)	7120
Spring Hill, FL (34606)	19738
Spring Hill, FL (34607)	6196
Spring Hill, FL (34608)	22818
Spring Hill, FL (34609)	29634
Spring Hill, FL (34610)	9854
Brooksville, FL (34613)	13307
Brooksville, FL (34614)	4847
Bunnell, FL (32110)	5741
Bushnell, FL (33513)	7449
Cape Canaveral, FL (32920)	7666
Casselberry, FL (32707)	27433
Winter Springs, FL (32708)	35990
Casselberry, FL (32730)	4296
Center Hill, FL (33514)	1389
Christmas, FL (32709)	2118
Citra, FL (32113)	4363
Clearwater, FL (33755)	18086
Clearwater, FL (33756)	22629
Clearwater, FL (33759)	13561
Clearwater, FL (33760)	11325
Clearwater, FL (33761)	14437
Clearwater, FL (33762)	5211
Clearwater, FL (33763)	13995
Clearwater, FL (33764)	18969
Clearwater, FL (33765)	10137
Clearwater Beach, FL (33767)	7002
Clermont, FL (34711)	41697
Clermont, FL (34714)	10672
Clermont, FL (34715)	10526
Cocoa, FL (32922)	9812
Cocoa, FL (32926)	17028
Cocoa, FL (32927)	22161
Cocoa Beach, FL (32931)	11185
Cortez, FL (34215)	754
Crescent City, FL (32112)	4149
Dade City, FL (33523)	11418
Dade City, FL (33525)	12305
Davenport, FL (33837)	14240
Davenport, FL (33896)	6157
Davenport, FL (33897)	10418
Daytona Beach, FL (32114)	18774
Daytona Beach, FL (32117)	17600
Daytona Beach, FL (32118)	12518
Daytona Beach, FL (32119)	15714
Daytona Beach, FL (32124)	2470
Debary, FL (32713)	16194
Deland, FL (32720)	21124
Deland, FL (32724)	23328
De Leon Springs, FL (32130)	4476
Deltona, FL (32725)	35020
Deltona, FL (32738)	34048
Dover, FL (33527)	11045
Dundee, FL (33838)	3107
Dunedin, FL (34698)	29142
Eagle Lake, FL (33839)	3656
East Palatka, FL (32131)	3480
Edgewater, FL (32132)	6172
Edgewater, FL (32141)	14092
Ellenton, FL (34222)	8591
Englewood, FL (34223)	12865
Englewood, FL (34224)	11254
Estero, FL (33928)	15938
Eustis, FL (32726)	14202
Eustis, FL (32736)	7580
Fellsmere, FL (32948)	4951
Flagler Beach, FL (32136)	6154
Palm Coast, FL (32137)	29861
Palm Coast, FL (32164)	31048
Florahome, FL (32140)	1362
Fort Mc Coy, FL (32134)	5222
Fort Meade, FL (33841)	6089
Fort Myers, FL (33901)	13876
North Fort Myers, FL (33903)	15505
Cape Coral, FL (33904)	24936
Fort Myers, FL (33905)	20859
Fort Myers, FL (33907)	16221
Fort Myers, FL (33908)	28697
Cape Coral, FL (33909)	17607
Fort Myers, FL (33912)	13761
Fort Myers, FL (33913)	12218
Cape Coral, FL (33914)	29880
Fort Myers, FL (33916)	12199
North Fort Myers, FL (33917)	20929
Fort Myers, FL (33919)	23070
Fort Myers, FL (33966)	6504
Fort Myers, FL (33967)	17140
Cape Coral, FL (33990)	23239
Cape Coral, FL (33991)	14538
Cape Coral, FL (33993)	16212
Fort Myers Beach, FL (33931)	7233
Frostproof, FL (33843)	6744
Fruitland Park, FL (34731)	8824
Geneva, FL (32732)	4509
Georgetown, FL (32139)	825
Gibsonton, FL (33534)	9375
Gotha, FL (34734)	3629
Grand Island, FL (32735)	3405
Grant, FL (32949)	1761
Groveland, FL (34736)	11185
Haines City, FL (33844)	21545
Hastings, FL (32145)	4018
Howey In The Hills, FL (34737)	2305
Immokalee, FL (34142)	10418
Indian Rocks Beach, FL (33785)	4669
Belleair Beach, FL (33786)	1352
Interlachen, FL (32148)	7169
Kathleen, FL (33849)	1448
Kenansville, FL (34739)	615
Kissimmee, FL (34741)	30652
Kissimmee, FL (34743)	27284
Kissimmee, FL (34744)	33540
Kissimmee, FL (34746)	27251
Kissimmee, FL (34747)	11500
Kissimmee, FL (34758)	23796
Kissimmee, FL (34759)	22682
Labelle, FL (33935)	9251
Lady Lake, FL (32159)	22317
The Villages, FL (32162)	37255
Lake Alfred, FL (33850)	5471
Lake Helen, FL (32744)	2861
Lakeland, FL (33801)	21047
Lakeland, FL (33803)	19868
Lakeland, FL (33805)	15360
Lakeland, FL (33809)	22639
Lakeland, FL (33810)	33725
Lakeland, FL (33811)	16915
Lakeland, FL (33812)	9285
Lakeland, FL (33813)	27465
Lakeland, FL (33815)	8160
Lake Mary, FL (32746)	32167
Lake Panasoffkee, FL (33538)	3199
Lake Placid, FL (33852)	13363
Lake Wales, FL (33853)	7605
Lake Wales, FL (33859)	8011
Lake Wales, FL (33898)	10607
Land O Lakes, FL (34637)	4058
Land O Lakes, FL (34638)	15130
Land O Lakes, FL (34639)	21372
Largo, FL (33770)	18466
Largo, FL (33771)	20497
Seminole, FL (33772)	18722
Largo, FL (33773)	13683
Largo, FL (33774)	13786
Seminole, FL (33776)	10950
Seminole, FL (33777)	14037
Largo, FL (33778)	11116
Leesburg, FL (34748)	29719
Leesburg, FL (34788)	12927
Lehigh Acres, FL (33936)	14941
Lehigh Acres, FL (33971)	14855
Lehigh Acres, FL (33972)	7695
Lehigh Acres, FL (33973)	4816
Lehigh Acres, FL (33974)	6806
Lehigh Acres, FL (33976)	7496
Lithia, FL (33547)	15589
Longboat Key, FL (34228)	5829
Longwood, FL (32750)	18989
Longwood, FL (32779)	24825
Lorida, FL (33857)	1136
Lutz, FL (33548)	5601
Lutz, FL (33549)	13920
Lutz, FL (33558)	16462
Lutz, FL (33559)	10460
Maitland, FL (32751)	16337
Malabar, FL (32950)	3755
Marco Island, FL (34145)	12812
Mascotte, FL (34753)	4186
Melbourne, FL (32901)	15138
Indialantic, FL (32903)	11378
Melbourne, FL (32904)	21306
Palm Bay, FL (32905)	16719
Palm Bay, FL (32907)	32479
Palm Bay, FL (32908)	8391
Palm Bay, FL (32909)	23705
Patrick Afb, FL (32925)	1019
Melbourne, FL (32934)	14432
Melbourne, FL (32935)	30651
Satellite Beach, FL (32937)	21943
Melbourne, FL (32940)	28397
Melbourne Beach, FL (32951)	9117
Merritt Island, FL (32952)	17859
Merritt Island, FL (32953)	18446
Mims, FL (32754)	8999
Montverde, FL (34756)	2778
Mount Dora, FL (32757)	16168
Mulberry, FL (33860)	16192
Myakka City, FL (34251)	5170
Naples, FL (34102)	8615
Naples, FL (34103)	10036
Naples, FL (34104)	18617
Naples, FL (34105)	11226
Naples, FL (34108)	14976
Naples, FL (34109)	19394
Naples, FL (34110)	16710
Naples, FL (34112)	19197
Naples, FL (34113)	13755
Naples, FL (34114)	9876
Naples, FL (34116)	23437
Naples, FL (34117)	11401
Naples, FL (34119)	21538
Naples, FL (34120)	20882
New Port Richey, FL (34652)	17517
New Port Richey, FL (34653)	22060
New Port Richey, FL (34654)	16934
New Port Richey, FL (34655)	32552
New Smyrna Beach, FL (32168)	18172
New Smyrna Beach, FL (32169)	7570
Nokomis, FL (34275)	12625
Oak Hill, FL (32759)	2114
Ocklawaha, FL (32179)	4920
Ocoee, FL (34761)	30129
Odessa, FL (33556)	19062
Okahumpka, FL (34762)	737
Oldsmar, FL (34677)	18231
Ona, FL (33865)	801
Orange City, FL (32763)	15749
Orlando, FL (32801)	7428
Orlando, FL (32803)	15056
Orlando, FL (32804)	13999
Orlando, FL (32805)	15504
Orlando, FL (32806)	20143
Orlando, FL (32807)	23638
Orlando, FL (32808)	34747
Orlando, FL (32809)	21816
Orlando, FL (32810)	24428
Orlando, FL (32811)	26038
Orlando, FL (32812)	26632
Orlando, FL (32814)	4751
Orlando, FL (32817)	23502
Orlando, FL (32818)	34498
Orlando, FL (32819)	21319
Orlando, FL (32820)	6420
Orlando, FL (32821)	13026
Orlando, FL (32822)	40840
Orlando, FL (32824)	29557
Orlando, FL (32825)	42371
Orlando, FL (32826)	14450
Orlando, FL (32827)	5098
Orlando, FL (32828)	43801
Orlando, FL (32829)	14031
Orlando, FL (32832)	10840
Orlando, FL (32833)	7266
Orlando, FL (32835)	30686
Orlando, FL (32836)	13901
Orlando, FL (32837)	41755
Orlando, FL (32839)	34769
Ormond Beach, FL (32174)	39757
Ormond Beach, FL (32176)	11627
Osprey, FL (34229)	6356
Osteen, FL (32764)	2665
Oviedo, FL (32765)	43141
Oviedo, FL (32766)	12531
Paisley, FL (32767)	1954
Palatka, FL (32177)	17169
Palmetto, FL (34221)	26628
Palm Harbor, FL (34683)	26384
Palm Harbor, FL (34684)	21430
Palm Harbor, FL (34685)	14958
Parrish, FL (34219)	13972
Pierson, FL (32180)	3008
Pinellas Park, FL (33781)	19363
Pinellas Park, FL (33782)	16324
Placida, FL (33946)	1825
Rotonda West, FL (33947)	6868
Plant City, FL (33563)	18606
Plant City, FL (33565)	12669
Plant City, FL (33566)	14812
Plant City, FL (33567)	7552
Polk City, FL (33868)	7694
Pomona Park, FL (32181)	1674
Port Orange, FL (32127)	23714
Port Orange, FL (32128)	13963
Port Orange, FL (32129)	16267
Hudson, FL (34667)	23296
Port Richey, FL (34668)	30882
Hudson, FL (34669)	9575
Port Charlotte, FL (33948)	12393
Punta Gorda, FL (33950)	15702
Port Charlotte, FL (33952)	21448
Port Charlotte, FL (33953)	4066
Port Charlotte, FL (33954)	7511
Punta Gorda, FL (33955)	6777
Punta Gorda, FL (33980)	7110
Port Charlotte, FL (33981)	7626
Punta Gorda, FL (33982)	6025
Punta Gorda, FL (33983)	11126
Riverview, FL (33569)	21701
Riverview, FL (33578)	24995
Riverview, FL (33579)	16169
Rockledge, FL (32955)	30297
Ruskin, FL (33570)	13315
Apollo Beach, FL (33572)	11916
Sun City Center, FL (33573)	16339
Safety Harbor, FL (34695)	15336
Saint Cloud, FL (34769)	16849
Saint Cloud, FL (34771)	12026
Saint Cloud, FL (34772)	17179
Saint Cloud, FL (34773)	2146
Saint James City, FL (33956)	2905
Saint Petersburg, FL (33701)	10382
Saint Petersburg, FL (33702)	23142
Saint Petersburg, FL (33703)	19556
Saint Petersburg, FL (33704)	13356
Saint Petersburg, FL (33705)	18954
Saint Petersburg, FL (33706)	12575
Saint Petersburg, FL (33707)	18285
Saint Petersburg, FL (33708)	12055
Saint Petersburg, FL (33709)	18847
Saint Petersburg, FL (33710)	27018
Saint Petersburg, FL (33711)	13149
Saint Petersburg, FL (33712)	18792
Saint Petersburg, FL (33713)	23794
Saint Petersburg, FL (33714)	13109
Saint Petersburg, FL (33715)	6292
Saint Petersburg, FL (33716)	11007
San Antonio, FL (33576)	3897
Sanford, FL (32771)	38014
Sanford, FL (32773)	21645
Sanibel, FL (33957)	5478
San Mateo, FL (32187)	1834
Sarasota, FL (34231)	23757
Sarasota, FL (34232)	26377
Sarasota, FL (34233)	14328
Sarasota, FL (34234)	13181
Sarasota, FL (34235)	11109
Sarasota, FL (34236)	9818
Sarasota, FL (34237)	11174
Sarasota, FL (34238)	15001
Sarasota, FL (34239)	12103
Sarasota, FL (34240)	9627
Sarasota, FL (34241)	11883
Sarasota, FL (34242)	7186
Sarasota, FL (34243)	20697
Satsuma, FL (32189)	3641
Sebastian, FL (32958)	20170
Sebastian, FL (32976)	6336
Sebring, FL (33870)	12227
Sebring, FL (33872)	11662
Sebring, FL (33875)	8331
Sebring, FL (33876)	3527
Seffner, FL (33584)	19503
Seville, FL (32190)	1107
Sorrento, FL (32776)	8500
Sumterville, FL (33585)	946
Tampa, FL (33602)	8527
Tampa, FL (33603)	14709
Tampa, FL (33604)	26805
Tampa, FL (33605)	13886
Tampa, FL (33606)	11711
Tampa, FL (33607)	19120
Tampa, FL (33609)	12817
Tampa, FL (33610)	31333
Tampa, FL (33611)	23170
Tampa, FL (33612)	30881
Tampa, FL (33613)	19897
Tampa, FL (33614)	35378
Tampa, FL (33615)	34605
Tampa, FL (33616)	10395
Tampa, FL (33617)	32338
Tampa, FL (33618)	21095
Tampa, FL (33619)	25016
Tampa, FL (33621)	1305
Tampa, FL (33624)	32212
Tampa, FL (33625)	20081
Tampa, FL (33626)	22018
Tampa, FL (33629)	19966
Tampa, FL (33634)	16165
Tampa, FL (33635)	12187
Tampa, FL (33637)	11208
Tampa, FL (33647)	43080
Tarpon Springs, FL (34688)	7470
Tarpon Springs, FL (34689)	19539
Holiday, FL (34690)	9306
Holiday, FL (34691)	15464
Tavares, FL (32778)	14189
Thonotosassa, FL (33592)	7529
Titusville, FL (32780)	27299
Titusville, FL (32796)	15488
Umatilla, FL (32784)	8336
Valrico, FL (33594)	29046
Valrico, FL (33596)	21689
Venice, FL (34285)	12971
North Port, FL (34286)	14722
North Port, FL (34287)	17315
North Port, FL (34288)	8484
North Port, FL (34289)	1436
North Port, FL (34291)	4595
Venice, FL (34292)	11178
Venice, FL (34293)	27611
Venus, FL (33960)	579
Vero Beach, FL (32960)	14214
Vero Beach, FL (32962)	17550
Vero Beach, FL (32963)	12893
Vero Beach, FL (32966)	12116
Vero Beach, FL (32967)	14780
Vero Beach, FL (32968)	10708
Wauchula, FL (33873)	9195
Webster, FL (33597)	5428
Weirsdale, FL (32195)	2933
Welaka, FL (32193)	905
Wildwood, FL (34785)	8237
Wimauma, FL (33598)	8893
Windermere, FL (34786)	22917
Winter Garden, FL (34787)	34213
Winter Haven, FL (33880)	26451
Winter Haven, FL (33881)	21350
Winter Haven, FL (33884)	23252
Winter Park, FL (32789)	18789
Winter Park, FL (32792)	33197
Yalaha, FL (34797)	1135
Zellwood, FL (32798)	3064
Zephyrhills, FL (33540)	5831
Zephyrhills, FL (33541)	12688
Zephyrhills, FL (33542)	12588
Wesley Chapel, FL (33543)	18598
Wesley Chapel, FL (33544)	18197
Wesley Chapel, FL (33545)	9951
Zolfo Springs, FL (33890)	4136
Abbeville, AL (36310)	4938
Adamsville, AL (35005)	6375
Addison, AL (35540)	1912
Adger, AL (35006)	2676
Akron, AL (35441)	866
Alabaster, AL (35007)	21780
Alberta, AL (36720)	609
Albertville, AL (35950)	17113
Albertville, AL (35951)	8994
Alexander City, AL (35010)	16204
Alexandria, AL (36250)	4061
Aliceville, AL (35442)	3917
Alpine, AL (35014)	3070
Altoona, AL (35952)	5439
Andalusia, AL (36420)	9134
Andalusia, AL (36421)	6268
Anderson, AL (35610)	1510
Anniston, AL (36201)	13184
Oxford, AL (36203)	15567
Anniston, AL (36205)	482
Anniston, AL (36206)	8745
Anniston, AL (36207)	14862
Arab, AL (35016)	13412
Ariton, AL (36311)	2096
Arley, AL (35541)	2568
Ashford, AL (36312)	4573
Ashland, AL (36251)	4231
Ashville, AL (35953)	5784
Athens, AL (35611)	18662
Athens, AL (35613)	15181
Athens, AL (35614)	5680
Atmore, AL (36502)	11077
Attalla, AL (35954)	9449
Auburn, AL (36830)	23518
Auburn, AL (36832)	9975
Autaugaville, AL (36003)	1628
Axis, AL (36505)	1154
Baileyton, AL (35019)	1766
Banks, AL (36005)	1336
Bankston, AL (35542)	841
Bay Minette, AL (36507)	14435
Bayou La Batre, AL (36509)	1722
Bear Creek, AL (35543)	811
Beatrice, AL (36425)	762
Beaverton, AL (35544)	532
Berry, AL (35546)	2931
Bessemer, AL (35020)	19176
Bessemer, AL (35022)	16096
Bessemer, AL (35023)	19495
Billingsley, AL (36006)	1117
Birmingham, AL (35203)	1940
Birmingham, AL (35204)	7231
Birmingham, AL (35205)	11604
Birmingham, AL (35206)	12877
Birmingham, AL (35207)	6546
Birmingham, AL (35208)	12084
Birmingham, AL (35209)	21082
Birmingham, AL (35210)	11173
Birmingham, AL (35211)	19526
Birmingham, AL (35212)	8171
Birmingham, AL (35213)	11782
Birmingham, AL (35214)	15464
Birmingham, AL (35215)	35392
Birmingham, AL (35216)	27647
Birmingham, AL (35217)	10183
Birmingham, AL (35218)	5263
Birmingham, AL (35221)	3715
Birmingham, AL (35222)	5952
Birmingham, AL (35223)	10271
Birmingham, AL (35224)	4410
Birmingham, AL (35226)	27102
Birmingham, AL (35228)	8079
Birmingham, AL (35233)	573
Birmingham, AL (35234)	4189
Birmingham, AL (35235)	15500
Birmingham, AL (35242)	41562
Birmingham, AL (35243)	15569
Birmingham, AL (35244)	26929
Black, AL (36314)	490
Blountsville, AL (35031)	5923
Boaz, AL (35956)	6666
Boaz, AL (35957)	11968
Boligee, AL (35443)	1325
Bon Secour, AL (36511)	769
Brantley, AL (36009)	1968
Bremen, AL (35033)	2711
Brent, AL (35034)	3090
Brewton, AL (36426)	10877
Bridgeport, AL (35740)	2724
Brierfield, AL (35035)	1057
Brilliant, AL (35548)	1228
Brookwood, AL (35444)	2983
Brownsboro, AL (35741)	2578
Brundidge, AL (36010)	3931
Bryant, AL (35958)	2484
Buhl, AL (35446)	1533
Calera, AL (35040)	11839
Camden, AL (36726)	3887
Camp Hill, AL (36850)	2168
Carbon Hill, AL (35549)	2887
Carrollton, AL (35447)	2649
Castleberry, AL (36432)	1949
Catherine, AL (36728)	604
Cedar Bluff, AL (35959)	3525
Centre, AL (35960)	7149
Centreville, AL (35042)	4226
Chancellor, AL (36316)	1324
Chatom, AL (36518)	2203
Chelsea, AL (35043)	7877
Cherokee, AL (35616)	3095
Childersburg, AL (35044)	5729
Chunchula, AL (36521)	3959
Citronelle, AL (36522)	5524
Clanton, AL (35045)	10205
Clanton, AL (35046)	4966
Clayton, AL (36016)	2556
Cleveland, AL (35049)	3113
Clio, AL (36017)	1074
Coden, AL (36523)	2161
Coffee Springs, AL (36318)	1007
Coffeeville, AL (36524)	887
Coker, AL (35452)	3077
Collinsville, AL (35961)	4299
Columbia, AL (36319)	1838
Columbiana, AL (35051)	6352
Coosada, AL (36020)	963
Cordova, AL (35550)	3945
Cottondale, AL (35453)	8490
Cottonwood, AL (36320)	2673
Courtland, AL (35618)	1608
Cowarts, AL (36321)	1412
Cragford, AL (36255)	677
Crane Hill, AL (35053)	1991
Creola, AL (36525)	1742
Cropwell, AL (35054)	3250
Crossville, AL (35962)	5041
Cullman, AL (35055)	14351
Cullman, AL (35057)	9536
Cullman, AL (35058)	7942
Cusseta, AL (36852)	1707
Dadeville, AL (36853)	6312
Daleville, AL (36322)	6534
Fort Rucker, AL (36362)	3288
Danville, AL (35619)	4236
Daphne, AL (36526)	22153
Spanish Fort, AL (36527)	9416
Dauphin Island, AL (36528)	1197
Daviston, AL (36256)	1239
Dawson, AL (35963)	1164
Deatsville, AL (36022)	10267
Decatur, AL (35601)	25771
Decatur, AL (35603)	25100
Delta, AL (36258)	1291
Demopolis, AL (36732)	6884
Detroit, AL (35552)	760
Dixons Mills, AL (36736)	1124
Dolomite, AL (35061)	1160
Dora, AL (35062)	6679
Dothan, AL (36301)	26580
Dothan, AL (36303)	23908
Dothan, AL (36305)	11865
Double Springs, AL (35553)	3468
Dozier, AL (36028)	1239
Duncanville, AL (35456)	3311
Dutton, AL (35744)	1814
Eastaboga, AL (36260)	3092
Eclectic, AL (36024)	4753
Elba, AL (36323)	5913
Elberta, AL (36530)	5453
Eldridge, AL (35554)	873
Elkmont, AL (35620)	6896
Elmore, AL (36025)	3358
Emelle, AL (35459)	645
Empire, AL (35063)	2508
Enterprise, AL (36330)	25806
Epes, AL (35460)	434
Equality, AL (36026)	869
Ethelsville, AL (35461)	1501
Eufaula, AL (36027)	11678
Eutaw, AL (35462)	3767
Eva, AL (35621)	2368
Evergreen, AL (36401)	5813
Fairfield, AL (35064)	8296
Fairhope, AL (36532)	20664
Falkville, AL (35622)	5406
Faunsdale, AL (36738)	723
Fayette, AL (35555)	7492
Fitzpatrick, AL (36029)	740
Five Points, AL (36855)	1099
Flat Rock, AL (35966)	2733
Flomaton, AL (36441)	2910
Florala, AL (36442)	2247
Florence, AL (35630)	21502
Florence, AL (35633)	16321
Florence, AL (35634)	8670
Foley, AL (36535)	17401
Forkland, AL (36740)	943
Fort Deposit, AL (36032)	2230
Fort Mitchell, AL (36856)	2939
Fort Payne, AL (35967)	12036
Fort Payne, AL (35968)	4623
Fosters, AL (35463)	1386
Franklin, AL (36444)	498
Frisco City, AL (36445)	3214
Fruitdale, AL (36539)	518
Fruithurst, AL (36262)	1041
Fultondale, AL (35068)	5660
Fyffe, AL (35971)	3417
Gadsden, AL (35901)	13726
Gadsden, AL (35903)	13541
Gadsden, AL (35904)	10440
Gadsden, AL (35905)	5218
Rainbow City, AL (35906)	8064
Gadsden, AL (35907)	7049
Gainestown, AL (36540)	735
Gallant, AL (35972)	938
Gallion, AL (36742)	1925
Gardendale, AL (35071)	13095
Gaylesville, AL (35973)	2099
Geneva, AL (36340)	4255
Georgiana, AL (36033)	3062
Geraldine, AL (35974)	1379
Glenwood, AL (36034)	644
Goodwater, AL (35072)	3685
Gordo, AL (35466)	4526
Gordon, AL (36343)	1092
Goshen, AL (36035)	1462
Grady, AL (36036)	1552
Graham, AL (36263)	527
Grand Bay, AL (36541)	11291
Grant, AL (35747)	4377
Graysville, AL (35073)	2000
Greensboro, AL (36744)	5378
Greenville, AL (36037)	10687
Grove Hill, AL (36451)	4014
Groveoak, AL (35975)	769
Guin, AL (35563)	3124
Gulf Shores, AL (36542)	8103
Guntersville, AL (35976)	12769
Gurley, AL (35748)	5240
Hackleburg, AL (35564)	1725
Haleyville, AL (35565)	9940
Hamilton, AL (35570)	7881
Hanceville, AL (35077)	9797
Harpersville, AL (35078)	1768
Hartford, AL (36344)	3996
Hartselle, AL (35640)	20494
Harvest, AL (35749)	18078
Hayden, AL (35079)	6765
Hayneville, AL (36040)	3358
Hazel Green, AL (35750)	11022
Headland, AL (36345)	6449
Heflin, AL (36264)	6810
Helena, AL (35080)	13265
Henagar, AL (35978)	4203
Higdon, AL (35979)	1137
Highland Home, AL (36041)	1141
Hillsboro, AL (35643)	2726
Hodges, AL (35571)	689
Holly Pond, AL (35083)	2414
Hollywood, AL (35752)	1698
Honoraville, AL (36042)	1093
Hope Hull, AL (36043)	3276
Horton, AL (35980)	3464
Houston, AL (35572)	760
Huntsville, AL (35801)	17107
Huntsville, AL (35802)	18463
Huntsville, AL (35803)	22945
Huntsville, AL (35805)	14085
Huntsville, AL (35806)	14536
Huntsville, AL (35808)	896
Huntsville, AL (35810)	23653
Huntsville, AL (35811)	21737
Huntsville, AL (35816)	9519
Huntsville, AL (35824)	4681
Hurtsboro, AL (36860)	1321
Ider, AL (35981)	1689
Irvington, AL (36544)	8623
Jack, AL (36346)	1056
Jackson, AL (36545)	7645
Jacksons Gap, AL (36861)	2527
Jacksonville, AL (36265)	13993
Jasper, AL (35501)	6780
Jasper, AL (35503)	6595
Jasper, AL (35504)	9960
Jemison, AL (35085)	6949
Jones, AL (36749)	828
Joppa, AL (35087)	1612
Kellyton, AL (35089)	1559
Kennedy, AL (35574)	1141
Killen, AL (35645)	10904
Kimberly, AL (35091)	2157
Kinston, AL (36453)	1755
Laceys Spring, AL (35754)	4182
Lafayette, AL (36862)	4851
Lanett, AL (36863)	9401
Lapine, AL (36046)	1083
Leeds, AL (35094)	11438
Leesburg, AL (35983)	2794
Leighton, AL (35646)	3764
Leroy, AL (36548)	1008
Lester, AL (35647)	850
Letohatchee, AL (36047)	1321
Lexington, AL (35648)	3133
Lillian, AL (36549)	3781
Lincoln, AL (35096)	5883
Linden, AL (36748)	2729
Lineville, AL (36266)	4328
Livingston, AL (35470)	3520
Locust Fork, AL (35097)	1477
Logan, AL (35098)	1163
Louisville, AL (36048)	1199
Lower Peach Tree, AL (36751)	760
Lowndesboro, AL (36752)	1439
Loxley, AL (36551)	6160
Luverne, AL (36049)	4181
Lynn, AL (35575)	763
Mc Calla, AL (35111)	12111
Mc Intosh, AL (36553)	2482
Mc Kenzie, AL (36456)	1465
Madison, AL (35756)	7381
Madison, AL (35757)	10855
Madison, AL (35758)	36090
Magnolia Springs, AL (36555)	1177
Maplesville, AL (36750)	2328
Marbury, AL (36051)	1822
Marion, AL (36756)	4346
Marion Junction, AL (36759)	1224
Mathews, AL (36052)	693
Maylene, AL (35114)	5305
Mentone, AL (35984)	1458
Meridianville, AL (35759)	5666
Midland City, AL (36350)	5216
Midway, AL (36053)	1561
Millbrook, AL (36054)	11793
Millport, AL (35576)	2369
Millry, AL (36558)	2764
Minter, AL (36761)	867
Mobile, AL (36602)	660
Mobile, AL (36603)	4719
Mobile, AL (36604)	7219
Mobile, AL (36605)	22380
Mobile, AL (36606)	14562
Mobile, AL (36607)	4998
Mobile, AL (36608)	27204
Mobile, AL (36609)	18000
Mobile, AL (36610)	10612
Mobile, AL (36611)	4391
Mobile, AL (36612)	3472
Eight Mile, AL (36613)	9355
Mobile, AL (36617)	10659
Mobile, AL (36618)	13309
Mobile, AL (36619)	11946
Mobile, AL (36693)	14752
Mobile, AL (36695)	35754
Monroeville, AL (36460)	6386
Montevallo, AL (35115)	9197
Montgomery, AL (36104)	6082
Montgomery, AL (36105)	10388
Montgomery, AL (36106)	11624
Montgomery, AL (36107)	6403
Montgomery, AL (36108)	16861
Montgomery, AL (36109)	21380
Montgomery, AL (36110)	10126
Montgomery, AL (36111)	10764
Montgomery, AL (36113)	737
Montgomery, AL (36116)	33860
Montgomery, AL (36117)	37488
Moody, AL (35004)	8432
Morris, AL (35116)	3790
Moulton, AL (35650)	10664
Moundville, AL (35474)	5149
Mount Hope, AL (35651)	958
Mount Olive, AL (35117)	5103
Mount Vernon, AL (36560)	2564
Mulga, AL (35118)	2763
Munford, AL (36268)	4416
Muscadine, AL (36269)	944
Muscle Shoals, AL (35661)	13733
Nauvoo, AL (35578)	3931
Newbern, AL (36765)	1029
New Brockton, AL (36351)	2710
New Hope, AL (35760)	3967
New Market, AL (35761)	9306
Newton, AL (36352)	3874
Newville, AL (36353)	1595
Northport, AL (35473)	11384
Northport, AL (35475)	11642
Northport, AL (35476)	6220
Notasulga, AL (36866)	2985
Oakman, AL (35579)	2350
Odenville, AL (35120)	10676
Ohatchee, AL (36271)	4746
Oneonta, AL (35121)	11624
Opelika, AL (36801)	15849
Opelika, AL (36804)	13349
Opp, AL (36467)	7660
Orange Beach, AL (36561)	5533
Orrville, AL (36767)	1483
Owens Cross Roads, AL (35763)	12115
Ozark, AL (36360)	14902
Paint Rock, AL (35764)	492
Pansey, AL (36370)	733
Parrish, AL (35580)	3038
Pelham, AL (35124)	20038
Pell City, AL (35125)	7921
Pell City, AL (35128)	7224
Perdido, AL (36562)	1385
Peterman, AL (36471)	971
Phenix City, AL (36867)	14901
Phenix City, AL (36869)	14285
Phenix City, AL (36870)	12839
Phil Campbell, AL (35581)	4065
Piedmont, AL (36272)	9626
Pike Road, AL (36064)	5618
Pine Apple, AL (36768)	577
Pine Hill, AL (36769)	2265
Pinson, AL (35126)	18161
Pisgah, AL (35765)	2818
Pittsview, AL (36871)	849
Plantersville, AL (36758)	1093
Pleasant Grove, AL (35127)	8541
Prattville, AL (36066)	14600
Prattville, AL (36067)	21193
Quinton, AL (35130)	2403
Ragland, AL (35131)	2996
Rainsville, AL (35986)	6167
Ralph, AL (35480)	1213
Ramer, AL (36069)	1585
Ranburne, AL (36273)	2016
Randolph, AL (36792)	945
Red Bay, AL (35582)	3395
Red Level, AL (36474)	2154
Reform, AL (35481)	2774
Remlap, AL (35133)	3137
Repton, AL (36475)	1494
Riverside, AL (35135)	1451
Roanoke, AL (36274)	8257
Robertsdale, AL (36567)	9967
Seminole, AL (36574)	988
Rockford, AL (35136)	1407
Rogersville, AL (35652)	6280
Russellville, AL (35653)	9732
Russellville, AL (35654)	6181
Rutledge, AL (36071)	682
Saint Stephens, AL (36569)	659
Salem, AL (36874)	6131
Samson, AL (36477)	3400
Saraland, AL (36571)	12009
Sardis, AL (36775)	739
Satsuma, AL (36572)	5727
Sawyerville, AL (36776)	1251
Scottsboro, AL (35768)	9177
Scottsboro, AL (35769)	7517
Seale, AL (36875)	3521
Section, AL (35771)	2819
Selma, AL (36701)	17852
Selma, AL (36703)	8920
Semmes, AL (36575)	14723
Sheffield, AL (35660)	7187
Shelby, AL (35143)	2292
Shorter, AL (36075)	1779
Shorterville, AL (36373)	472
Silverhill, AL (36576)	3213
Skipperville, AL (36374)	927
Slocomb, AL (36375)	5530
Smiths Station, AL (36877)	9021
Somerville, AL (35670)	6087
Springville, AL (35146)	7845
Spruce Pine, AL (35585)	1209
Stapleton, AL (36578)	1509
Steele, AL (35987)	1965
Sterrett, AL (35147)	4332
Fackler, AL (35746)	691
Stevenson, AL (35772)	3742
Stockton, AL (36579)	1438
Sulligent, AL (35586)	3345
Sumiton, AL (35148)	2329
Summerdale, AL (36580)	4095
Sweet Water, AL (36782)	1831
Sylacauga, AL (35150)	14021
Sylacauga, AL (35151)	5722
Sylvania, AL (35988)	1400
Talladega, AL (35160)	18245
Tallassee, AL (36078)	10586
Tanner, AL (35671)	1705
Theodore, AL (36582)	18191
Thomaston, AL (36783)	661
Thomasville, AL (36784)	6604
Thorsby, AL (35171)	2679
Tibbie, AL (36583)	501
Titus, AL (36080)	1839
Toney, AL (35773)	10273
Town Creek, AL (35672)	5061
Townley, AL (35587)	693
Trafford, AL (35172)	2333
Trinity, AL (35673)	6649
Troy, AL (36079)	6165
Troy, AL (36081)	10180
Trussville, AL (35173)	22564
Tuscaloosa, AL (35401)	16255
Tuscaloosa, AL (35404)	13620
Tuscaloosa, AL (35405)	28170
Tuscaloosa, AL (35406)	10830
Tuscumbia, AL (35674)	14316
Tuskegee, AL (36083)	6807
Tuskegee Institute, AL (36088)	1889
Tyler, AL (36785)	1044
Union Grove, AL (35175)	4185
Union Springs, AL (36089)	5391
Uniontown, AL (36786)	2606
Uriah, AL (36480)	1399
Valhermoso Springs, AL (35775)	520
Valley, AL (36854)	11676
Valley Head, AL (35989)	2542
Vance, AL (35490)	3075
Vandiver, AL (35176)	707
Verbena, AL (36091)	2810
Vernon, AL (35592)	3651
Vina, AL (35593)	1338
Vincent, AL (35178)	2807
Vinegar Bend, AL (36584)	518
Vinemont, AL (35179)	7281
Wadley, AL (36276)	1756
Wagarville, AL (36585)	793
Warrior, AL (35180)	10996
Waterloo, AL (35677)	1409
Waverly, AL (36879)	1280
Weaver, AL (36277)	4524
Webb, AL (36376)	1828
Wedowee, AL (36278)	3275
Wellington, AL (36279)	2158
Weogufka, AL (35183)	574
West Blocton, AL (35184)	4193
Wetumpka, AL (36092)	16686
Wetumpka, AL (36093)	8743
Whatley, AL (36482)	794
Wilmer, AL (36587)	8082
Wilsonville, AL (35186)	3658
Winfield, AL (35594)	5887
Woodland, AL (36280)	2975
Woodstock, AL (35188)	2264
Woodville, AL (35776)	2758
Ardmore, AL (35739)	3887
Butler, AL (36904)	3280
Cuba, AL (36907)	1333
Gilbertown, AL (36908)	1829
Lisman, AL (36912)	1516
Pennington, AL (36916)	515
Silas, AL (36919)	1564
Toxey, AL (36921)	873
Ward, AL (36922)	504
York, AL (36925)	2395
Abbeville, MS (38601)	1784
Aberdeen, MS (39730)	8894
Ackerman, MS (39735)	2986
Amory, MS (38821)	9536
Anguilla, MS (38721)	970
Ashland, MS (38603)	2203
Bailey, MS (39320)	1483
Baldwyn, MS (38824)	6283
Bassfield, MS (39421)	2545
Batesville, MS (38606)	12504
Bay Saint Louis, MS (39520)	8359
Diamondhead, MS (39525)	6950
Pearlington, MS (39572)	914
Waveland, MS (39576)	3797
Bay Springs, MS (39422)	4491
Beaumont, MS (39423)	1960
Belden, MS (38826)	3831
Belmont, MS (38827)	2407
Belzoni, MS (39038)	4674
Benoit, MS (38725)	758
Benton, MS (39039)	1812
Bentonia, MS (39040)	2588
Biloxi, MS (39530)	5497
Biloxi, MS (39531)	12124
Biloxi, MS (39532)	24883
Diberville, MS (39540)	6371
Blue Mountain, MS (38610)	2435
Blue Springs, MS (38828)	3176
Bogue Chitto, MS (39629)	4790
Bolton, MS (39041)	2921
Booneville, MS (38829)	13211
New Site, MS (38859)	523
Boyle, MS (38730)	1539
Brandon, MS (39042)	26551
Brandon, MS (39047)	28833
Braxton, MS (39044)	2431
Brookhaven, MS (39601)	16719
Brooklyn, MS (39425)	1317
Brooksville, MS (39739)	2385
Bruce, MS (38915)	3237
Buckatunna, MS (39322)	1487
Bude, MS (39630)	785
Burnsville, MS (38833)	1850
Byhalia, MS (38611)	13055
Caledonia, MS (39740)	4013
Calhoun City, MS (38916)	3415
Camden, MS (39045)	1154
Canton, MS (39046)	20588
Carriere, MS (39426)	11857
Carrollton, MS (38917)	2512
Carson, MS (39427)	962
Carthage, MS (39051)	11734
Cascilla, MS (38920)	561
Cedarbluff, MS (39741)	1188
Centreville, MS (39631)	2627
Charleston, MS (38921)	3343
Chunky, MS (39323)	988
Clarksdale, MS (38614)	14062
Cleveland, MS (38732)	12577
Clinton, MS (39056)	20758
Coahoma, MS (38617)	480
Coffeeville, MS (38922)	2629
Coila, MS (38923)	941
Coldwater, MS (38618)	9294
Collins, MS (39428)	7305
Collinsville, MS (39325)	4923
Columbia, MS (39429)	12877
Columbus, MS (39701)	9383
Columbus, MS (39702)	16834
Columbus, MS (39705)	11121
Como, MS (38619)	3841
Conehatta, MS (39057)	1630
Corinth, MS (38834)	19260
Courtland, MS (38620)	2556
Crawford, MS (39743)	1616
Crenshaw, MS (38621)	1332
Crosby, MS (39633)	732
Cruger, MS (38924)	608
Crystal Springs, MS (39059)	8962
Daleville, MS (39326)	571
Decatur, MS (39327)	3078
De Kalb, MS (39328)	3501
Dennis, MS (38838)	1115
Drew, MS (38737)	2141
Duck Hill, MS (38925)	1809
Dumas, MS (38625)	766
Dundee, MS (38626)	960
Durant, MS (39063)	2735
Ecru, MS (38841)	2508
Edwards, MS (39066)	3500
Ellisville, MS (39437)	8960
Enid, MS (38927)	879
Enterprise, MS (39330)	2169
Ethel, MS (39067)	1026
Etta, MS (38627)	923
Eupora, MS (39744)	4472
Falkner, MS (38629)	1272
Fayette, MS (39069)	3899
Flora, MS (39071)	4237
Florence, MS (39073)	15468
Forest, MS (39074)	10722
Foxworth, MS (39483)	4727
French Camp, MS (39745)	659
Fulton, MS (38843)	8170
Gautier, MS (39553)	13379
Georgetown, MS (39078)	615
Glen, MS (38846)	1765
Glen Allan, MS (38744)	676
Gloster, MS (39638)	2449
Golden, MS (38847)	2592
Goodman, MS (39079)	1308
Gore Springs, MS (38929)	976
Greenville, MS (38701)	17629
Greenville, MS (38703)	9461
Greenwood, MS (38930)	17053
Greenwood Springs, MS (38848)	656
Grenada, MS (38901)	13430
Gulfport, MS (39501)	14519
Gulfport, MS (39503)	33916
Gulfport, MS (39507)	12140
Guntown, MS (38849)	4127
Hamilton, MS (39746)	2549
Harrisville, MS (39082)	1038
Hattiesburg, MS (39401)	27486
Hattiesburg, MS (39402)	27793
Hazlehurst, MS (39083)	7946
Heidelberg, MS (39439)	3578
Hermanville, MS (39086)	1808
Hernando, MS (38632)	20071
Hickory, MS (39332)	1412
Hickory Flat, MS (38633)	1709
Holcomb, MS (38940)	1554
Hollandale, MS (38748)	2886
Holly Springs, MS (38635)	10658
Horn Lake, MS (38637)	20486
Houlka, MS (38850)	2656
Houston, MS (38851)	6604
Indianola, MS (38751)	8896
Inverness, MS (38753)	1246
Isola, MS (38754)	1256
Itta Bena, MS (38941)	3110
Iuka, MS (38852)	6756
Jackson, MS (39201)	407
Jackson, MS (39202)	5162
Jackson, MS (39203)	3973
Jackson, MS (39204)	12836
Jackson, MS (39206)	19006
Pearl, MS (39208)	21916
Jackson, MS (39209)	21859
Jackson, MS (39211)	18806
Jackson, MS (39212)	24414
Jackson, MS (39213)	17191
Jackson, MS (39216)	2521
Richland, MS (39218)	5496
Flowood, MS (39232)	5340
Byram, MS (39272)	10412
Jayess, MS (39641)	3282
Kilmichael, MS (39747)	1378
Kiln, MS (39556)	5321
Kokomo, MS (39643)	1005
Kosciusko, MS (39090)	9789
Lake, MS (39092)	2446
Lake Cormorant, MS (38641)	1952
Lamar, MS (38642)	1901
Lambert, MS (38643)	1620
Lauderdale, MS (39335)	2536
Laurel, MS (39440)	13723
Laurel, MS (39443)	17235
Lawrence, MS (39336)	1127
Leakesville, MS (39451)	3111
Leland, MS (38756)	5547
Lena, MS (39094)	2813
Lexington, MS (39095)	5211
Liberty, MS (39645)	3881
Little Rock, MS (39337)	1431
Long Beach, MS (39560)	13545
Lorman, MS (39096)	1507
Louin, MS (39338)	2344
Louise, MS (39097)	631
Louisville, MS (39339)	11855
Lucedale, MS (39452)	19596
Lumberton, MS (39455)	6728
Lyon, MS (38645)	1236
Mc Call Creek, MS (39647)	871
Mc Carley, MS (38943)	527
Mccomb, MS (39648)	14847
Mc Cool, MS (39108)	1399
Mc Henry, MS (39561)	1331
Mc Lain, MS (39456)	1156
Maben, MS (39750)	2204
Macon, MS (39341)	5664
Madison, MS (39110)	30789
Magee, MS (39111)	7398
Magnolia, MS (39652)	6103
Mantachie, MS (38855)	3563
Mantee, MS (39751)	1045
Marietta, MS (38856)	1380
Marion, MS (39342)	1300
Marks, MS (38646)	2304
Mathiston, MS (39752)	1857
Meadville, MS (39653)	2285
Mendenhall, MS (39114)	7230
Meridian, MS (39301)	18824
Meridian, MS (39305)	15228
Meridian, MS (39307)	11208
Merigold, MS (38759)	1156
Michigan City, MS (38647)	776
Mize, MS (39116)	1899
Monticello, MS (39654)	4746
Mooreville, MS (38857)	2621
Moorhead, MS (38761)	1740
Morton, MS (39117)	7390
Moselle, MS (39459)	2523
Mound Bayou, MS (38762)	1545
Mount Olive, MS (39119)	4137
Myrtle, MS (38650)	2838
Natchez, MS (39120)	20822
Nesbit, MS (38651)	6154
Nettleton, MS (38858)	5263
New Albany, MS (38652)	13289
New Augusta, MS (39462)	920
Newhebron, MS (39140)	1745
Newton, MS (39345)	4909
Noxapater, MS (39346)	1716
Oakland, MS (38948)	1576
Oak Vale, MS (39656)	710
Ocean Springs, MS (39564)	28673
Vancleave, MS (39565)	15113
Okolona, MS (38860)	4719
Olive Branch, MS (38654)	38281
Osyka, MS (39657)	1819
Ovett, MS (39464)	1793
Oxford, MS (38655)	23547
Pachuta, MS (39347)	1142
Moss Point, MS (39562)	13059
Moss Point, MS (39563)	10216
Pascagoula, MS (39567)	7423
Pascagoula, MS (39581)	8759
Pass Christian, MS (39571)	9818
Pattison, MS (39144)	1087
Pelahatchie, MS (39145)	4171
Perkinston, MS (39573)	5897
Petal, MS (39465)	16917
Pheba, MS (39755)	823
Philadelphia, MS (39350)	19037
Picayune, MS (39466)	19966
Pickens, MS (39146)	2195
Vaughan, MS (39179)	843
Pinola, MS (39149)	1220
Pittsboro, MS (38951)	722
Plantersville, MS (38862)	2194
Pontotoc, MS (38863)	15383
Pope, MS (38658)	1719
Poplarville, MS (39470)	8656
Porterville, MS (39352)	639
Port Gibson, MS (39150)	4569
Potts Camp, MS (38659)	2163
Prairie, MS (39756)	1593
Prentiss, MS (39474)	4780
Preston, MS (39354)	1372
Pulaski, MS (39152)	945
Purvis, MS (39475)	9441
Quitman, MS (39355)	5371
Raleigh, MS (39153)	2756
Randolph, MS (38864)	1038
Raymond, MS (39154)	7133
Red Banks, MS (38661)	1439
Redwood, MS (39156)	578
Richton, MS (39476)	5841
Ridgeland, MS (39157)	18046
Rienzi, MS (38865)	3815
Ripley, MS (38663)	9444
Robinsonville, MS (38664)	2301
Rolling Fork, MS (39159)	2177
Rosedale, MS (38769)	1670
Rose Hill, MS (39356)	583
Roxie, MS (39661)	2149
Ruleville, MS (38771)	2314
Ruth, MS (39662)	1002
Sallis, MS (39160)	2102
Saltillo, MS (38866)	9642
Sandy Hook, MS (39478)	1593
Sarah, MS (38665)	1832
Sardis, MS (38666)	5090
Saucier, MS (39574)	10561
Schlater, MS (38952)	500
Scobey, MS (38953)	518
Scooba, MS (39358)	1132
Seminary, MS (39479)	4385
Senatobia, MS (38668)	10493
Shannon, MS (38868)	4249
Shaw, MS (38773)	2409
Shelby, MS (38774)	1807
Shubuta, MS (39360)	3048
Shuqualak, MS (39361)	1133
Sidon, MS (38954)	1032
Silver Creek, MS (39663)	2032
Sledge, MS (38670)	998
Smithdale, MS (39664)	1622
Smithville, MS (38870)	2366
Sontag, MS (39665)	719
Soso, MS (39480)	2160
Southaven, MS (38671)	28707
Southaven, MS (38672)	8609
Starkville, MS (39759)	24708
State Line, MS (39362)	2025
Steens, MS (39766)	2097
Stewart, MS (39767)	587
Stonewall, MS (39363)	1355
Stringer, MS (39481)	1345
Sturgis, MS (39769)	1386
Summit, MS (39666)	7553
Sumrall, MS (39482)	7379
Sunflower, MS (38778)	1245
Taylor, MS (38673)	714
Taylorsville, MS (39168)	5086
Tchula, MS (39169)	2222
Terry, MS (39170)	8155
Thaxton, MS (38871)	1414
Tillatoba, MS (38961)	712
Tiplersville, MS (38674)	741
Tishomingo, MS (38873)	2166
Toomsuba, MS (39364)	2351
Tremont, MS (38876)	944
Tunica, MS (38676)	5443
Tupelo, MS (38801)	20894
Tupelo, MS (38804)	12150
Tutwiler, MS (38963)	1167
Tylertown, MS (39667)	9415
Union, MS (39365)	5667
Union Church, MS (39668)	514
Utica, MS (39175)	3952
Vaiden, MS (39176)	1530
Vardaman, MS (38878)	2020
Vicksburg, MS (39180)	25610
Vicksburg, MS (39183)	12027
Vossburg, MS (39366)	1094
Walls, MS (38680)	4919
Walnut, MS (38683)	3593
Walnut Grove, MS (39189)	2605
Waterford, MS (38685)	992
Water Valley, MS (38965)	6726
Waynesboro, MS (39367)	11551
Webb, MS (38966)	926
Weir, MS (39772)	1351
Wesson, MS (39191)	6048
West, MS (39192)	1261
West Point, MS (39773)	12412
Wiggins, MS (39577)	7450
Winona, MS (38967)	5619
Woodland, MS (39776)	1325
Woodville, MS (39669)	4031
Yazoo City, MS (39194)	12017
Abbeville, LA (70510)	17840
Abita Springs, LA (70420)	6539
Addis, LA (70710)	2994
Albany, LA (70711)	4417
Alexandria, LA (71301)	16189
Alexandria, LA (71302)	10746
Alexandria, LA (71303)	15512
Ama, LA (70031)	1236
Amite, LA (70422)	9632
Anacoco, LA (71403)	3508
Angie, LA (70426)	3433
Arabi, LA (70032)	2200
Arcadia, LA (71001)	3420
Arnaudville, LA (70512)	7333
Athens, LA (71003)	793
Atlanta, LA (71404)	622
Baker, LA (70714)	15207
Baldwin, LA (70514)	2287
Ball, LA (71405)	4354
Barataria, LA (70036)	835
Basile, LA (70515)	2443
Baskin, LA (71219)	1013
Bastrop, LA (71220)	17198
Batchelor, LA (70715)	947
Baton Rouge, LA (70802)	19156
Baton Rouge, LA (70805)	23752
Baton Rouge, LA (70806)	20840
Baton Rouge, LA (70807)	12421
Baton Rouge, LA (70808)	22872
Baton Rouge, LA (70809)	18895
Baton Rouge, LA (70810)	29589
Baton Rouge, LA (70811)	11086
Baton Rouge, LA (70812)	8832
Baton Rouge, LA (70814)	11447
Baton Rouge, LA (70815)	22747
Baton Rouge, LA (70816)	32224
Baton Rouge, LA (70817)	26680
Baton Rouge, LA (70818)	7923
Baton Rouge, LA (70819)	3837
Baton Rouge, LA (70820)	7370
Belcher, LA (71004)	510
Bell City, LA (70630)	1086
Belle Chasse, LA (70037)	12103
Belle Rose, LA (70341)	2739
Bentley, LA (71407)	837
Benton, LA (71006)	10129
Bernice, LA (71222)	2432
Berwick, LA (70342)	4079
Bethany, LA (71007)	909
Bienville, LA (71008)	545
Bogalusa, LA (70427)	12826
Bossier City, LA (71111)	28820
Bossier City, LA (71112)	24568
Bourg, LA (70343)	4698
Boutte, LA (70039)	2476
Boyce, LA (71409)	5247
Braithwaite, LA (70040)	1258
Branch, LA (70516)	1094
Breaux Bridge, LA (70517)	20374
Broussard, LA (70518)	10832
Brusly, LA (70719)	3639
Bunkie, LA (71322)	4912
Buras, LA (70041)	1493
Bush, LA (70431)	4163
Calhoun, LA (71225)	5535
Cameron, LA (70631)	1001
Campti, LA (71411)	2153
Carencro, LA (70520)	14627
Carville, LA (70721)	456
Castor, LA (71016)	1476
Center Point, LA (71323)	777
Chalmette, LA (70043)	9194
Chatham, LA (71226)	1277
Chauvin, LA (70344)	4345
Cheneyville, LA (71325)	905
Choudrant, LA (71227)	2830
Church Point, LA (70525)	9719
Clayton, LA (71326)	1013
Clinton, LA (70722)	5392
Cloutierville, LA (71416)	560
Colfax, LA (71417)	3684
Collinston, LA (71229)	1389
Columbia, LA (71418)	5019
Convent, LA (70723)	1292
Converse, LA (71419)	1658
Cottonport, LA (71327)	2922
Cotton Valley, LA (71018)	1290
Coushatta, LA (71019)	6374
Covington, LA (70433)	24011
Covington, LA (70435)	12376
Crowley, LA (70526)	12571
Cut Off, LA (70345)	8375
Darrow, LA (70725)	1411
Delcambre, LA (70528)	2090
Delhi, LA (71232)	5067
Denham Springs, LA (70706)	15282
Denham Springs, LA (70726)	37331
Dequincy, LA (70633)	5903
Deridder, LA (70634)	18485
Des Allemands, LA (70030)	3329
Destrehan, LA (70047)	10859
Deville, LA (71328)	5970
Dodson, LA (71422)	1149
Donaldsonville, LA (70346)	8408
Downsville, LA (71234)	3359
Doyline, LA (71023)	2854
Dry Creek, LA (70637)	657
Dry Prong, LA (71423)	3787
Dubach, LA (71235)	3306
Dubberly, LA (71024)	951
Dulac, LA (70353)	910
Theriot, LA (70397)	1015
Duson, LA (70529)	8613
Edgard, LA (70049)	1963
Effie, LA (71331)	858
Egan, LA (70531)	1009
Elmer, LA (71424)	984
Elm Grove, LA (71051)	1815
Elton, LA (70532)	2325
Epps, LA (71237)	975
Erath, LA (70533)	5498
Eros, LA (71238)	2211
Erwinville, LA (70729)	997
Ethel, LA (70730)	2958
Eunice, LA (70535)	13882
Evangeline, LA (70537)	500
Evans, LA (70639)	479
Evergreen, LA (71333)	580
Farmerville, LA (71241)	7699
Ferriday, LA (71334)	5957
Florien, LA (71429)	2332
Folsom, LA (70437)	5997
Fordoche, LA (70732)	949
Forest Hill, LA (71430)	1848
Franklin, LA (70538)	10497
Franklinton, LA (70438)	13141
French Settlement, LA (70733)	1436
Frierson, LA (71027)	1466
Galliano, LA (70354)	3861
Garyville, LA (70051)	1921
Geismar, LA (70734)	5522
Georgetown, LA (71432)	800
Gibsland, LA (71028)	1238
Gibson, LA (70356)	1847
Gilbert, LA (71336)	1231
Glenmora, LA (71433)	3236
Gloster, LA (71030)	1204
Golden Meadow, LA (70357)	2262
Goldonna, LA (71031)	726
Gonzales, LA (70737)	27923
Grambling, LA (71245)	1797
Gramercy, LA (70052)	3061
Grand Cane, LA (71032)	1733
Grand Isle, LA (70358)	829
Gray, LA (70359)	6633
Grayson, LA (71435)	2217
Greensburg, LA (70441)	3865
Greenwell Springs, LA (70739)	10194
Greenwood, LA (71033)	2901
Gretna, LA (70053)	11252
Gretna, LA (70056)	28775
Grosse Tete, LA (70740)	1098
Gueydan, LA (70542)	2578
Hackberry, LA (70645)	1026
Hahnville, LA (70057)	3323
Hammond, LA (70401)	11915
Hammond, LA (70403)	16918
Harrisonburg, LA (71340)	896
Harvey, LA (70058)	30072
Haughton, LA (71037)	15865
Haynesville, LA (71038)	3024
Heflin, LA (71039)	1552
Hessmer, LA (71341)	2533
Hineston, LA (71438)	1392
Holden, LA (70744)	3946
Homer, LA (71040)	5733
Hornbeck, LA (71439)	1430
Houma, LA (70360)	20939
Houma, LA (70363)	19630
Houma, LA (70364)	22983
Ida, LA (71044)	480
Independence, LA (70443)	7595
Iota, LA (70543)	2854
Iowa, LA (70647)	6960
Jackson, LA (70748)	3908
Jamestown, LA (71045)	508
Jarreau, LA (70749)	1087
Jeanerette, LA (70544)	9083
Jena, LA (71342)	5458
Jennings, LA (70546)	12538
Jonesboro, LA (71251)	6146
Jonesville, LA (71343)	5711
Kaplan, LA (70548)	7866
Keatchie, LA (71046)	1087
Keithville, LA (71047)	9288
Kenner, LA (70062)	11906
Kenner, LA (70065)	39430
Kentwood, LA (70444)	7259
Kinder, LA (70648)	4973
Krotz Springs, LA (70750)	1498
Labadieville, LA (70372)	2249
Lacombe, LA (70445)	8065
Lafayette, LA (70501)	21063
Lafayette, LA (70503)	20873
Lafayette, LA (70506)	28238
Lafayette, LA (70507)	12104
Lafayette, LA (70508)	26603
Lafitte, LA (70067)	2600
Lake Arthur, LA (70549)	3089
Lake Charles, LA (70601)	23817
Lake Charles, LA (70605)	26020
Lake Charles, LA (70607)	17926
Lake Charles, LA (70611)	14878
Lake Charles, LA (70615)	8675
Lakeland, LA (70752)	724
Lake Providence, LA (71254)	4378
La Place, LA (70068)	26678
Larose, LA (70373)	3923
Lecompte, LA (71346)	2267
Leesville, LA (71446)	15632
Fort Polk, LA (71459)	8070
Lena, LA (71447)	1000
Lettsworth, LA (70753)	686
Livingston, LA (70754)	7489
Livonia, LA (70755)	1801
Lockport, LA (70374)	6648
Logansport, LA (71049)	2475
Longville, LA (70652)	1627
Loranger, LA (70446)	4580
Loreauville, LA (70552)	1719
Luling, LA (70070)	10451
Lutcher, LA (70071)	2934
Madisonville, LA (70447)	8502
Mamou, LA (70554)	3940
Mandeville, LA (70448)	19852
Mandeville, LA (70471)	17415
Mangham, LA (71259)	1407
Mansfield, LA (71052)	8132
Mansura, LA (71350)	3177
Many, LA (71449)	6784
Maringouin, LA (70757)	2405
Marion, LA (71260)	2280
Marksville, LA (71351)	8767
Marrero, LA (70072)	43652
Marthaville, LA (71450)	845
Gheens, LA (70355)	768
Maurepas, LA (70449)	2666
Maurice, LA (70555)	5744
Melville, LA (71353)	1266
Meraux, LA (70075)	3080
Mer Rouge, LA (71261)	1354
Merryville, LA (70653)	2288
Metairie, LA (70001)	29137
Metairie, LA (70002)	14804
Metairie, LA (70003)	32396
Metairie, LA (70005)	19374
Metairie, LA (70006)	12066
Minden, LA (71055)	14849
Monroe, LA (71201)	15865
Monroe, LA (71202)	19485
Monroe, LA (71203)	25521
Montegut, LA (70377)	2974
Monterey, LA (71354)	1291
Montgomery, LA (71454)	1854
Mooringsport, LA (71060)	2246
Moreauville, LA (71355)	1977
Morgan City, LA (70380)	14869
Morganza, LA (70759)	1195
Morrow, LA (71356)	502
Morse, LA (70559)	1843
Mount Hermon, LA (70450)	1949
Napoleonville, LA (70390)	4938
Natchez, LA (71456)	943
Natchitoches, LA (71457)	17899
Newellton, LA (71357)	1496
New Iberia, LA (70560)	30351
New Iberia, LA (70563)	15059
New Llano, LA (71461)	2550
New Orleans, LA (70112)	2310
New Orleans, LA (70113)	3904
New Orleans, LA (70114)	14948
New Orleans, LA (70115)	21122
New Orleans, LA (70116)	6580
New Orleans, LA (70117)	13723
New Orleans, LA (70118)	19145
New Orleans, LA (70119)	19593
New Orleans, LA (70121)	8941
New Orleans, LA (70122)	17565
New Orleans, LA (70123)	21377
New Orleans, LA (70124)	11455
New Orleans, LA (70125)	8350
New Orleans, LA (70126)	14185
New Orleans, LA (70127)	12242
New Orleans, LA (70128)	11289
New Orleans, LA (70129)	5668
New Orleans, LA (70130)	9360
New Orleans, LA (70131)	20262
New Roads, LA (70760)	5511
Noble, LA (71462)	1049
Norco, LA (70079)	2762
Norwood, LA (70761)	678
Oakdale, LA (71463)	6178
Oak Grove, LA (71263)	6022
Oak Ridge, LA (71264)	743
Oberlin, LA (70655)	2353
Oil City, LA (71061)	1302
Olla, LA (71465)	2270
Opelousas, LA (70570)	27210
Oscar, LA (70762)	731
Palmetto, LA (71358)	836
Paradis, LA (70080)	1295
Patterson, LA (70392)	6645
Paulina, LA (70763)	2974
Pearl River, LA (70452)	10024
Pelican, LA (71063)	570
Pierre Part, LA (70339)	4656
Pine Grove, LA (70453)	1109
Pineville, LA (71360)	25865
Pioneer, LA (71266)	1120
Pitkin, LA (70656)	2780
Plain Dealing, LA (71064)	2783
Plaquemine, LA (70764)	13072
Plattenville, LA (70393)	718
Plaucheville, LA (71362)	1477
Pleasant Hill, LA (71065)	872
Pollock, LA (71467)	3894
Ponchatoula, LA (70454)	19878
Port Allen, LA (70767)	11802
Port Barre, LA (70577)	3909
Port Sulphur, LA (70083)	1803
Prairieville, LA (70769)	29593
Pride, LA (70770)	3175
Princeton, LA (71067)	2544
Provencal, LA (71468)	772
Quitman, LA (71268)	2205
Raceland, LA (70394)	11250
Ragley, LA (70657)	3450
Rayne, LA (70578)	12139
Rayville, LA (71269)	8709
Reeves, LA (70658)	627
Reserve, LA (70084)	6122
Ringgold, LA (71068)	2665
Roanoke, LA (70581)	781
Robeline, LA (71469)	2019
Robert, LA (70455)	1604
Rodessa, LA (71069)	509
Rosedale, LA (70772)	688
Roseland, LA (70456)	2206
Ruston, LA (71270)	19846
Saint Amant, LA (70774)	8129
Saint Bernard, LA (70085)	2956
Saint Francisville, LA (70775)	7015
Saint Gabriel, LA (70776)	2125
Saint James, LA (70086)	1700
Saint Joseph, LA (71366)	1479
Saint Landry, LA (71367)	972
Saint Martinville, LA (70582)	15665
Saint Rose, LA (70087)	6166
Saline, LA (71070)	1225
Sarepta, LA (71071)	2057
Schriever, LA (70395)	4127
Scott, LA (70583)	9559
Shongaloo, LA (71072)	1197
Shreveport, LA (71101)	5434
Shreveport, LA (71103)	5143
Shreveport, LA (71104)	10342
Shreveport, LA (71105)	17078
Shreveport, LA (71106)	26752
Shreveport, LA (71107)	23793
Shreveport, LA (71108)	15079
Shreveport, LA (71109)	16515
Barksdale Afb, LA (71110)	2409
Shreveport, LA (71115)	11045
Shreveport, LA (71118)	19263
Shreveport, LA (71119)	9344
Shreveport, LA (71129)	10701
Sibley, LA (71073)	1896
Sicily Island, LA (71368)	1021
Simmesport, LA (71369)	2260
Simsboro, LA (71275)	1853
Singer, LA (70660)	1124
Slaughter, LA (70777)	3458
Slidell, LA (70458)	26965
Slidell, LA (70460)	16334
Slidell, LA (70461)	21515
Sorrento, LA (70778)	1848
Spearsville, LA (71277)	1330
Springfield, LA (70462)	4392
Springhill, LA (71075)	4351
Starks, LA (70661)	1517
Sterlington, LA (71280)	3177
Stonewall, LA (71078)	4470
Sulphur, LA (70663)	21792
Sulphur, LA (70665)	8168
Sunset, LA (70584)	5381
Sunshine, LA (70780)	801
Tallulah, LA (71282)	6505
Thibodaux, LA (70301)	31447
Tickfaw, LA (70466)	5302
Trout, LA (71371)	1437
Tullos, LA (71479)	530
Vacherie, LA (70090)	6477
Ventress, LA (70783)	2084
Vidalia, LA (71373)	5776
Ville Platte, LA (70586)	14372
Vinton, LA (70668)	4689
Violet, LA (70092)	4367
Vivian, LA (71082)	3701
Walker, LA (70785)	16008
Washington, LA (70589)	2916
Waterproof, LA (71375)	803
Welsh, LA (70591)	3880
Westlake, LA (70669)	7999
West Monroe, LA (71291)	25673
West Monroe, LA (71292)	16401
Westwego, LA (70094)	23858
White Castle, LA (70788)	3354
Wilson, LA (70789)	639
Winnfield, LA (71483)	7037
Winnsboro, LA (71295)	9768
Wisner, LA (71378)	1856
Woodworth, LA (71485)	1866
Youngsville, LA (70592)	15425
Zachary, LA (70791)	20591
Zwolle, LA (71486)	3460
Alexander, AR (72002)	10934
Alma, AR (72921)	10449
Almyra, AR (72003)	637
Alpena, AR (72611)	1393
Altheimer, AR (72004)	1114
Altus, AR (72821)	1267
Amity, AR (71921)	2241
Arkadelphia, AR (71923)	10677
Ashdown, AR (71822)	6403
Ash Flat, AR (72513)	2012
Atkins, AR (72823)	4937
Augusta, AR (72006)	1925
Austin, AR (72007)	5935
Bald Knob, AR (72010)	4850
Banks, AR (71631)	521
Batesville, AR (72501)	17349
Bauxite, AR (72011)	3426
Bay, AR (72411)	1762
Bearden, AR (71720)	1962
Beebe, AR (72012)	9445
Bee Branch, AR (72013)	1511
Belleville, AR (72824)	1036
Benton, AR (72015)	20776
Benton, AR (72019)	17934
Bryant, AR (72022)	11149
Bentonville, AR (72712)	32352
Bella Vista, AR (72714)	11127
Bella Vista, AR (72715)	11917
Berryville, AR (72616)	7830
Bigelow, AR (72016)	2306
Biscoe, AR (72017)	534
Bismarck, AR (71929)	3420
Black Rock, AR (72415)	997
Blytheville, AR (72315)	16578
Bonnerdale, AR (71933)	1020
Bono, AR (72416)	4172
Booneville, AR (72927)	6355
Bradford, AR (72020)	2987
Bradley, AR (71826)	835
Branch, AR (72928)	563
Brinkley, AR (72021)	3279
Brookland, AR (72417)	2653
Buckner, AR (71827)	598
Bull Shoals, AR (72619)	1555
Cabot, AR (72023)	28306
Caddo Gap, AR (71935)	527
Calico Rock, AR (72519)	1919
Camden, AR (71701)	14266
Canehill, AR (72717)	618
Caraway, AR (72419)	1332
Carlisle, AR (72024)	2802
Casa, AR (72025)	619
Cave City, AR (72521)	3567
Cave Springs, AR (72718)	1244
Cedarville, AR (72932)	1264
Center Ridge, AR (72027)	1099
Centerton, AR (72719)	6721
Charleston, AR (72933)	3712
Cherry Valley, AR (72324)	1598
Chester, AR (72934)	592
Chidester, AR (71726)	959
Clarendon, AR (72029)	1461
Clarkridge, AR (72623)	522
Clarksville, AR (72830)	10878
Cleveland, AR (72030)	537
Clinton, AR (72031)	5600
Coal Hill, AR (72832)	759
Colt, AR (72326)	1746
Concord, AR (72523)	795
Conway, AR (72032)	22042
Conway, AR (72034)	30339
Corning, AR (72422)	3526
Cotter, AR (72626)	900
Cotton Plant, AR (72036)	546
Cove, AR (71937)	1279
Crawfordsville, AR (72327)	1282
Crossett, AR (71635)	9824
Damascus, AR (72039)	1700
Danville, AR (72833)	3684
Dardanelle, AR (72834)	7387
Decatur, AR (72722)	2056
Deer, AR (72628)	569
Delaware, AR (72835)	607
Delight, AR (71940)	1154
De Queen, AR (71832)	7166
Dermott, AR (71638)	2301
Des Arc, AR (72040)	2166
Desha, AR (72527)	549
De Valls Bluff, AR (72041)	1037
De Witt, AR (72042)	4142
Dierks, AR (71833)	1774
Doddridge, AR (71834)	937
Marble Falls, AR (72648)	546
Donaldson, AR (71941)	1479
Dover, AR (72837)	6130
Drasco, AR (72530)	1505
Dumas, AR (71639)	4980
Dyess, AR (72330)	548
Earle, AR (72331)	2154
Edgemont, AR (72044)	679
Elaine, AR (72333)	654
El Dorado, AR (71730)	25409
Elizabeth, AR (72531)	517
Elkins, AR (72727)	4305
El Paso, AR (72045)	947
Emerson, AR (71740)	1262
Emmet, AR (71835)	1055
England, AR (72046)	3166
Enola, AR (72047)	787
Eudora, AR (71640)	2159
Eureka Springs, AR (72631)	3172
Eureka Springs, AR (72632)	3420
Evening Shade, AR (72532)	1178
Everton, AR (72633)	1126
Farmington, AR (72730)	6363
Fayetteville, AR (72701)	22206
Fayetteville, AR (72703)	20028
Fayetteville, AR (72704)	14751
Flippin, AR (72634)	3636
Floral, AR (72534)	1014
Fordyce, AR (71742)	4142
Foreman, AR (71836)	2202
Forrest City, AR (72335)	9094
Fort Smith, AR (72901)	14409
Fort Smith, AR (72903)	19254
Fort Smith, AR (72904)	14618
Fort Smith, AR (72908)	10334
Fort Smith, AR (72916)	5859
Barling, AR (72923)	3533
Fouke, AR (71837)	3736
Fountain Hill, AR (71642)	519
Horseshoe Bend, AR (72512)	1488
Fulton, AR (71838)	808
Gamaliel, AR (72537)	589
Garfield, AR (72732)	3331
Gassville, AR (72635)	2681
Gentry, AR (72734)	5426
Gillett, AR (72055)	703
Gillham, AR (71841)	662
Glenwood, AR (71943)	3402
Gould, AR (71643)	923
Grady, AR (71644)	635
Grannis, AR (71944)	511
Grapevine, AR (72057)	804
Gravette, AR (72736)	4442
Greenbrier, AR (72058)	11950
Green Forest, AR (72638)	5053
Greenwood, AR (72936)	11509
Griffithville, AR (72060)	513
Gurdon, AR (71743)	3108
Hackett, AR (72937)	2741
Hamburg, AR (71646)	4920
Hampton, AR (71744)	2252
Cherokee Village, AR (72529)	2905
Hardy, AR (72542)	2693
Harrisburg, AR (72432)	4474
Harrison, AR (72601)	20939
Hartford, AR (72938)	989
Hartman, AR (72840)	1394
Hatfield, AR (71945)	1069
Hattieville, AR (72063)	1224
Havana, AR (72842)	1090
Hazen, AR (72064)	1934
Heber Springs, AR (72543)	9662
Hector, AR (72843)	1641
Helena, AR (72342)	3499
Henderson, AR (72544)	478
Hensley, AR (72065)	3942
Hermitage, AR (71647)	1420
Heth, AR (72346)	554
Hickory Ridge, AR (72347)	604
Higden, AR (72067)	2141
Hindsville, AR (72738)	1824
Holly Grove, AR (72069)	1037
Hope, AR (71801)	10772
Horatio, AR (71842)	1713
Hot Springs National Park, AR (71901)	20695
Hot Springs Village, AR (71909)	14259
Hot Springs National Park, AR (71913)	32485
Houston, AR (72070)	1304
Hoxie, AR (72433)	1960
Hughes, AR (72348)	1777
Humphrey, AR (72073)	1017
Huntington, AR (72940)	1848
Huntsville, AR (72740)	7130
Huttig, AR (71747)	742
Imboden, AR (72434)	1513
Jacksonville, AR (72076)	28950
Jasper, AR (72641)	1856
Jefferson, AR (72079)	589
Jerusalem, AR (72080)	486
Jessieville, AR (71949)	1404
Joiner, AR (72350)	735
Jonesboro, AR (72401)	35408
Jonesboro, AR (72404)	16938
Judsonia, AR (72081)	5878
Junction City, AR (71749)	2213
Kensett, AR (72082)	1419
Kingsland, AR (71652)	784
Kingston, AR (72742)	481
Kirby, AR (71950)	717
Knoxville, AR (72845)	966
Lake City, AR (72437)	2347
Lakeview, AR (72642)	1539
Lake Village, AR (71653)	3790
Lamar, AR (72846)	2883
Lavaca, AR (72941)	4144
Leachville, AR (72438)	1872
Lead Hill, AR (72644)	1695
Leola, AR (72084)	879
Lepanto, AR (72354)	1712
Leslie, AR (72645)	1143
Lewisville, AR (71845)	1551
Lexa, AR (72355)	1824
Lincoln, AR (72744)	3801
Little Rock, AR (72201)	681
Little Rock, AR (72202)	6514
Little Rock, AR (72204)	22064
Little Rock, AR (72205)	17073
Little Rock, AR (72206)	17421
Little Rock, AR (72207)	9222
Little Rock, AR (72209)	23413
Little Rock, AR (72210)	10884
Little Rock, AR (72211)	17089
Little Rock, AR (72212)	11084
Little Rock, AR (72223)	16147
Little Rock, AR (72227)	9248
Lockesburg, AR (71846)	1824
Locust Grove, AR (72550)	655
London, AR (72847)	2073
Lonoke, AR (72086)	8303
Lonsdale, AR (72087)	1210
Louann, AR (71751)	689
Lowell, AR (72745)	8734
Luxora, AR (72358)	1022
Mc Caskill, AR (71847)	485
Mc Crory, AR (72101)	2552
Mc Gehee, AR (71654)	3325
Mc Neil, AR (71752)	740
Mc Rae, AR (72102)	2108
Mabelvale, AR (72103)	10226
Magazine, AR (72943)	1813
Magnolia, AR (71753)	10607
Malvern, AR (72104)	16575
Mammoth Spring, AR (72554)	2069
Manila, AR (72442)	3593
Mansfield, AR (72944)	2163
Marianna, AR (72360)	4337
Marion, AR (72364)	12808
Marked Tree, AR (72365)	2179
Lafe, AR (72436)	783
Marmaduke, AR (72443)	2148
Marshall, AR (72650)	3329
Marvell, AR (72366)	1629
Mayflower, AR (72106)	4383
Maynard, AR (72444)	1330
Melbourne, AR (72556)	2504
Mena, AR (71953)	10761
Midway, AR (72651)	1008
Mineral Springs, AR (71851)	1708
Monette, AR (72447)	1365
Monticello, AR (71655)	9794
Montrose, AR (71658)	551
Moro, AR (72368)	767
Morrilton, AR (72110)	8528
Mountainburg, AR (72946)	2530
Mountain Home, AR (72653)	21399
Mountain Pine, AR (71956)	1534
Mountain View, AR (72560)	6398
Mount Ida, AR (71957)	2448
Mount Pleasant, AR (72561)	756
Mount Vernon, AR (72111)	1037
Mulberry, AR (72947)	3013
Murfreesboro, AR (71958)	1922
Nashville, AR (71852)	7728
Newark, AR (72562)	1606
New Blaine, AR (72851)	563
New Edinburg, AR (71660)	724
Newhope, AR (71959)	548
Newport, AR (72112)	6715
Norfork, AR (72658)	1305
Norman, AR (71960)	934
Maumelle, AR (72113)	17358
North Little Rock, AR (72114)	7696
North Little Rock, AR (72116)	18455
North Little Rock, AR (72117)	9170
North Little Rock, AR (72118)	17098
Sherwood, AR (72120)	26504
Oden, AR (71961)	663
Okolona, AR (71962)	579
Ola, AR (72853)	1503
Omaha, AR (72662)	2260
Osceola, AR (72370)	6230
Oxford, AR (72565)	629
Ozan, AR (71855)	541
Ozark, AR (72949)	7450
Ozone, AR (72854)	488
Palestine, AR (72372)	1514
Pangburn, AR (72121)	1997
Paragould, AR (72450)	26005
Paris, AR (72855)	4722
Parkin, AR (72373)	1006
Paron, AR (72122)	1064
Pearcy, AR (71964)	3052
Pea Ridge, AR (72751)	5039
Perry, AR (72125)	720
Perryville, AR (72126)	2801
Piggott, AR (72454)	3671
Pine Bluff, AR (71601)	10992
White Hall, AR (71602)	13392
Pine Bluff, AR (71603)	24782
Plainview, AR (72857)	1042
Pleasant Plains, AR (72568)	1466
Plumerville, AR (72127)	1693
Pocahontas, AR (72455)	9253
Poplar Grove, AR (72374)	555
Portland, AR (71663)	598
Pottsville, AR (72858)	2692
Poyen, AR (72128)	687
Prairie Grove, AR (72753)	6281
Prattsville, AR (72129)	1087
Prescott, AR (71857)	4526
Proctor, AR (72376)	1415
Quitman, AR (72131)	3435
Ratcliff, AR (72951)	850
Ravenden, AR (72459)	895
Ravenden Springs, AR (72460)	513
Rector, AR (72461)	2680
Redfield, AR (72132)	2653
Rison, AR (71665)	4608
Rogers, AR (72756)	28684
Rogers, AR (72758)	24907
Roland, AR (72135)	2284
Romance, AR (72136)	1344
Rose Bud, AR (72137)	1984
Rosston, AR (71858)	1223
Royal, AR (71968)	3473
Rudy, AR (72952)	2033
Russellville, AR (72801)	11097
Russellville, AR (72802)	15738
Saint Joe, AR (72675)	964
Salem, AR (72576)	2639
Scott, AR (72142)	2024
Scranton, AR (72863)	1321
Searcy, AR (72143)	23096
Sheridan, AR (72150)	9403
Fairfield Bay, AR (72088)	1802
Shirley, AR (72153)	1767
Sidney, AR (72577)	510
Siloam Springs, AR (72761)	15283
Smackover, AR (71762)	2167
Smithville, AR (72466)	915
Solgohachia, AR (72156)	508
Sparkman, AR (71763)	1244
Springdale, AR (72762)	25923
Springdale, AR (72764)	33654
Springfield, AR (72157)	1171
Stamps, AR (71860)	1880
Star City, AR (71667)	5926
Stephens, AR (71764)	1389
Strawberry, AR (72469)	710
Strong, AR (71765)	1796
Stuttgart, AR (72160)	8509
Subiaco, AR (72865)	944
Sulphur Rock, AR (72579)	1025
Sulphur Springs, AR (72768)	752
Summers, AR (72769)	707
Swifton, AR (72471)	736
Taylor, AR (71861)	1577
Thornton, AR (71766)	536
Tillar, AR (71670)	1068
Timbo, AR (72680)	560
Traskwood, AR (72167)	1270
Trumann, AR (72472)	6841
Tuckerman, AR (72473)	1892
Tumbling Shoals, AR (72581)	823
Turrell, AR (72384)	748
Tyronza, AR (72386)	1314
Valley Springs, AR (72682)	513
Van Buren, AR (72956)	24753
Vilonia, AR (72173)	7153
Viola, AR (72583)	1178
Waldo, AR (71770)	2374
Waldron, AR (72958)	5659
Walnut Ridge, AR (72476)	4969
Ward, AR (72176)	6082
Warren, AR (71671)	6351
Washington, AR (71862)	582
Watson, AR (71674)	501
Weiner, AR (72479)	1032
Wesley, AR (72773)	820
Western Grove, AR (72685)	1072
West Fork, AR (72774)	5051
West Helena, AR (72390)	6310
West Memphis, AR (72301)	18233
Wickes, AR (71973)	983
Williford, AR (72482)	751
Wilmar, AR (71675)	1458
Wilmot, AR (71676)	549
Wilson, AR (72395)	818
Winslow, AR (72959)	1990
Winthrop, AR (71866)	565
Wynne, AR (72396)	10384
Yellville, AR (72687)	4421
Ada, OK (74820)	21190
Adair, OK (74330)	2224
Afton, OK (74331)	4536
Agra, OK (74824)	998
Alex, OK (73002)	910
Allen, OK (74825)	1644
Altus, OK (73521)	15986
Alva, OK (73717)	4738
Amber, OK (73004)	743
Anadarko, OK (73005)	6595
Antlers, OK (74523)	4535
Apache, OK (73006)	2723
Arapaho, OK (73620)	854
Arcadia, OK (73007)	1561
Ardmore, OK (73401)	25460
Arkoma, OK (74901)	1344
Arnett, OK (73832)	815
Asher, OK (74826)	799
Atoka, OK (74525)	6690
Barnsdall, OK (74002)	1708
Bartlesville, OK (74003)	10345
Bartlesville, OK (74006)	21681
Beggs, OK (74421)	3511
Bennington, OK (74723)	1018
Bethany, OK (73008)	15228
Big Cabin, OK (74332)	1478
Billings, OK (74630)	473
Binger, OK (73009)	1039
Bixby, OK (74008)	17939
Blackwell, OK (74631)	5866
Blair, OK (73526)	1769
Blanchard, OK (73010)	13603
Bluejacket, OK (74333)	924
Bokchito, OK (74726)	1654
Bokoshe, OK (74930)	1291
Boswell, OK (74727)	1512
Boynton, OK (74422)	607
Braggs, OK (74423)	783
Braman, OK (74632)	486
Bristow, OK (74010)	7714
Broken Arrow, OK (74011)	21392
Broken Arrow, OK (74012)	46994
Broken Arrow, OK (74014)	28239
Broken Bow, OK (74728)	8178
Buffalo, OK (73834)	1280
Bunch, OK (74931)	924
Burneyville, OK (73430)	839
Byars, OK (74831)	655
Cache, OK (73527)	4010
Caddo, OK (74729)	2016
Calera, OK (74730)	2986
Calumet, OK (73014)	1165
Calvin, OK (74531)	733
Cameron, OK (74932)	1693
Canadian, OK (74425)	895
Caney, OK (74533)	669
Canton, OK (73724)	1017
Canute, OK (73626)	966
Carnegie, OK (73015)	2145
Carney, OK (74832)	702
Carter, OK (73627)	525
Cartwright, OK (74731)	959
Cashion, OK (73016)	1571
Castle, OK (74833)	525
Catoosa, OK (74015)	6830
Cement, OK (73017)	1294
Chandler, OK (74834)	5451
Chattanooga, OK (73528)	594
Checotah, OK (74426)	6847
Chelsea, OK (74016)	4495
Cherokee, OK (73728)	1586
Cheyenne, OK (73628)	1274
Chickasha, OK (73018)	13507
Choctaw, OK (73020)	17389
Chouteau, OK (74337)	3716
Claremore, OK (74017)	20237
Claremore, OK (74019)	13761
Clayton, OK (74536)	1360
Cleo Springs, OK (73729)	499
Cleveland, OK (74020)	5737
Clinton, OK (73601)	7947
Coalgate, OK (74538)	3041
Colbert, OK (74733)	2090
Colcord, OK (74338)	3362
Coleman, OK (73432)	771
Collinsville, OK (74021)	14673
Comanche, OK (73529)	3931
Commerce, OK (74339)	1846
Cookson, OK (74427)	1041
Copan, OK (74022)	1443
Cordell, OK (73632)	2780
Corn, OK (73024)	461
Council Hill, OK (74428)	733
Covington, OK (73730)	576
Coweta, OK (74429)	11363
Coyle, OK (73027)	794
Crescent, OK (73028)	2614
Cushing, OK (74023)	8416
Custer City, OK (73639)	533
Cyril, OK (73029)	1331
Davis, OK (73030)	3521
Delaware, OK (74027)	774
Depew, OK (74028)	1475
Dewey, OK (74029)	3960
Dill City, OK (73641)	595
Dover, OK (73734)	819
Drummond, OK (73735)	592
Drumright, OK (74030)	2944
Duke, OK (73532)	506
Duncan, OK (73533)	20968
Durant, OK (74701)	14011
Dustin, OK (74839)	617
Eagletown, OK (74734)	706
Earlsboro, OK (74840)	1447
Edmond, OK (73003)	19960
Edmond, OK (73012)	18114
Edmond, OK (73013)	34848
Edmond, OK (73025)	7984
Edmond, OK (73034)	29657
Elgin, OK (73538)	3789
Elk City, OK (73644)	10064
Elmore City, OK (73433)	1957
El Reno, OK (73036)	12754
Enid, OK (73701)	17867
Enid, OK (73703)	22729
Enid, OK (73705)	272
Erick, OK (73645)	1028
Eucha, OK (74342)	1287
Eufaula, OK (74432)	7227
Fairfax, OK (74637)	1324
Fairland, OK (74343)	2241
Fairview, OK (73737)	2900
Fargo, OK (73840)	504
Fletcher, OK (73541)	2328
Fort Cobb, OK (73038)	1410
Fort Gibson, OK (74434)	7080
Fort Towson, OK (74735)	1175
Foss, OK (73647)	595
Foster, OK (73434)	536
Frederick, OK (73542)	3357
Gage, OK (73843)	670
Gans, OK (74936)	835
Garber, OK (73738)	967
Garvin, OK (74736)	856
Geary, OK (73040)	1369
Geronimo, OK (73543)	1296
Glencoe, OK (74032)	1692
Glenpool, OK (74033)	8425
Gore, OK (74435)	2448
Gracemont, OK (73042)	758
Grandfield, OK (73546)	963
Granite, OK (73547)	961
Grove, OK (74344)	8992
Guthrie, OK (73044)	15668
Hammon, OK (73650)	750
Harrah, OK (73045)	8525
Hartshorne, OK (74547)	2670
Haskell, OK (74436)	3861
Haworth, OK (74740)	1661
Healdton, OK (73438)	2536
Heavener, OK (74937)	4030
Helena, OK (73741)	520
Hendrix, OK (74741)	589
Hennessey, OK (73742)	2942
Henryetta, OK (74437)	6920
Hinton, OK (73047)	2424
Hobart, OK (73651)	3219
Hodgen, OK (74939)	516
Holdenville, OK (74848)	4902
Hollis, OK (73550)	1754
Hominy, OK (74035)	2617
Howe, OK (74940)	1680
Hugo, OK (74743)	5969
Hulbert, OK (74441)	3604
Hydro, OK (73048)	1705
Idabel, OK (74745)	6927
Indiahoma, OK (73552)	984
Indianola, OK (74442)	627
Inola, OK (74036)	5500
Jay, OK (74346)	5658
Jenks, OK (74037)	13004
Jennings, OK (74038)	1555
Jones, OK (73049)	4711
Kansas, OK (74347)	2387
Kaw City, OK (74641)	563
Kellyville, OK (74039)	3134
Keota, OK (74941)	1881
Kiefer, OK (74041)	1801
Kingfisher, OK (73750)	5662
Kingston, OK (73439)	5032
Kinta, OK (74552)	733
Kiowa, OK (74553)	1166
Konawa, OK (74849)	2341
Lahoma, OK (73754)	908
Lamont, OK (74643)	487
Lane, OK (74555)	706
Laverne, OK (73848)	1812
Lawton, OK (73501)	12242
Fort Sill, OK (73503)	4679
Lawton, OK (73505)	37053
Lawton, OK (73507)	16887
Leedey, OK (73654)	722
Lexington, OK (73051)	5286
Lindsay, OK (73052)	4807
Locust Grove, OK (74352)	5115
Lone Grove, OK (73443)	3389
Lone Wolf, OK (73655)	660
Longdale, OK (73755)	590
Lookeba, OK (73053)	611
Luther, OK (73054)	2975
Mcalester, OK (74501)	18926
Mccurtain, OK (74944)	814
Mcloud, OK (74851)	6783
Macomb, OK (74852)	1127
Madill, OK (73446)	5746
Mangum, OK (73554)	2614
Mannford, OK (74044)	5917
Mannsville, OK (73447)	746
Marietta, OK (73448)	4503
Marlow, OK (73055)	7702
Maud, OK (74854)	1416
Maysville, OK (73057)	1868
Mead, OK (73449)	1872
Medford, OK (73759)	1182
Meeker, OK (74855)	3552
Miami, OK (74354)	12817
Milburn, OK (73450)	892
Mill Creek, OK (74856)	616
Minco, OK (73059)	2247
Mooreland, OK (73852)	1737
Morris, OK (74445)	2441
Morrison, OK (73061)	1261
Mounds, OK (74047)	5170
Mountain View, OK (73062)	997
Muldrow, OK (74948)	8651
Mulhall, OK (73063)	578
Muskogee, OK (74401)	11484
Muskogee, OK (74403)	22068
Mustang, OK (73064)	17621
Newalla, OK (74857)	7419
Newcastle, OK (73065)	5751
Newkirk, OK (74647)	2921
Ninnekah, OK (73067)	1452
Noble, OK (73068)	9027
Norman, OK (73026)	8992
Norman, OK (73069)	16046
Norman, OK (73071)	24595
Norman, OK (73072)	28507
Nowata, OK (74048)	4533
Ochelata, OK (74051)	1531
Okarche, OK (73762)	1912
Okeene, OK (73763)	1351
Okemah, OK (74859)	4398
Oklahoma City, OK (73102)	1223
Oklahoma City, OK (73103)	3022
Oklahoma City, OK (73104)	1097
Oklahoma City, OK (73105)	3696
Oklahoma City, OK (73106)	6978
Oklahoma City, OK (73107)	17528
Oklahoma City, OK (73108)	8381
Oklahoma City, OK (73109)	12156
Oklahoma City, OK (73110)	24724
Oklahoma City, OK (73111)	7764
Oklahoma City, OK (73112)	22723
Oklahoma City, OK (73114)	11331
Oklahoma City, OK (73115)	16007
Oklahoma City, OK (73116)	8099
Oklahoma City, OK (73117)	3317
Oklahoma City, OK (73118)	10029
Oklahoma City, OK (73119)	18877
Oklahoma City, OK (73120)	27488
Oklahoma City, OK (73121)	2357
Oklahoma City, OK (73122)	9820
Oklahoma City, OK (73127)	16121
Oklahoma City, OK (73128)	3233
Oklahoma City, OK (73129)	11757
Oklahoma City, OK (73130)	16236
Oklahoma City, OK (73131)	2019
Oklahoma City, OK (73132)	20472
Oklahoma City, OK (73134)	3231
Oklahoma City, OK (73135)	15777
Oklahoma City, OK (73139)	12451
Oklahoma City, OK (73141)	1973
Oklahoma City, OK (73142)	8414
Oklahoma City, OK (73145)	2332
Oklahoma City, OK (73149)	3179
Oklahoma City, OK (73150)	4025
Oklahoma City, OK (73151)	1259
Oklahoma City, OK (73159)	23273
Oklahoma City, OK (73160)	41857
Oklahoma City, OK (73162)	23333
Oklahoma City, OK (73165)	5059
Oklahoma City, OK (73169)	1395
Oklahoma City, OK (73170)	29722
Oklahoma City, OK (73173)	975
Oklahoma City, OK (73179)	2518
Okmulgee, OK (74447)	11899
Oktaha, OK (74450)	1454
Olustee, OK (73560)	560
Oologah, OK (74053)	3881
Orlando, OK (73073)	485
Overbrook, OK (73453)	536
Owasso, OK (74055)	32540
Paden, OK (74860)	1171
Paoli, OK (73074)	922
Park Hill, OK (74451)	3076
Pauls Valley, OK (73075)	7364
Pawhuska, OK (74056)	4176
Pawnee, OK (74058)	3148
Peggs, OK (74452)	521
Perkins, OK (74059)	4278
Perry, OK (73077)	5616
Piedmont, OK (73078)	6620
Pittsburg, OK (74560)	489
Pocasset, OK (73079)	531
Pocola, OK (74902)	3395
Ponca City, OK (74601)	14904
Ponca City, OK (74604)	10433
Pond Creek, OK (73766)	881
Porter, OK (74454)	2227
Porum, OK (74455)	2075
Poteau, OK (74953)	8890
Prague, OK (74864)	3896
Prue, OK (74060)	473
Pryor, OK (74361)	10972
Purcell, OK (73080)	7043
Quapaw, OK (74363)	2199
Quinton, OK (74561)	1754
Ralston, OK (74650)	511
Ramona, OK (74061)	1622
Randlett, OK (73562)	565
Ratliff City, OK (73481)	699
Rattan, OK (74562)	745
Red Oak, OK (74563)	1457
Red Rock, OK (74651)	543
Ringling, OK (73456)	1646
Ringwood, OK (73768)	1314
Ripley, OK (74062)	854
Roff, OK (74865)	1290
Roland, OK (74954)	3856
Rose, OK (74364)	1184
Rush Springs, OK (73082)	2304
Ryan, OK (73565)	700
Salina, OK (74365)	3523
Sallisaw, OK (74955)	11017
Sand Springs, OK (74063)	24032
Sapulpa, OK (74066)	23165
Sasakwa, OK (74867)	749
Sawyer, OK (74756)	615
Sayre, OK (73662)	3312
Seiling, OK (73663)	1058
Seminole, OK (74868)	8261
Sentinel, OK (73664)	924
Shady Point, OK (74956)	1423
Sharon, OK (73857)	550
Shattuck, OK (73858)	1326
Shawnee, OK (74801)	15507
Shawnee, OK (74804)	14183
Shidler, OK (74652)	660
Skiatook, OK (74070)	10987
Smithville, OK (74957)	799
Snyder, OK (73566)	1228
Soper, OK (74759)	947
S Coffeyville, OK (74072)	1527
Sparks, OK (74869)	565
Spavinaw, OK (74366)	964
Spencer, OK (73084)	4808
Sperry, OK (74073)	4211
Spiro, OK (74959)	4769
Springer, OK (73458)	822
Stigler, OK (74462)	5523
Stillwater, OK (74074)	17421
Stillwater, OK (74075)	13869
Stilwell, OK (74960)	9727
Stonewall, OK (74871)	1773
Stratford, OK (74872)	2688
Stringtown, OK (74569)	604
Stroud, OK (74079)	3345
Stuart, OK (74570)	1020
Sulphur, OK (73086)	6006
Tahlequah, OK (74464)	18061
Talala, OK (74080)	1999
Talihina, OK (74571)	2719
Taloga, OK (73667)	492
Tecumseh, OK (74873)	8774
Temple, OK (73568)	849
Terlton, OK (74081)	1281
Thackerville, OK (73459)	921
Thomas, OK (73669)	1336
Tipton, OK (73570)	885
Tishomingo, OK (73460)	3104
Tonkawa, OK (74653)	2678
Tryon, OK (74875)	802
Tulsa, OK (74103)	601
Tulsa, OK (74104)	7758
Tulsa, OK (74105)	21371
Tulsa, OK (74106)	10725
Tulsa, OK (74107)	13560
Tulsa, OK (74108)	5343
Tulsa, OK (74110)	9421
Tulsa, OK (74112)	15769
Tulsa, OK (74114)	13112
Tulsa, OK (74115)	16053
Tulsa, OK (74116)	2705
Tulsa, OK (74119)	2507
Tulsa, OK (74120)	3365
Tulsa, OK (74126)	6893
Tulsa, OK (74127)	11851
Tulsa, OK (74128)	9443
Tulsa, OK (74129)	14314
Tulsa, OK (74130)	1565
Tulsa, OK (74131)	2219
Tulsa, OK (74132)	6194
Tulsa, OK (74133)	35841
Tulsa, OK (74134)	12903
Tulsa, OK (74135)	16478
Tulsa, OK (74136)	21732
Tulsa, OK (74137)	22445
Tulsa, OK (74145)	14324
Tulsa, OK (74146)	10432
Tupelo, OK (74572)	577
Tuskahoma, OK (74574)	633
Tuttle, OK (73089)	9398
Union City, OK (73090)	766
Valliant, OK (74764)	2620
Verden, OK (73092)	676
Vian, OK (74962)	3500
Vici, OK (73859)	1169
Vinita, OK (74301)	8049
Wagoner, OK (74467)	9975
Walters, OK (73572)	2861
Wanette, OK (74878)	1173
Wann, OK (74083)	935
Wapanucka, OK (73461)	591
Warner, OK (74469)	2001
Washington, OK (73093)	2233
Watonga, OK (73772)	3227
Watts, OK (74964)	1929
Waukomis, OK (73773)	1414
Waurika, OK (73573)	1710
Wayne, OK (73095)	1383
Waynoka, OK (73860)	1060
Weatherford, OK (73096)	9002
Webbers Falls, OK (74470)	1223
Welch, OK (74369)	1411
Weleetka, OK (74880)	1405
Welling, OK (74471)	1117
Wellston, OK (74881)	3561
Westville, OK (74965)	3821
Wetumka, OK (74883)	1789
Wewoka, OK (74884)	4132
Wilburton, OK (74578)	4683
Wilson, OK (73463)	2463
Wister, OK (74966)	2772
Woodward, OK (73801)	11387
Wright City, OK (74766)	1140
Wyandotte, OK (74370)	2544
Wynnewood, OK (73098)	3200
Wynona, OK (74084)	457
Yale, OK (74085)	1871
Yukon, OK (73099)	47159
Texarkana, AR (71854)	26511
Addison, TX (75001)	10245
Alba, TX (75410)	3155
Allen, TX (75002)	52358
Allen, TX (75013)	25569
Alto, TX (75925)	2883
Anna, TX (75409)	8989
Annona, TX (75550)	653
Apple Springs, TX (75926)	837
Arp, TX (75750)	2997
Arthur City, TX (75411)	789
Athens, TX (75751)	12645
Athens, TX (75752)	4740
Atlanta, TX (75551)	8581
Avery, TX (75554)	1352
Avinger, TX (75630)	1925
Bagwell, TX (75412)	560
Barry, TX (75102)	1127
Beckville, TX (75631)	2113
Bells, TX (75414)	2529
Ben Wheeler, TX (75754)	4452
Big Sandy, TX (75755)	4025
Bivins, TX (75555)	1121
Bloomburg, TX (75556)	1032
Blossom, TX (75416)	2328
Blue Ridge, TX (75424)	2644
Bogata, TX (75417)	1849
Bonham, TX (75418)	8815
Bon Wier, TX (75928)	970
Brashear, TX (75420)	859
Broaddus, TX (75929)	1152
Bronson, TX (75930)	1355
Brookeland, TX (75931)	1667
Brookston, TX (75421)	819
Brownsboro, TX (75756)	3036
Buffalo, TX (75831)	3994
Bullard, TX (75757)	8076
Burkeville, TX (75932)	1156
Caddo Mills, TX (75135)	4860
Call, TX (75933)	1153
Campbell, TX (75422)	2180
Canton, TX (75103)	10257
Carrollton, TX (75006)	38972
Carrollton, TX (75007)	45464
Carrollton, TX (75010)	17158
Carthage, TX (75633)	11621
Cedar Hill, TX (75104)	34793
Celeste, TX (75423)	2133
Celina, TX (75009)	6696
Center, TX (75935)	10254
Centerville, TX (75833)	2625
Chandler, TX (75758)	7626
Chester, TX (75936)	700
Chireno, TX (75937)	891
Clarksville, TX (75426)	4099
Colmesneil, TX (75938)	1951
Commerce, TX (75428)	5552
Como, TX (75431)	1575
Cookville, TX (75558)	1170
Cooper, TX (75432)	2477
Coppell, TX (75019)	34805
Corrigan, TX (75939)	3000
Corsicana, TX (75109)	3006
Corsicana, TX (75110)	20700
Crandall, TX (75114)	4240
Crockett, TX (75835)	8678
Cumby, TX (75433)	2104
Cushing, TX (75760)	1897
Daingerfield, TX (75638)	4395
Dallas, TX (75201)	6709
Dallas, TX (75202)	1319
Dallas, TX (75203)	9969
Dallas, TX (75204)	17571
Dallas, TX (75205)	16637
Dallas, TX (75206)	24726
Dallas, TX (75207)	628
Dallas, TX (75208)	23585
Dallas, TX (75209)	11199
Dallas, TX (75210)	4212
Dallas, TX (75211)	51878
Dallas, TX (75212)	17516
Dallas, TX (75214)	25594
Dallas, TX (75215)	9775
Dallas, TX (75216)	35009
Dallas, TX (75217)	57055
Dallas, TX (75218)	18331
Dallas, TX (75219)	17375
Dallas, TX (75220)	26442
Dallas, TX (75223)	10554
Dallas, TX (75224)	23717
Dallas, TX (75225)	19408
Dallas, TX (75226)	2024
Dallas, TX (75227)	38936
Dallas, TX (75228)	46796
Dallas, TX (75229)	27098
Dallas, TX (75230)	22222
Dallas, TX (75231)	23801
Dallas, TX (75232)	22153
Dallas, TX (75233)	9692
Dallas, TX (75234)	23496
Dallas, TX (75235)	12286
Dallas, TX (75236)	10605
Dallas, TX (75237)	11191
Dallas, TX (75238)	22550
Dallas, TX (75240)	16733
Dallas, TX (75241)	20746
Dallas, TX (75243)	40571
Dallas, TX (75244)	10600
Dallas, TX (75246)	1699
Dallas, TX (75247)	695
Dallas, TX (75248)	29004
Dallas, TX (75249)	10491
Dallas, TX (75251)	2005
Dallas, TX (75252)	31444
Dallas, TX (75253)	11448
Dallas, TX (75254)	16309
Dallas, TX (75287)	37474
De Berry, TX (75639)	2199
De Kalb, TX (75559)	4729
Denison, TX (75020)	16525
Denison, TX (75021)	6825
Deport, TX (75435)	809
Desoto, TX (75115)	37234
Detroit, TX (75436)	1565
Diana, TX (75640)	3640
Diboll, TX (75941)	6251
Dike, TX (75437)	870
Dodd City, TX (75438)	884
Donie, TX (75838)	553
Douglass, TX (75943)	1057
Douglassville, TX (75560)	868
Duncanville, TX (75116)	14846
Duncanville, TX (75137)	15292
Ector, TX (75439)	712
Edgewood, TX (75117)	3168
Elkhart, TX (75839)	3985
Emory, TX (75440)	4831
Ennis, TX (75119)	19581
Etoile, TX (75944)	973
Eustace, TX (75124)	3381
Fairfield, TX (75840)	6135
Farmersville, TX (75442)	6640
Ferris, TX (75125)	5213
Flint, TX (75762)	10335
Forney, TX (75126)	27433
Frankston, TX (75763)	4500
Frisco, TX (75034)	56797
Frisco, TX (75035)	37957
Fruitvale, TX (75127)	1280
Garland, TX (75040)	47500
Garland, TX (75041)	21729
Garland, TX (75042)	28686
Garland, TX (75043)	45476
Garland, TX (75044)	33925
Sachse, TX (75048)	17231
Garrison, TX (75946)	2671
Gary, TX (75643)	1511
Gilmer, TX (75644)	9164
Gilmer, TX (75645)	6939
Gladewater, TX (75647)	10306
Grand Prairie, TX (75050)	29564
Grand Prairie, TX (75051)	26275
Grand Prairie, TX (75052)	68943
Grand Prairie, TX (75054)	6470
Grand Saline, TX (75140)	5154
Grapeland, TX (75844)	3985
Greenville, TX (75401)	12689
Greenville, TX (75402)	12797
Groveton, TX (75845)	2052
Gunter, TX (75058)	2365
Hallsville, TX (75650)	7338
Harleton, TX (75651)	1805
Hawkins, TX (75765)	5686
Hemphill, TX (75948)	4448
Henderson, TX (75652)	9772
Henderson, TX (75654)	8599
Honey Grove, TX (75446)	2450
Hooks, TX (75561)	4560
Howe, TX (75459)	3541
Hughes Springs, TX (75656)	3808
Huntington, TX (75949)	6041
Hutchins, TX (75141)	2477
Irving, TX (75038)	21643
Irving, TX (75039)	8231
Irving, TX (75060)	35350
Irving, TX (75061)	37493
Irving, TX (75062)	34919
Irving, TX (75063)	27912
Ivanhoe, TX (75447)	884
Jacksonville, TX (75766)	19553
Jasper, TX (75951)	12076
Jefferson, TX (75657)	6324
Jewett, TX (75846)	2080
Joaquin, TX (75954)	2580
Karnack, TX (75661)	1850
Kaufman, TX (75142)	14878
Kemp, TX (75143)	10584
Kennard, TX (75847)	1157
Kerens, TX (75144)	2401
Kilgore, TX (75662)	18305
Kirbyville, TX (75956)	5630
Klondike, TX (75448)	517
Ladonia, TX (75449)	804
Lake Dallas, TX (75065)	8944
Lancaster, TX (75134)	14114
Lancaster, TX (75146)	14595
Laneville, TX (75667)	836
Larue, TX (75770)	1923
Lavon, TX (75166)	2639
Leesburg, TX (75451)	1019
Leona, TX (75850)	490
Leonard, TX (75452)	3272
Flower Mound, TX (75022)	19102
Flower Mound, TX (75028)	37370
The Colony, TX (75056)	39340
Lewisville, TX (75057)	9111
Lewisville, TX (75067)	46631
Lewisville, TX (75077)	31384
Lindale, TX (75771)	15254
Linden, TX (75563)	3260
Little Elm, TX (75068)	27083
Lone Oak, TX (75453)	2561
Lone Star, TX (75668)	1609
Longview, TX (75601)	11160
Longview, TX (75602)	16228
Longview, TX (75603)	4300
Longview, TX (75604)	23252
Longview, TX (75605)	22001
Lovelady, TX (75851)	1929
Lufkin, TX (75901)	21057
Lufkin, TX (75904)	24382
Mckinney, TX (75069)	24848
Mckinney, TX (75070)	62107
Mckinney, TX (75071)	26404
Mabank, TX (75147)	5874
Mabank, TX (75156)	9798
Malakoff, TX (75148)	4306
Marietta, TX (75566)	574
Marshall, TX (75670)	12124
Marshall, TX (75672)	12545
Maud, TX (75567)	2742
Melissa, TX (75454)	4660
Mesquite, TX (75149)	42329
Mesquite, TX (75150)	44465
Balch Springs, TX (75180)	16065
Mesquite, TX (75181)	20191
Sunnyvale, TX (75182)	4453
Midway, TX (75852)	1228
Milam, TX (75959)	704
Mineola, TX (75773)	9514
Montalba, TX (75853)	800
Moscow, TX (75960)	717
Mount Enterprise, TX (75681)	1983
Mount Pleasant, TX (75455)	19644
Mount Vernon, TX (75457)	5083
Murchison, TX (75778)	2311
Nacogdoches, TX (75961)	9752
Nacogdoches, TX (75964)	12932
Nacogdoches, TX (75965)	11180
Naples, TX (75568)	2275
Nash, TX (75569)	2633
Nevada, TX (75173)	3214
New Boston, TX (75570)	7239
Newton, TX (75966)	3399
Oakwood, TX (75855)	1826
Omaha, TX (75571)	2251
Ore City, TX (75683)	2993
Overton, TX (75684)	4413
Palestine, TX (75801)	12410
Palestine, TX (75803)	10803
Palmer, TX (75152)	3840
Paris, TX (75460)	16369
Paris, TX (75462)	9070
Pattonville, TX (75468)	824
Pickton, TX (75471)	1040
Pineland, TX (75968)	1395
Pittsburg, TX (75686)	9817
Plano, TX (75023)	38880
Plano, TX (75024)	28881
Plano, TX (75025)	44329
Plano, TX (75074)	34130
Plano, TX (75075)	28631
Plano, TX (75093)	41091
Plano, TX (75094)	17008
Point, TX (75472)	2577
Pollok, TX (75969)	2877
Pottsboro, TX (75076)	6215
Powderly, TX (75473)	2917
Powell, TX (75153)	532
Princeton, TX (75407)	10680
Prosper, TX (75078)	8122
Queen City, TX (75572)	3007
Quinlan, TX (75474)	11328
Quitman, TX (75783)	5587
Ravenna, TX (75476)	1014
Red Oak, TX (75154)	29234
Reklaw, TX (75784)	573
Rice, TX (75155)	1791
Richardson, TX (75080)	33743
Richardson, TX (75081)	28009
Richardson, TX (75082)	18327
Rockwall, TX (75032)	22243
Rockwall, TX (75087)	24094
Rowlett, TX (75088)	21538
Rowlett, TX (75089)	24865
Roxton, TX (75477)	712
Royse City, TX (75189)	17170
Rusk, TX (75785)	6710
Saltillo, TX (75478)	710
San Augustine, TX (75972)	4840
Savoy, TX (75479)	1341
Scroggins, TX (75480)	1193
Scurry, TX (75158)	3605
Seagoville, TX (75159)	12440
Shelbyville, TX (75973)	2013
Sherman, TX (75090)	16524
Sherman, TX (75092)	16908
Simms, TX (75574)	1373
Streetman, TX (75859)	1496
Sulphur Springs, TX (75482)	18078
Sumner, TX (75486)	2011
Talco, TX (75487)	1187
Tatum, TX (75691)	3373
Teague, TX (75860)	4474
Telephone, TX (75488)	811
Tenaha, TX (75974)	2209
Tennessee Colony, TX (75861)	1444
Terrell, TX (75160)	18524
Terrell, TX (75161)	4554
Texarkana, TX (75501)	25835
Texarkana, TX (75503)	19203
Timpson, TX (75975)	2626
Trenton, TX (75490)	1893
Trinidad, TX (75163)	1818
Trinity, TX (75862)	7041
Troup, TX (75789)	5835
Tyler, TX (75701)	23667
Tyler, TX (75702)	18031
Tyler, TX (75703)	29088
Tyler, TX (75704)	6269
Tyler, TX (75705)	1626
Tyler, TX (75706)	6329
Tyler, TX (75707)	11033
Tyler, TX (75708)	5193
Tyler, TX (75709)	3793
Van, TX (75790)	3609
Van Alstyne, TX (75495)	5941
Waskom, TX (75692)	4146
Waxahachie, TX (75165)	28462
Waxahachie, TX (75167)	6301
Whitehouse, TX (75791)	11115
White Oak, TX (75693)	5783
Whitewright, TX (75491)	3650
Wiergate, TX (75977)	473
Wills Point, TX (75169)	11143
Wilmer, TX (75172)	2688
Winnsboro, TX (75494)	8079
Winona, TX (75792)	2649
Wolfe City, TX (75496)	2404
Woodville, TX (75979)	6167
Wylie, TX (75098)	39240
Yantis, TX (75497)	2533
Zavalla, TX (75980)	1952
Beaver, OK (73932)	1800
Boise City, OK (73933)	1404
Forgan, OK (73938)	621
Goodwell, OK (73939)	894
Guymon, OK (73942)	11623
Hooker, OK (73945)	2236
Texhoma, OK (73949)	1353
Turpin, OK (73950)	1301
Tyrone, OK (73951)	852
Abernathy, TX (79311)	2722
Abilene, TX (79601)	12905
Abilene, TX (79602)	16963
Abilene, TX (79603)	17967
Abilene, TX (79605)	23294
Abilene, TX (79606)	18819
Dyess Afb, TX (79607)	2155
Albany, TX (76430)	2126
Aledo, TX (76008)	12051
Alvarado, TX (76009)	15597
Alvord, TX (76225)	2633
Amarillo, TX (79101)	1856
Amarillo, TX (79102)	7378
Amarillo, TX (79103)	8335
Amarillo, TX (79104)	5717
Amarillo, TX (79106)	20692
Amarillo, TX (79107)	23567
Amarillo, TX (79108)	9863
Amarillo, TX (79109)	35471
Amarillo, TX (79110)	15253
Amarillo, TX (79111)	1076
Amarillo, TX (79118)	15106
Amarillo, TX (79119)	9333
Amarillo, TX (79121)	5595
Amarillo, TX (79124)	6480
Amherst, TX (79312)	737
Anson, TX (79501)	2775
Anton, TX (79313)	1332
Argyle, TX (76226)	14869
Arlington, TX (76001)	24832
Arlington, TX (76002)	24144
Arlington, TX (76006)	17960
Arlington, TX (76010)	35107
Arlington, TX (76011)	15138
Arlington, TX (76012)	21302
Arlington, TX (76013)	23891
Arlington, TX (76014)	25456
Arlington, TX (76015)	13738
Arlington, TX (76016)	27269
Arlington, TX (76017)	37503
Arlington, TX (76018)	22133
Aspermont, TX (79502)	1041
Aubrey, TX (76227)	17657
Azle, TX (76020)	21085
Baird, TX (79504)	2136
Ballinger, TX (76821)	3822
Bangs, TX (76823)	2397
Bedford, TX (76021)	29082
Bedford, TX (76022)	11172
Bellevue, TX (76228)	870
Big Lake, TX (76932)	2780
Blackwell, TX (79506)	555
Blanket, TX (76432)	1053
Bluff Dale, TX (76433)	1042
Booker, TX (79005)	1336
Borger, TX (79007)	11067
Bovina, TX (79009)	1683
Bowie, TX (76230)	7829
Boyd, TX (76023)	4825
Brady, TX (76825)	5569
Breckenridge, TX (76424)	6630
Bridgeport, TX (76426)	8886
Bronte, TX (76933)	1019
Brownfield, TX (79316)	7900
Brownwood, TX (76801)	17792
Early, TX (76802)	3844
Bryson, TX (76427)	649
Buffalo Gap, TX (79508)	1070
Burkburnett, TX (76354)	9416
Burleson, TX (76028)	48315
Byers, TX (76357)	618
Canadian, TX (79014)	3184
Canyon, TX (79015)	13932
Carbon, TX (76435)	459
Carlsbad, TX (76934)	818
Cherokee, TX (76832)	472
Chico, TX (76431)	2799
Childress, TX (79201)	4543
Chillicothe, TX (79225)	791
Christoval, TX (76935)	1312
Cisco, TX (76437)	4086
Clarendon, TX (79226)	2424
Claude, TX (79019)	1486
Cleburne, TX (76031)	12902
Cleburne, TX (76033)	20205
Clyde, TX (79510)	6374
Coahoma, TX (79511)	1210
Coleman, TX (76834)	4592
Colleyville, TX (76034)	21596
Collinsville, TX (76233)	2545
Colorado City, TX (79512)	4467
Comanche, TX (76442)	5782
Cresson, TX (76035)	1342
Crosbyton, TX (79322)	1489
Cross Plains, TX (76443)	1547
Crowell, TX (79227)	1049
Crowley, TX (76036)	17863
Dalhart, TX (79022)	7294
Decatur, TX (76234)	12732
De Leon, TX (76444)	2819
Denton, TX (76201)	11718
Denton, TX (76205)	11567
Denton, TX (76207)	8326
Denton, TX (76208)	14705
Denton, TX (76209)	17982
Denton, TX (76210)	31092
Denver City, TX (79323)	5140
Dimmitt, TX (79027)	3692
Dublin, TX (76446)	6184
Dumas, TX (79029)	12948
Earth, TX (79031)	983
Eastland, TX (76448)	4478
Eden, TX (76837)	1126
Eldorado, TX (76936)	2428
Electra, TX (76360)	2621
Era, TX (76238)	474
Euless, TX (76039)	27541
Euless, TX (76040)	21105
Farwell, TX (79325)	1790
Floydada, TX (79235)	3085
Follett, TX (79034)	546
Forestburg, TX (76239)	827
Fort Worth, TX (76102)	5056
Fort Worth, TX (76103)	10569
Fort Worth, TX (76104)	10534
Fort Worth, TX (76105)	15667
Fort Worth, TX (76106)	25237
Fort Worth, TX (76107)	20065
Fort Worth, TX (76108)	30105
Fort Worth, TX (76109)	15610
Fort Worth, TX (76110)	22691
Fort Worth, TX (76111)	16282
Fort Worth, TX (76112)	28685
Fort Worth, TX (76114)	18683
Fort Worth, TX (76115)	14316
Fort Worth, TX (76116)	33677
Haltom City, TX (76117)	23044
Fort Worth, TX (76118)	11257
Fort Worth, TX (76119)	28696
Fort Worth, TX (76120)	11369
Fort Worth, TX (76123)	23351
Fort Worth, TX (76126)	17198
Naval Air Station/ Jrb, TX (76127)	405
Fort Worth, TX (76131)	21447
Fort Worth, TX (76132)	18830
Fort Worth, TX (76133)	38798
Fort Worth, TX (76134)	18029
Fort Worth, TX (76135)	15235
Fort Worth, TX (76137)	43623
Fort Worth, TX (76140)	19696
Fort Worth, TX (76148)	20030
Fort Worth, TX (76155)	2759
Fort Worth, TX (76164)	11869
Fort Worth, TX (76177)	4053
Fort Worth, TX (76179)	38294
North Richland Hills, TX (76180)	48925
North Richland Hills, TX (76182)	2524
Friona, TX (79035)	4213
Fritch, TX (79036)	4126
Gainesville, TX (76240)	19357
Glen Rose, TX (76043)	5562
Godley, TX (76044)	3235
Goldthwaite, TX (76844)	2732
Gordon, TX (76453)	862
Gordonville, TX (76245)	1406
Gorman, TX (76454)	1278
Graford, TX (76449)	1754
Graham, TX (76450)	10991
Granbury, TX (76048)	17420
Granbury, TX (76049)	21247
Grandview, TX (76050)	5165
Grapevine, TX (76051)	38324
Southlake, TX (76092)	24319
Groom, TX (79039)	646
Gruver, TX (79040)	1479
Gustine, TX (76455)	750
Hale Center, TX (79041)	2371
Hamlin, TX (79520)	1873
Happy, TX (79042)	926
Hart, TX (79043)	1136
Hartley, TX (79044)	659
Haskell, TX (79521)	2731
Haslet, TX (76052)	11906
Hawley, TX (79525)	2474
Henrietta, TX (76365)	4031
Hereford, TX (79045)	15188
Hermleigh, TX (79526)	780
Hico, TX (76457)	2954
Holliday, TX (76366)	1874
Hurst, TX (76053)	22454
Hurst, TX (76054)	11288
Idalou, TX (79329)	2789
Iowa Park, TX (76367)	8092
Itasca, TX (76055)	2157
Jacksboro, TX (76458)	4174
Jayton, TX (79528)	471
Joshua, TX (76058)	13674
Junction, TX (76849)	3164
Justin, TX (76247)	10412
Keene, TX (76059)	3540
Keller, TX (76244)	5891
Keller, TX (76248)	70353
Kennedale, TX (76060)	5925
Knox City, TX (79529)	1032
Kress, TX (79052)	1039
Krum, TX (76249)	6107
Lamesa, TX (79331)	8722
Lawn, TX (79530)	484
Levelland, TX (79336)	12753
Lindsay, TX (76250)	1081
Lipan, TX (76462)	2196
Littlefield, TX (79339)	5605
Lockney, TX (79241)	2012
Lometa, TX (76853)	1146
Loraine, TX (79532)	672
Lorenzo, TX (79343)	1176
Lubbock, TX (79401)	2679
Lubbock, TX (79403)	11588
Lubbock, TX (79404)	7097
Lubbock, TX (79407)	12997
Lubbock, TX (79410)	5659
Lubbock, TX (79411)	4878
Lubbock, TX (79412)	10865
Lubbock, TX (79413)	16176
Lubbock, TX (79414)	12106
Lubbock, TX (79415)	11193
Lubbock, TX (79416)	21806
Lubbock, TX (79423)	26325
Lubbock, TX (79424)	32403
Mclean, TX (79057)	957
Mansfield, TX (76063)	50138
Mason, TX (76856)	2950
Matador, TX (79244)	588
May, TX (76857)	1298
Maypearl, TX (76064)	1638
Meadow, TX (79345)	743
Memphis, TX (79245)	1853
Menard, TX (76859)	1590
Merkel, TX (79536)	4189
Mertzon, TX (76941)	1174
Miami, TX (79059)	671
Midlothian, TX (76065)	24588
Miles, TX (76861)	1637
Millsap, TX (76066)	2481
Mineral Wells, TX (76067)	14701
Montague, TX (76251)	632
Morton, TX (79346)	1895
Muenster, TX (76252)	2474
Muleshoe, TX (79347)	5353
Mullin, TX (76864)	553
Munday, TX (76371)	1262
Nazareth, TX (79063)	615
Newark, TX (76071)	2590
Newcastle, TX (76372)	722
Nocona, TX (76255)	4295
Odonnell, TX (79351)	1076
Olney, TX (76374)	3356
Olton, TX (79064)	2019
Ovalo, TX (79541)	618
Ozona, TX (76943)	3170
Paducah, TX (79248)	1199
Palo Pinto, TX (76484)	792
Pampa, TX (79065)	15161
Panhandle, TX (79068)	2569
Paradise, TX (76073)	4309
Perrin, TX (76486)	1013
Perryton, TX (79070)	8013
Petersburg, TX (79250)	1195
Petrolia, TX (76377)	670
Pilot Point, TX (76258)	5348
Plains, TX (79355)	1571
Plainview, TX (79072)	19711
Ponder, TX (76259)	3675
Poolville, TX (76487)	1954
Post, TX (79356)	3405
Quanah, TX (79252)	2331
Rainbow, TX (76077)	501
Ralls, TX (79357)	1832
Ranger, TX (76470)	2140
Rhome, TX (76078)	6476
Richland Springs, TX (76871)	589
Rio Vista, TX (76093)	1880
Rising Star, TX (76471)	1221
Roanoke, TX (76262)	22173
Robert Lee, TX (76945)	1366
Roby, TX (79543)	913
Rochelle, TX (76872)	541
Ropesville, TX (79358)	998
Roscoe, TX (79545)	1459
Rotan, TX (79546)	1496
Rowena, TX (76875)	565
Rule, TX (79547)	625
Sadler, TX (76264)	1199
Saint Jo, TX (76265)	1483
San Angelo, TX (76901)	21943
San Angelo, TX (76903)	23126
San Angelo, TX (76904)	24239
San Angelo, TX (76905)	8976
Goodfellow Afb, TX (76908)	756
Sanger, TX (76266)	10870
San Saba, TX (76877)	3184
Santa Anna, TX (76878)	1252
Santo, TX (76472)	1269
Seagraves, TX (79359)	2208
Seminole, TX (79360)	9747
Seymour, TX (76380)	2908
Shallowater, TX (79363)	4452
Shamrock, TX (79079)	2158
Silverton, TX (79257)	891
Skellytown, TX (79080)	471
Slaton, TX (79364)	6286
Ransom Canyon, TX (79366)	1002
Snyder, TX (79549)	10249
Sonora, TX (76950)	3770
Spearman, TX (79081)	3077
Springtown, TX (76082)	14207
Spur, TX (79370)	1198
Stamford, TX (79553)	2716
Stephenville, TX (76401)	17678
Sterling City, TX (76951)	968
Stinnett, TX (79083)	1988
Stratford, TX (79084)	1911
Strawn, TX (76475)	774
Sudan, TX (79371)	1111
Sunray, TX (79086)	1748
Sunset, TX (76270)	1477
Sweetwater, TX (79556)	10052
Tahoka, TX (79373)	2598
Texline, TX (79087)	546
Throckmorton, TX (76483)	865
Tioga, TX (76271)	1188
Tolar, TX (76476)	2085
Trent, TX (79561)	562
Tulia, TX (79088)	3992
Tuscola, TX (79562)	3090
Tye, TX (79563)	1064
Valley View, TX (76272)	3710
Vega, TX (79092)	996
Venus, TX (76084)	5930
Vernon, TX (76384)	9373
Weatherford, TX (76085)	7742
Weatherford, TX (76086)	15575
Weatherford, TX (76087)	20580
Weatherford, TX (76088)	9039
Wellington, TX (79095)	2057
Wheeler, TX (79096)	1776
White Deer, TX (79097)	1013
Whitesboro, TX (76273)	7231
Wichita Falls, TX (76301)	11757
Wichita Falls, TX (76302)	8940
Wichita Falls, TX (76305)	4297
Wichita Falls, TX (76306)	11563
Wichita Falls, TX (76308)	15648
Wichita Falls, TX (76309)	10330
Wichita Falls, TX (76310)	14715
Sheppard Afb, TX (76311)	2376
Wilson, TX (79381)	761
Windthorst, TX (76389)	1186
Winters, TX (79567)	2650
Wolfforth, TX (79382)	5456
Zephyr, TX (76890)	711
Alvin, TX (77511)	34258
Anahuac, TX (77514)	4278
Anderson, TX (77830)	2140
Angleton, TX (77515)	20615
Bacliff, TX (77518)	6825
Batson, TX (77519)	870
Bay City, TX (77414)	16084
Baytown, TX (77520)	31972
Baytown, TX (77521)	36379
Baytown, TX (77523)	10257
Beasley, TX (77417)	1494
Lumberton, TX (77657)	16252
Beaumont, TX (77701)	10033
Beaumont, TX (77702)	2378
Beaumont, TX (77703)	9883
Beaumont, TX (77705)	19772
Beaumont, TX (77706)	22799
Beaumont, TX (77707)	13082
Beaumont, TX (77708)	8916
Beaumont, TX (77713)	9424
Bedias, TX (77831)	2191
Bellaire, TX (77401)	15358
Bellville, TX (77418)	7719
Boling, TX (77420)	1901
Brazoria, TX (77422)	10334
Brenham, TX (77833)	19892
Bridge City, TX (77611)	6964
Brookshire, TX (77423)	6299
Bryan, TX (77801)	7685
Bryan, TX (77802)	17103
Bryan, TX (77803)	20368
Bryan, TX (77807)	6276
Bryan, TX (77808)	8997
Buna, TX (77612)	6676
Burton, TX (77835)	2021
Caldwell, TX (77836)	8783
Calvert, TX (77837)	1213
Channelview, TX (77530)	23568
Chappell Hill, TX (77426)	1654
Cleveland, TX (77327)	13398
Cleveland, TX (77328)	11328
Clute, TX (77531)	11888
Coldspring, TX (77331)	4896
College Station, TX (77840)	17629
College Station, TX (77845)	35385
Conroe, TX (77301)	18057
Conroe, TX (77302)	13425
Conroe, TX (77303)	11677
Conroe, TX (77304)	16433
Conroe, TX (77306)	7936
Conroe, TX (77384)	10245
Conroe, TX (77385)	15067
Crosby, TX (77532)	21391
Cypress, TX (77429)	58295
Cypress, TX (77433)	37962
Damon, TX (77430)	1788
Danbury, TX (77534)	2432
Dayton, TX (77535)	21007
Deer Park, TX (77536)	26822
Devers, TX (77538)	688
Dickinson, TX (77539)	29043
Dime Box, TX (77853)	847
Eagle Lake, TX (77434)	3627
East Bernard, TX (77435)	4064
El Campo, TX (77437)	13671
Franklin, TX (77856)	3468
Fred, TX (77616)	965
Freeport, TX (77541)	12099
Fresno, TX (77545)	14427
Friendswood, TX (77546)	40237
Fulshear, TX (77441)	4220
Galena Park, TX (77547)	7509
Galveston, TX (77550)	15089
Galveston, TX (77551)	11919
Galveston, TX (77554)	5473
Garwood, TX (77442)	778
Goodrich, TX (77335)	1633
Groves, TX (77619)	13220
Guy, TX (77444)	687
Hamshire, TX (77622)	1348
Hankamer, TX (77560)	877
Hearne, TX (77859)	5428
Hempstead, TX (77445)	8885
Highlands, TX (77562)	8609
Hillister, TX (77624)	699
Hitchcock, TX (77563)	6870
Hockley, TX (77447)	9119
Houston, TX (77002)	4878
Houston, TX (77003)	6442
Houston, TX (77004)	17083
Houston, TX (77005)	20268
Houston, TX (77006)	14422
Houston, TX (77007)	23282
Houston, TX (77008)	23616
Houston, TX (77009)	27460
Houston, TX (77010)	396
Houston, TX (77011)	12917
Houston, TX (77012)	13675
Houston, TX (77013)	11306
Houston, TX (77014)	19914
Houston, TX (77015)	38860
Houston, TX (77016)	21001
Houston, TX (77017)	22608
Houston, TX (77018)	20653
Houston, TX (77019)	15167
Houston, TX (77020)	17899
Houston, TX (77021)	17987
Houston, TX (77022)	22098
Houston, TX (77023)	20162
Houston, TX (77024)	30150
Houston, TX (77025)	19188
Houston, TX (77026)	16377
Houston, TX (77027)	11716
Houston, TX (77028)	12237
Houston, TX (77029)	13364
Houston, TX (77030)	7819
Houston, TX (77031)	10795
Houston, TX (77032)	7859
Houston, TX (77033)	20575
Houston, TX (77034)	23939
Houston, TX (77035)	24203
Houston, TX (77036)	39848
Houston, TX (77037)	13468
Houston, TX (77038)	18155
Houston, TX (77039)	19546
Houston, TX (77040)	35441
Houston, TX (77041)	29844
Houston, TX (77042)	27841
Houston, TX (77043)	17872
Houston, TX (77044)	22673
Houston, TX (77045)	22459
Houston, TX (77046)	1181
Houston, TX (77047)	15986
Houston, TX (77048)	11044
Houston, TX (77049)	21095
Houston, TX (77050)	3245
Houston, TX (77051)	10299
Houston, TX (77053)	21930
Houston, TX (77054)	13884
Houston, TX (77055)	28009
Houston, TX (77056)	16303
Houston, TX (77057)	27237
Houston, TX (77058)	12262
Houston, TX (77059)	15555
Houston, TX (77060)	25102
Houston, TX (77061)	16149
Houston, TX (77062)	21952
Houston, TX (77063)	23126
Houston, TX (77064)	36400
Houston, TX (77065)	27200
Houston, TX (77066)	24961
Houston, TX (77067)	20865
Houston, TX (77068)	8056
Houston, TX (77069)	13847
Houston, TX (77070)	36163
Houston, TX (77071)	19369
Houston, TX (77072)	40152
Houston, TX (77073)	24816
Houston, TX (77074)	24151
Houston, TX (77075)	26273
Houston, TX (77076)	21487
Houston, TX (77077)	40493
Houston, TX (77078)	10560
Houston, TX (77079)	27970
Houston, TX (77080)	29608
Houston, TX (77081)	26173
Houston, TX (77082)	36323
Houston, TX (77083)	54475
Houston, TX (77084)	72890
Houston, TX (77085)	11979
Houston, TX (77086)	19891
Houston, TX (77087)	26541
Houston, TX (77088)	37706
Houston, TX (77089)	38222
Houston, TX (77090)	21910
Houston, TX (77091)	16693
Houston, TX (77092)	24025
Houston, TX (77093)	32205
Houston, TX (77094)	8637
Houston, TX (77095)	56079
Houston, TX (77096)	25918
Houston, TX (77098)	10256
Houston, TX (77099)	33303
Huffman, TX (77336)	10138
Hull, TX (77564)	1298
Humble, TX (77338)	24459
Kingwood, TX (77339)	30377
Kingwood, TX (77345)	23289
Humble, TX (77346)	43880
Humble, TX (77396)	28722
Hungerford, TX (77448)	634
Huntsville, TX (77320)	14906
Huntsville, TX (77340)	15218
Iola, TX (77861)	1815
Katy, TX (77449)	70855
Katy, TX (77450)	58330
Katy, TX (77493)	18532
Katy, TX (77494)	48970
Kemah, TX (77565)	5367
Kountze, TX (77625)	6659
Lake Jackson, TX (77566)	24909
La Marque, TX (77568)	11809
La Porte, TX (77571)	29396
League City, TX (77573)	57331
Liberty, TX (77575)	10637
Liverpool, TX (77577)	996
Livingston, TX (77351)	19917
Louise, TX (77455)	1639
Madisonville, TX (77864)	5881
Magnolia, TX (77354)	23363
Magnolia, TX (77355)	19024
Manvel, TX (77578)	10680
Marquez, TX (77865)	1311
Missouri City, TX (77459)	49473
Missouri City, TX (77489)	28764
Montgomery, TX (77316)	11733
Montgomery, TX (77356)	21140
Navasota, TX (77868)	9960
Nederland, TX (77627)	18870
Needville, TX (77461)	8149
New Caney, TX (77357)	15089
New Waverly, TX (77358)	3907
Normangee, TX (77871)	2796
North Zulch, TX (77872)	1365
Oakhurst, TX (77359)	553
Onalaska, TX (77360)	4008
Orange, TX (77630)	19705
Orange, TX (77632)	16884
Palacios, TX (77465)	5236
Pasadena, TX (77502)	27366
Pasadena, TX (77503)	17820
Pasadena, TX (77504)	16087
Pasadena, TX (77505)	19181
Pasadena, TX (77506)	24241
Pearland, TX (77581)	34077
Pearland, TX (77584)	54550
Pinehurst, TX (77362)	3951
Plantersville, TX (77363)	2303
Pointblank, TX (77364)	1734
Port Arthur, TX (77640)	12079
Port Arthur, TX (77642)	26905
Porter, TX (77365)	19604
Port Neches, TX (77651)	11181
Richards, TX (77873)	964
Richmond, TX (77406)	19460
Richmond, TX (77407)	16357
Richmond, TX (77469)	38667
Rosenberg, TX (77471)	26017
Rosharon, TX (77583)	14168
Santa Fe, TX (77510)	11646
Santa Fe, TX (77517)	4944
Saratoga, TX (77585)	725
Seabrook, TX (77586)	17586
Sealy, TX (77474)	10523
Shepherd, TX (77371)	5204
Silsbee, TX (77656)	13473
Somerville, TX (77879)	3257
Sour Lake, TX (77659)	4115
South Houston, TX (77587)	12312
Splendora, TX (77372)	8811
Spring, TX (77373)	42549
Spring, TX (77379)	59704
Spring, TX (77380)	18495
Spring, TX (77381)	31122
Spring, TX (77382)	28806
Spring, TX (77386)	29707
Spring, TX (77388)	33840
Spring, TX (77389)	17131
Spurger, TX (77660)	1306
Stafford, TX (77477)	25586
Sugar Land, TX (77478)	35424
Sugar Land, TX (77479)	62375
Sugar Land, TX (77498)	26061
Sweeny, TX (77480)	5700
Texas City, TX (77590)	22419
Texas City, TX (77591)	9426
Tomball, TX (77375)	29464
Tomball, TX (77377)	24593
Van Vleck, TX (77482)	1885
Vidor, TX (77662)	19641
Waller, TX (77484)	8699
Wallis, TX (77485)	2572
Wallisville, TX (77597)	576
Warren, TX (77664)	2154
Washington, TX (77880)	1439
Webster, TX (77598)	15658
West Columbia, TX (77486)	5771
Wharton, TX (77488)	10629
Willis, TX (77318)	10722
Willis, TX (77378)	11379
Winnie, TX (77665)	4912
Abbott, TX (76621)	908
Ackerly, TX (79713)	488
Adkins, TX (78101)	6803
Agua Dulce, TX (78330)	927
Alamo, TX (78516)	19793
Alice, TX (78332)	19637
Alpine, TX (79830)	3926
Andrews, TX (79714)	11912
Aquilla, TX (76622)	826
Aransas Pass, TX (78336)	7775
Asherton, TX (78827)	884
Atascosa, TX (78002)	5201
Austin, TX (78701)	4614
Austin, TX (78702)	14748
Austin, TX (78703)	15681
Austin, TX (78704)	29684
Austin, TX (78705)	6321
Austin, TX (78717)	18710
Austin, TX (78719)	1271
Austin, TX (78721)	7819
Austin, TX (78722)	4286
Austin, TX (78723)	19486
Austin, TX (78724)	12800
Austin, TX (78725)	4474
Austin, TX (78726)	10230
Austin, TX (78727)	21646
Austin, TX (78728)	15073
Austin, TX (78729)	21329
Austin, TX (78730)	6427
Austin, TX (78731)	20782
Austin, TX (78732)	10495
Austin, TX (78733)	7359
Austin, TX (78734)	15313
Austin, TX (78735)	12304
Austin, TX (78736)	6186
Austin, TX (78737)	10564
Austin, TX (78738)	10472
Austin, TX (78739)	14154
Austin, TX (78741)	24672
Austin, TX (78742)	568
Austin, TX (78744)	29195
Austin, TX (78745)	42573
Austin, TX (78746)	23723
Austin, TX (78747)	10895
Austin, TX (78748)	31973
Austin, TX (78749)	28596
Austin, TX (78750)	22295
Austin, TX (78751)	8748
Austin, TX (78752)	11032
Austin, TX (78753)	32743
Austin, TX (78754)	10729
Austin, TX (78756)	5681
Austin, TX (78757)	16774
Austin, TX (78758)	30239
Austin, TX (78759)	32533
Axtell, TX (76624)	1873
Balmorhea, TX (79718)	516
Bandera, TX (78003)	7180
Bartlett, TX (76511)	1684
Bastrop, TX (78602)	18734
Batesville, TX (78829)	915
Beeville, TX (78102)	13302
Belton, TX (76513)	26238
Bertram, TX (78605)	3706
Bigfoot, TX (78005)	525
Big Spring, TX (79720)	20058
Bishop, TX (78343)	3432
Blanco, TX (78606)	4315
Blooming Grove, TX (76626)	1268
Blum, TX (76627)	1261
Bergheim, TX (78004)	537
Boerne, TX (78006)	24993
Boerne, TX (78015)	8915
Brackettville, TX (78832)	2426
Bremond, TX (76629)	1537
Briggs, TX (78608)	471
Brownsville, TX (78520)	44082
Brownsville, TX (78521)	66668
Brownsville, TX (78526)	31538
Bruceville, TX (76630)	1397
Buchanan Dam, TX (78609)	1611
Buckholts, TX (76518)	993
Buda, TX (78610)	19063
Burlington, TX (76519)	476
Burnet, TX (78611)	10045
Cameron, TX (76520)	6339
Camp Wood, TX (78833)	1018
Canutillo, TX (79835)	9464
Carmine, TX (78932)	588
Carrizo Springs, TX (78834)	5562
Castroville, TX (78009)	6307
Mico, TX (78056)	1488
Cat Spring, TX (78933)	1201
Cedar Creek, TX (78612)	9367
Cedar Park, TX (78613)	52383
Center Point, TX (78010)	2492
Charlotte, TX (78011)	1482
Chilton, TX (76632)	1266
China Spring, TX (76633)	4396
Cibolo, TX (78108)	22793
Clifton, TX (76634)	5315
Clint, TX (79836)	4646
Columbus, TX (78934)	5742
Alleyton, TX (78935)	689
Comfort, TX (78013)	4424
Converse, TX (78109)	29324
Coolidge, TX (76635)	951
Copperas Cove, TX (76522)	28318
Corpus Christi, TX (78401)	2254
Corpus Christi, TX (78402)	420
Corpus Christi, TX (78404)	11423
Corpus Christi, TX (78405)	10354
Corpus Christi, TX (78406)	714
Corpus Christi, TX (78407)	2055
Corpus Christi, TX (78408)	7942
Corpus Christi, TX (78409)	1990
Corpus Christi, TX (78410)	19702
Corpus Christi, TX (78411)	21125
Corpus Christi, TX (78412)	25241
Corpus Christi, TX (78413)	27973
Corpus Christi, TX (78414)	23189
Corpus Christi, TX (78415)	28579
Corpus Christi, TX (78416)	11479
Corpus Christi, TX (78417)	3233
Corpus Christi, TX (78418)	22032
Cotulla, TX (78014)	3181
Coupland, TX (78615)	999
Covington, TX (76636)	1269
Crane, TX (79731)	3357
Crawford, TX (76638)	2423
Crystal City, TX (78839)	5859
Cuero, TX (77954)	7702
Dale, TX (78616)	4715
Dawson, TX (76639)	1117
Del Rio, TX (78840)	34843
Del Valle, TX (78617)	13088
Devine, TX (78016)	7256
D Hanis, TX (78850)	972
Dilley, TX (78017)	2511
Donna, TX (78537)	23668
Driftwood, TX (78619)	2577
Dripping Springs, TX (78620)	12581
Eagle Pass, TX (78852)	34295
Edcouch, TX (78538)	6689
Eddy, TX (76524)	2318
Edinburg, TX (78539)	26436
Edinburg, TX (78541)	25248
Edinburg, TX (78542)	25360
Edna, TX (77957)	6623
Elgin, TX (78621)	16211
Elmendorf, TX (78112)	5989
Elm Mott, TX (76640)	2480
El Paso, TX (79901)	12682
El Paso, TX (79902)	16056
El Paso, TX (79903)	14072
El Paso, TX (79904)	24327
El Paso, TX (79905)	18528
El Paso, TX (79906)	3845
El Paso, TX (79907)	43435
El Paso, TX (79908)	1253
El Paso, TX (79911)	1031
El Paso, TX (79912)	58177
El Paso, TX (79915)	29001
Fort Bliss, TX (79916)	1803
El Paso, TX (79922)	7268
El Paso, TX (79924)	45854
El Paso, TX (79925)	31120
El Paso, TX (79927)	29950
El Paso, TX (79928)	33379
El Paso, TX (79930)	20170
El Paso, TX (79932)	18705
El Paso, TX (79934)	14026
El Paso, TX (79935)	13653
El Paso, TX (79936)	88503
El Paso, TX (79938)	35094
Evant, TX (76525)	749
Falfurrias, TX (78355)	5377
Falls City, TX (78113)	1807
Fayetteville, TX (78940)	1615
Fischer, TX (78623)	800
Flatonia, TX (78941)	2294
Florence, TX (76527)	3277
Floresville, TX (78114)	15049
Fort Davis, TX (79734)	1649
Fort Hancock, TX (79839)	1396
Fort Stockton, TX (79735)	9052
Fredericksburg, TX (78624)	18164
Freer, TX (78357)	2762
Frost, TX (76641)	1259
Ganado, TX (77962)	2870
Garden City, TX (79739)	839
Gardendale, TX (79758)	1773
Gatesville, TX (76528)	12184
Georgetown, TX (78626)	17253
Georgetown, TX (78628)	22495
Georgetown, TX (78633)	15079
George West, TX (78022)	3787
Giddings, TX (78942)	7076
Goliad, TX (77963)	4188
Gonzales, TX (78629)	9049
Granger, TX (76530)	2015
Groesbeck, TX (76642)	4736
Hallettsville, TX (77964)	6372
Hamilton, TX (76531)	3882
Harlingen, TX (78550)	35476
Harlingen, TX (78552)	22159
Harper, TX (78631)	2088
Harwood, TX (78632)	756
Hebbronville, TX (78361)	3859
Helotes, TX (78023)	21122
Hewitt, TX (76643)	11819
Hidalgo, TX (78557)	12003
Hillsboro, TX (76645)	8425
Hobson, TX (78117)	495
Holland, TX (76534)	2039
Hondo, TX (78861)	9110
Hubbard, TX (76648)	1841
Hunt, TX (78024)	1266
Hutto, TX (78634)	17690
Industry, TX (78944)	555
Inez, TX (77968)	2188
Ingleside, TX (78362)	7800
Ingram, TX (78025)	4186
Iredell, TX (76649)	579
Italy, TX (76651)	2328
Jarrell, TX (76537)	3361
Johnson City, TX (78636)	2970
Jonesboro, TX (76538)	615
Jourdanton, TX (78026)	4473
Karnes City, TX (78118)	3057
Kempner, TX (76539)	6791
Kenedy, TX (78119)	3584
Kermit, TX (79745)	4819
Kerrville, TX (78028)	28323
Killeen, TX (76541)	13018
Killeen, TX (76542)	28695
Killeen, TX (76543)	22469
Fort Hood, TX (76544)	20511
Harker Heights, TX (76548)	20541
Killeen, TX (76549)	32269
Kingsbury, TX (78638)	1603
Kingsland, TX (78639)	5456
Kingsville, TX (78363)	19820
Knippa, TX (78870)	707
Kopperl, TX (76652)	804
Kosse, TX (76653)	847
Kyle, TX (78640)	32070
La Coste, TX (78039)	1493
La Feria, TX (78559)	8320
La Grange, TX (78945)	8215
La Joya, TX (78560)	3698
Lampasas, TX (76550)	9463
Laredo, TX (78040)	28418
Laredo, TX (78041)	35152
Laredo, TX (78043)	29088
Laredo, TX (78045)	42658
Laredo, TX (78046)	42901
La Vernia, TX (78121)	9419
Leakey, TX (78873)	1373
Leander, TX (78641)	33858
Leander, TX (78645)	8465
Ledbetter, TX (78946)	721
Lexington, TX (78947)	3544
Liberty Hill, TX (78642)	7808
Lincoln, TX (78948)	711
Linn, TX (78563)	590
Little River Academy, TX (76554)	1813
Llano, TX (78643)	5102
Lockhart, TX (78644)	12604
Lolita, TX (77971)	750
Lorena, TX (76655)	6943
Los Fresnos, TX (78566)	10391
Lott, TX (76656)	1808
Luling, TX (78648)	5660
Lyford, TX (78569)	2993
Lytle, TX (78052)	5379
Mcallen, TX (78501)	40712
Mcallen, TX (78503)	14859
Mcallen, TX (78504)	34673
Mc Camey, TX (79752)	1750
Mc Dade, TX (78650)	1248
Mc Gregor, TX (76657)	7699
Mc Queeney, TX (78123)	2101
Manchaca, TX (78652)	3720
Manor, TX (78653)	12596
Marble Falls, TX (78654)	14340
Horseshoe Bay, TX (78657)	4394
Marfa, TX (79843)	1976
Marion, TX (78124)	4896
Marlin, TX (76661)	4823
Mart, TX (76664)	2480
Martindale, TX (78655)	2140
Mathis, TX (78368)	7154
Maxwell, TX (78656)	1736
Medina, TX (78055)	1238
Mercedes, TX (78570)	19819
Meridian, TX (76665)	1972
Mexia, TX (76667)	8709
Midland, TX (79701)	21513
Midland, TX (79703)	16563
Midland, TX (79705)	25476
Midland, TX (79706)	13665
Midland, TX (79707)	25826
Milano, TX (76556)	1174
Milford, TX (76670)	1001
Mission, TX (78572)	48297
Mission, TX (78573)	24515
Mission, TX (78574)	30029
Monahans, TX (79756)	7210
Moody, TX (76557)	3982
Moore, TX (78057)	727
Morgan, TX (76671)	1210
Moulton, TX (77975)	1506
Mountain Home, TX (78058)	1014
Mount Calm, TX (76673)	808
Natalia, TX (78059)	3739
New Braunfels, TX (78130)	47380
New Braunfels, TX (78132)	16088
Canyon Lake, TX (78133)	13172
New Ulm, TX (78950)	1685
Nixon, TX (78140)	2489
Nolanville, TX (76559)	3791
Nordheim, TX (78141)	500
Odem, TX (78370)	3979
Odessa, TX (79761)	23182
Odessa, TX (79762)	30037
Odessa, TX (79763)	25472
Odessa, TX (79764)	15827
Odessa, TX (79765)	5651
Odessa, TX (79766)	3980
Oglesby, TX (76561)	833
Olmito, TX (78575)	3727
Orange Grove, TX (78372)	4375
Paige, TX (78659)	2142
Pearsall, TX (78061)	6716
Pecos, TX (79772)	7403
Penitas, TX (78576)	5872
Pflugerville, TX (78660)	53788
Pharr, TX (78577)	46199
Pipe Creek, TX (78063)	6912
Pleasanton, TX (78064)	10533
Port Aransas, TX (78373)	3227
Port Isabel, TX (78578)	7482
South Padre Island, TX (78597)	2133
Portland, TX (78374)	13984
Port Lavaca, TX (77979)	13405
Poteet, TX (78065)	7698
Premont, TX (78375)	2517
Presidio, TX (79845)	5481
Purdon, TX (76679)	1098
Quemado, TX (78877)	640
Raymondville, TX (78580)	8338
Red Rock, TX (78662)	1788
Refugio, TX (78377)	3003
Riesel, TX (76682)	2234
Rio Grande City, TX (78582)	24672
Rio Hondo, TX (78583)	4597
Rio Medina, TX (78066)	580
Riviera, TX (78379)	1432
Robstown, TX (78380)	16768
Rockdale, TX (76567)	7181
Rockport, TX (78382)	11633
Rocksprings, TX (78880)	1295
Rogers, TX (76569)	2166
Roma, TX (78584)	14262
Rosanky, TX (78953)	865
Rosebud, TX (76570)	2000
Round Mountain, TX (78663)	485
Round Rock, TX (78664)	42720
Round Rock, TX (78665)	24821
Round Rock, TX (78681)	40542
Round Top, TX (78954)	889
Runge, TX (78151)	1060
Sabinal, TX (78881)	1721
Saint Hedwig, TX (78152)	2103
Salado, TX (76571)	5977
San Antonio, TX (78201)	32633
San Antonio, TX (78202)	9378
San Antonio, TX (78203)	4104
San Antonio, TX (78204)	8275
San Antonio, TX (78205)	1014
San Antonio, TX (78207)	32629
San Antonio, TX (78208)	2648
San Antonio, TX (78209)	30337
San Antonio, TX (78210)	26813
San Antonio, TX (78211)	23554
San Antonio, TX (78212)	19934
San Antonio, TX (78213)	30456
San Antonio, TX (78214)	17201
San Antonio, TX (78215)	798
San Antonio, TX (78216)	29493
San Antonio, TX (78217)	25218
San Antonio, TX (78218)	23041
San Antonio, TX (78219)	11105
San Antonio, TX (78220)	12159
San Antonio, TX (78221)	26597
San Antonio, TX (78222)	13709
San Antonio, TX (78223)	36315
San Antonio, TX (78224)	13598
San Antonio, TX (78225)	10231
San Antonio, TX (78226)	4586
San Antonio, TX (78227)	34553
San Antonio, TX (78228)	43510
San Antonio, TX (78229)	19044
San Antonio, TX (78230)	30808
San Antonio, TX (78231)	7193
San Antonio, TX (78232)	29612
San Antonio, TX (78233)	34631
San Antonio, TX (78234)	3432
Lackland A F B, TX (78236)	1539
San Antonio, TX (78237)	27055
San Antonio, TX (78238)	17634
San Antonio, TX (78239)	22176
San Antonio, TX (78240)	38085
San Antonio, TX (78242)	21605
San Antonio, TX (78244)	22146
San Antonio, TX (78245)	43391
San Antonio, TX (78247)	41124
San Antonio, TX (78248)	12500
San Antonio, TX (78249)	34588
San Antonio, TX (78250)	45011
San Antonio, TX (78251)	37672
San Antonio, TX (78252)	3728
San Antonio, TX (78253)	23911
San Antonio, TX (78254)	34903
San Antonio, TX (78255)	8037
San Antonio, TX (78256)	4383
San Antonio, TX (78257)	3255
San Antonio, TX (78258)	34168
San Antonio, TX (78259)	18765
San Antonio, TX (78260)	18350
San Antonio, TX (78261)	10441
San Antonio, TX (78263)	3708
San Antonio, TX (78264)	8786
San Antonio, TX (78266)	5406
San Benito, TX (78586)	34392
Sandia, TX (78383)	2740
San Diego, TX (78384)	4355
San Elizario, TX (79849)	9310
San Juan, TX (78589)	27552
San Marcos, TX (78666)	35271
Santa Rosa, TX (78593)	3900
San Ygnacio, TX (78067)	619
Schertz, TX (78154)	25677
Schulenburg, TX (78956)	4294
Seadrift, TX (77983)	1549
Seguin, TX (78155)	33603
Shiner, TX (77984)	3524
Sinton, TX (78387)	7566
Skidmore, TX (78389)	1280
Smiley, TX (78159)	675
Smithville, TX (78957)	6612
Somerset, TX (78069)	3806
Spicewood, TX (78669)	7063
Spring Branch, TX (78070)	12245
Bulverde, TX (78163)	8664
Stanton, TX (79782)	3267
Stockdale, TX (78160)	3016
Stonewall, TX (78671)	678
Sullivan City, TX (78595)	3983
Sutherland Springs, TX (78161)	713
Taft, TX (78390)	4709
Taylor, TX (76574)	13742
Temple, TX (76501)	12401
Temple, TX (76502)	24523
Temple, TX (76504)	16418
Terlingua, TX (79852)	528
Thorndale, TX (76577)	2366
Thornton, TX (76687)	1119
Thrall, TX (76578)	1275
Three Rivers, TX (78071)	2633
Tilden, TX (78072)	536
Tivoli, TX (77990)	613
Tow, TX (78672)	725
Troy, TX (76579)	3427
Universal City, TX (78148)	16453
Utopia, TX (78884)	962
Uvalde, TX (78801)	14841
Valley Mills, TX (76689)	3079
Victoria, TX (77901)	30172
Victoria, TX (77904)	20440
Victoria, TX (77905)	11396
Von Ormy, TX (78073)	5861
Waco, TX (76701)	777
Waco, TX (76704)	4540
Waco, TX (76705)	20530
Waco, TX (76706)	19769
Waco, TX (76707)	11281
Waco, TX (76708)	18077
Waco, TX (76710)	17968
Waco, TX (76711)	6427
Woodway, TX (76712)	18549
Waelder, TX (78959)	1267
Walnut Springs, TX (76690)	986
Weimar, TX (78962)	3718
Weslaco, TX (78596)	40400
West, TX (76691)	5227
West Point, TX (78963)	655
Whitney, TX (76692)	7646
Wimberley, TX (78676)	10689
Woodsboro, TX (78393)	2004
Wortham, TX (76693)	1349
Yancey, TX (78886)	455
Yoakum, TX (77995)	7398
Yorktown, TX (78164)	3046
Zapata, TX (78076)	8459
Akron, IN (46910)	2932
Albany, IN (47320)	3568
Albion, IN (46701)	6220
Alexandria, IN (46001)	9317
Amboy, IN (46911)	1271
Anderson, IN (46011)	14399
Anderson, IN (46012)	15730
Anderson, IN (46013)	14967
Anderson, IN (46016)	12898
Anderson, IN (46017)	5220
Andrews, IN (46702)	1977
Angola, IN (46703)	14245
Arcadia, IN (46030)	2714
Argos, IN (46501)	3098
Arlington, IN (46104)	851
Ashley, IN (46705)	1393
Atlanta, IN (46031)	2015
Attica, IN (47918)	5347
Auburn, IN (46706)	15863
Avilla, IN (46710)	4010
Bainbridge, IN (46105)	1644
Bargersville, IN (46106)	5129
Battle Ground, IN (47920)	2216
Bedford, IN (47421)	22719
Beech Grove, IN (46107)	10544
Berne, IN (46711)	5758
Bicknell, IN (47512)	2942
Birdseye, IN (47513)	1683
Bloomfield, IN (47424)	7718
Bloomingdale, IN (47832)	873
Bloomington, IN (47401)	27740
Bloomington, IN (47403)	23200
Bloomington, IN (47404)	14505
Bloomington, IN (47408)	12385
Bluffton, IN (46714)	12510
Boswell, IN (47921)	886
Bourbon, IN (46504)	2922
Bowling Green, IN (47833)	892
Brazil, IN (47834)	15691
Bremen, IN (46506)	8347
Bringhurst, IN (46913)	1196
Bristol, IN (46507)	8126
Bristow, IN (47515)	772
Brook, IN (47922)	1334
Brookston, IN (47923)	3198
Brownsburg, IN (46112)	29318
Brownstown, IN (47220)	4649
Brownsville, IN (47325)	654
Bruceville, IN (47516)	1107
Bryant, IN (47326)	1561
Bunker Hill, IN (46914)	1787
Burlington, IN (46915)	606
Burnettsville, IN (47926)	908
Butler, IN (46721)	4116
Butlerville, IN (47223)	1303
Cambridge City, IN (47327)	3585
Camby, IN (46113)	11696
Camden, IN (46917)	1483
Cannelburg, IN (47519)	518
Cannelton, IN (47520)	2528
Carbon, IN (47837)	958
Carlisle, IN (47838)	1728
Carmel, IN (46032)	36835
Carmel, IN (46033)	31533
Carthage, IN (46115)	1649
Cayuga, IN (47928)	1658
Cedar Lake, IN (46303)	11807
Celestine, IN (47521)	869
Centerpoint, IN (47840)	1301
Centerville, IN (47330)	4852
Chalmers, IN (47929)	771
Charlottesville, IN (46117)	605
Chesterton, IN (46304)	21130
Churubusco, IN (46723)	6714
Cicero, IN (46034)	6073
Clarks Hill, IN (47930)	936
Clay City, IN (47841)	1810
Claypool, IN (46510)	2943
Clayton, IN (46118)	4309
Clinton, IN (47842)	7838
Cloverdale, IN (46120)	5216
Coal City, IN (47427)	838
Coatesville, IN (46121)	4377
Colfax, IN (46035)	991
Columbia City, IN (46725)	19750
Columbus, IN (47201)	34763
Columbus, IN (47203)	22245
Commiskey, IN (47227)	1320
Connersville, IN (47331)	18625
Converse, IN (46919)	2064
Corunna, IN (46730)	1163
Cory, IN (47846)	597
Covington, IN (47932)	4661
Craigville, IN (46731)	535
Crawfordsville, IN (47933)	23102
Cromwell, IN (46732)	2622
Crothersville, IN (47229)	2736
Crown Point, IN (46307)	51892
Culver, IN (46511)	3565
Cutler, IN (46920)	921
Dale, IN (47523)	2768
Daleville, IN (47334)	2929
Dana, IN (47847)	998
Danville, IN (46122)	12908
Avon, IN (46123)	27883
Darlington, IN (47940)	1293
Decatur, IN (46733)	15973
Delphi, IN (46923)	6941
Demotte, IN (46310)	11377
Denver, IN (46926)	1506
Deputy, IN (47230)	1738
Dubois, IN (47527)	1745
Dugger, IN (47848)	1437
Dunkirk, IN (47336)	3066
Dupont, IN (47231)	978
Dyer, IN (46311)	18518
Earl Park, IN (47942)	580
East Chicago, IN (46312)	19514
Eaton, IN (47338)	2403
Economy, IN (47339)	572
Edinburgh, IN (46124)	6511
Edwardsport, IN (47528)	611
Elizabethtown, IN (47232)	2333
Elkhart, IN (46514)	33681
Elkhart, IN (46516)	25256
Elkhart, IN (46517)	18308
Ellettsville, IN (47429)	6269
Elnora, IN (47529)	798
Elwood, IN (46036)	9861
Etna Green, IN (46524)	1716
Fairland, IN (46126)	4262
Fairmount, IN (46928)	4148
Fair Oaks, IN (47943)	767
Farmersburg, IN (47850)	2120
Farmland, IN (47340)	2503
Ferdinand, IN (47532)	4241
Fillmore, IN (46128)	1796
Fishers, IN (46037)	29121
Fishers, IN (46038)	32761
Flat Rock, IN (47234)	1294
Flora, IN (46929)	2816
Forest, IN (46039)	654
Fortville, IN (46040)	8399
Fort Wayne, IN (46802)	6400
Fort Wayne, IN (46803)	6491
Fort Wayne, IN (46804)	23763
Fort Wayne, IN (46805)	16144
Fort Wayne, IN (46806)	16210
Fort Wayne, IN (46807)	12274
Fort Wayne, IN (46808)	14904
Fort Wayne, IN (46809)	7503
Fort Wayne, IN (46814)	10856
Fort Wayne, IN (46815)	22159
Fort Wayne, IN (46816)	13320
Fort Wayne, IN (46818)	15245
Fort Wayne, IN (46819)	7554
Fort Wayne, IN (46825)	23414
Fort Wayne, IN (46835)	28626
Fort Wayne, IN (46845)	19753
Fountain City, IN (47341)	1852
Fountaintown, IN (46130)	2222
Fowler, IN (47944)	2968
Francesville, IN (47946)	1761
Frankfort, IN (46041)	19981
Franklin, IN (46131)	24839
Needham, IN (46162)	468
Frankton, IN (46044)	2669
Freedom, IN (47431)	1176
Freetown, IN (47235)	1546
Fremont, IN (46737)	6205
French Lick, IN (47432)	3766
Galveston, IN (46932)	3143
Garrett, IN (46738)	6413
Gary, IN (46402)	4211
Gary, IN (46403)	9197
Gary, IN (46404)	12209
Lake Station, IN (46405)	9254
Gary, IN (46406)	7183
Gary, IN (46407)	8512
Gary, IN (46408)	12397
Gary, IN (46409)	6454
Merrillville, IN (46410)	29357
Gas City, IN (46933)	5559
Gaston, IN (47342)	2389
Geneva, IN (46740)	2845
Gentryville, IN (47537)	738
Glenwood, IN (46133)	761
Goodland, IN (47948)	1164
Goshen, IN (46526)	25271
Goshen, IN (46528)	21252
Gosport, IN (47433)	3398
Grabill, IN (46741)	3125
Granger, IN (46530)	27294
Greencastle, IN (46135)	13457
Greenfield, IN (46140)	33009
Greensburg, IN (47240)	17987
Greens Fork, IN (47345)	1190
Greentown, IN (46936)	5357
Greenwood, IN (46142)	27789
Greenwood, IN (46143)	41045
Griffith, IN (46319)	15622
Grovertown, IN (46531)	1217
Hagerstown, IN (47346)	3488
Hamilton, IN (46742)	2831
Hamlet, IN (46532)	1540
Hammond, IN (46320)	9295
Munster, IN (46321)	21095
Highland, IN (46322)	21160
Hammond, IN (46323)	17476
Hammond, IN (46324)	17081
Hammond, IN (46327)	8413
Hanna, IN (46340)	1052
Hanover, IN (47243)	4133
Harlan, IN (46743)	1940
Hartford City, IN (47348)	8400
Hartsville, IN (47244)	696
Hebron, IN (46341)	9142
Heltonville, IN (47436)	1320
Hillsboro, IN (47949)	1134
Hillsdale, IN (47854)	698
Hoagland, IN (46745)	1719
Hobart, IN (46342)	26684
Holland, IN (47541)	1150
Hope, IN (47246)	3777
Howe, IN (46746)	3249
Hudson, IN (46747)	2143
Huntertown, IN (46748)	4605
Huntingburg, IN (47542)	8304
Huntington, IN (46750)	22354
Idaville, IN (47950)	739
Indianapolis, IN (46201)	21035
Indianapolis, IN (46202)	9152
Indianapolis, IN (46203)	28041
Indianapolis, IN (46204)	2623
Indianapolis, IN (46205)	19239
Indianapolis, IN (46208)	14114
Indianapolis, IN (46214)	19379
Indianapolis, IN (46216)	1359
Indianapolis, IN (46217)	25860
Indianapolis, IN (46218)	20903
Indianapolis, IN (46219)	27301
Indianapolis, IN (46220)	29728
Indianapolis, IN (46221)	21056
Indianapolis, IN (46222)	24522
Indianapolis, IN (46224)	29223
Indianapolis, IN (46225)	4974
Indianapolis, IN (46226)	34123
Indianapolis, IN (46227)	42661
Indianapolis, IN (46228)	12564
Indianapolis, IN (46229)	22077
Indianapolis, IN (46231)	9077
Indianapolis, IN (46234)	21319
Indianapolis, IN (46235)	22718
Indianapolis, IN (46236)	24141
Indianapolis, IN (46237)	33325
Indianapolis, IN (46239)	21289
Indianapolis, IN (46240)	16603
Indianapolis, IN (46241)	23640
Indianapolis, IN (46250)	16186
Indianapolis, IN (46254)	30767
Indianapolis, IN (46256)	21134
Indianapolis, IN (46259)	10274
Indianapolis, IN (46260)	26633
Indianapolis, IN (46268)	20516
Indianapolis, IN (46278)	7925
Indianapolis, IN (46280)	5998
Ingalls, IN (46048)	1609
Jamestown, IN (46147)	2504
Jasonville, IN (47438)	3563
Jasper, IN (47546)	18351
Jonesboro, IN (46938)	2776
Kempton, IN (46049)	756
Kendallville, IN (46755)	12573
Kentland, IN (47951)	1845
Kewanna, IN (46939)	1808
Keystone, IN (46759)	506
Kimmell, IN (46760)	1096
Kingman, IN (47952)	2261
Kirklin, IN (46050)	1583
Knightstown, IN (46148)	4248
Knox, IN (46534)	8914
Kokomo, IN (46901)	30182
Kokomo, IN (46902)	29763
Kouts, IN (46347)	4119
La Crosse, IN (46348)	949
Ladoga, IN (47954)	1837
Lafayette, IN (47901)	2251
Lafayette, IN (47904)	11396
Lafayette, IN (47905)	32618
West Lafayette, IN (47906)	33164
Lafayette, IN (47909)	31357
La Fontaine, IN (46940)	2230
Lagrange, IN (46761)	9012
Lagro, IN (46941)	1044
Lake Village, IN (46349)	2807
Lakeville, IN (46536)	2804
Evanston, IN (47531)	829
Lamar, IN (47550)	683
Laotto, IN (46763)	1451
Lapel, IN (46051)	2467
La Porte, IN (46350)	36314
Larwill, IN (46764)	1237
Lebanon, IN (46052)	18846
Leesburg, IN (46538)	3649
Leo, IN (46765)	4631
Leopold, IN (47551)	492
Lewis, IN (47858)	575
Lewisville, IN (47352)	881
Liberty, IN (47353)	4923
Liberty Center, IN (46766)	473
Ligonier, IN (46767)	6961
Linden, IN (47955)	929
Linton, IN (47441)	7613
Lizton, IN (46149)	1685
Logansport, IN (46947)	23570
Loogootee, IN (47553)	6865
Losantville, IN (47354)	975
Lowell, IN (46356)	14904
Lucerne, IN (46950)	635
Lynn, IN (47355)	2399
Lyons, IN (47443)	942
Mc Cordsville, IN (46055)	8450
Macy, IN (46951)	1852
Madison, IN (47250)	18062
Manilla, IN (46150)	725
Marion, IN (46952)	16978
Marion, IN (46953)	16111
Markle, IN (46770)	2394
Markleville, IN (46056)	2092
Marshall, IN (47859)	819
Martinsville, IN (46151)	26954
Medaryville, IN (47957)	1474
Medora, IN (47260)	1612
Mentone, IN (46539)	2016
Merom, IN (47861)	521
Michigan City, IN (46360)	33533
Michigantown, IN (46057)	1008
Middlebury, IN (46540)	9472
Middletown, IN (47356)	5193
Milford, IN (46542)	3814
Mill Creek, IN (46365)	986
Millersburg, IN (46543)	2685
Milroy, IN (46156)	1208
Milton, IN (47357)	1099
Mishawaka, IN (46544)	25101
Mishawaka, IN (46545)	19804
Mitchell, IN (47446)	8185
Modoc, IN (47358)	800
Monon, IN (47959)	2296
Monroe, IN (46772)	2287
Monroe City, IN (47557)	1186
Monroeville, IN (46773)	3171
Monrovia, IN (46157)	3025
Monterey, IN (46960)	978
Montezuma, IN (47862)	1354
Montgomery, IN (47558)	3259
Monticello, IN (47960)	12529
Montpelier, IN (47359)	2631
Mooreland, IN (47360)	1380
Mooresville, IN (46158)	20650
Morgantown, IN (46160)	5355
Morocco, IN (47963)	1702
Morristown, IN (46161)	2227
Mulberry, IN (46058)	1847
Muncie, IN (47302)	20965
Muncie, IN (47303)	15957
Muncie, IN (47304)	23592
Muncie, IN (47305)	2333
Nappanee, IN (46550)	9937
Nashville, IN (47448)	6703
Newberry, IN (47449)	491
New Carlisle, IN (46552)	5617
New Castle, IN (47362)	22418
New Haven, IN (46774)	14131
New Palestine, IN (46163)	11130
New Paris, IN (46553)	2946
New Richmond, IN (47967)	659
New Ross, IN (47968)	885
Nineveh, IN (46164)	3765
Noblesville, IN (46060)	28971
Noblesville, IN (46062)	24803
Norman, IN (47264)	1090
North Judson, IN (46366)	4825
North Liberty, IN (46554)	3774
North Manchester, IN (46962)	7542
North Salem, IN (46165)	1343
North Vernon, IN (47265)	16632
North Webster, IN (46555)	2622
Oaktown, IN (47561)	1370
Odon, IN (47562)	3519
Oolitic, IN (47451)	1121
Orland, IN (46776)	1324
Orleans, IN (47452)	4009
Osceola, IN (46561)	11453
Ossian, IN (46777)	5590
Otterbein, IN (47970)	1776
Otwell, IN (47564)	1241
Oxford, IN (47971)	1541
Paoli, IN (47454)	5978
Paragon, IN (46166)	1961
Paris Crossing, IN (47270)	611
Parker City, IN (47368)	2449
Pendleton, IN (46064)	11845
Pennville, IN (47369)	1070
Perrysville, IN (47974)	987
Peru, IN (46970)	19541
Petersburg, IN (47567)	4936
Pierceton, IN (46562)	4212
Pine Village, IN (47975)	650
Pittsboro, IN (46167)	5658
Plainfield, IN (46168)	23921
Plainville, IN (47568)	735
Pleasant Lake, IN (46779)	1706
Plymouth, IN (46563)	19114
Poland, IN (47868)	2300
Poneto, IN (46781)	799
Portage, IN (46368)	32445
Portland, IN (47371)	10187
Quincy, IN (47456)	1049
Redkey, IN (47373)	1830
Reelsville, IN (46171)	1522
Remington, IN (47977)	2022
Rensselaer, IN (47978)	9430
Reynolds, IN (47980)	987
Richmond, IN (47374)	35906
Ridgeville, IN (47380)	1696
Roachdale, IN (46172)	2078
Roann, IN (46974)	1493
Roanoke, IN (46783)	5590
Rochester, IN (46975)	11848
Rockville, IN (47872)	5796
Rolling Prairie, IN (46371)	3110
Rome City, IN (46784)	1982
Romney, IN (47981)	745
Rosedale, IN (47874)	2796
Rossville, IN (46065)	3053
Royal Center, IN (46978)	1871
Rushville, IN (46173)	9157
Russellville, IN (46175)	541
Russiaville, IN (46979)	4351
Saint Anthony, IN (47575)	998
Saint Joe, IN (46785)	1285
Saint John, IN (46373)	12407
Saint Meinrad, IN (47577)	871
Saint Paul, IN (47272)	1688
Sandborn, IN (47578)	666
San Pierre, IN (46374)	857
Santa Claus, IN (47579)	2373
Schererville, IN (46375)	21097
Scipio, IN (47273)	1725
Selma, IN (47383)	2579
Seymour, IN (47274)	26164
Sharpsville, IN (46068)	2586
Shelburn, IN (47879)	2481
Shelbyville, IN (46176)	23502
Sheridan, IN (46069)	5814
Shipshewana, IN (46565)	5947
Shirley, IN (47384)	1723
Shoals, IN (47581)	3009
Silver Lake, IN (46982)	2332
Solsberry, IN (47459)	3082
South Bend, IN (46601)	3046
South Bend, IN (46613)	7869
South Bend, IN (46614)	25198
South Bend, IN (46615)	11991
South Bend, IN (46616)	4315
South Bend, IN (46617)	6934
South Bend, IN (46619)	16433
South Bend, IN (46628)	20281
South Bend, IN (46635)	5336
South Bend, IN (46637)	11644
South Whitley, IN (46787)	3260
Spencer, IN (47460)	9730
Spencerville, IN (46788)	2707
Spiceland, IN (47385)	1415
Springport, IN (47386)	1097
Springville, IN (47462)	4075
Star City, IN (46985)	1234
Stilesville, IN (46180)	927
Straughn, IN (47387)	610
Sullivan, IN (47882)	6946
Summitville, IN (46070)	1966
Swayzee, IN (46986)	1748
Switz City, IN (47465)	610
Syracuse, IN (46567)	8139
Tell City, IN (47586)	9522
Terre Haute, IN (47802)	24825
Terre Haute, IN (47803)	16578
Terre Haute, IN (47804)	7906
Terre Haute, IN (47805)	11217
Terre Haute, IN (47807)	7398
Thorntown, IN (46071)	3015
Tippecanoe, IN (46570)	918
Tipton, IN (46072)	7955
Topeka, IN (46571)	4055
Trafalgar, IN (46181)	4209
Troy, IN (47588)	632
Twelve Mile, IN (46988)	739
Union City, IN (47390)	4388
Uniondale, IN (46791)	849
Union Mills, IN (46382)	1869
Unionville, IN (47468)	1157
Upland, IN (46989)	3128
Urbana, IN (46990)	674
Vallonia, IN (47281)	1388
Valparaiso, IN (46383)	30657
Valparaiso, IN (46385)	33544
Van Buren, IN (46991)	1568
Veedersburg, IN (47987)	3447
Velpen, IN (47590)	651
Vincennes, IN (47591)	19907
Wabash, IN (46992)	14178
Wakarusa, IN (46573)	3008
Waldron, IN (46182)	1663
Walkerton, IN (46574)	6780
Walton, IN (46994)	2292
Wanatah, IN (46390)	2472
Warren, IN (46792)	3411
Warsaw, IN (46580)	17807
Warsaw, IN (46582)	10305
Washington, IN (47501)	14222
Waterloo, IN (46793)	3659
Waveland, IN (47989)	1050
Wawaka, IN (46794)	1226
Waynetown, IN (47990)	1491
West Baden Springs, IN (47469)	1579
Westfield, IN (46074)	22252
West Lebanon, IN (47991)	901
Westpoint, IN (47992)	1324
Westport, IN (47283)	3056
West Terre Haute, IN (47885)	7634
Westville, IN (46391)	5233
Wheatfield, IN (46392)	6600
Wheatland, IN (47597)	878
Whiteland, IN (46184)	10100
Whitestown, IN (46075)	2485
Whiting, IN (46394)	9394
Wilkinson, IN (46186)	1548
Williams, IN (47470)	1352
Williamsburg, IN (47393)	1305
Williamsport, IN (47993)	3403
Winamac, IN (46996)	6006
Winchester, IN (47394)	6935
Windfall, IN (46076)	1447
Wingate, IN (47994)	524
Winona Lake, IN (46590)	3712
Winslow, IN (47598)	2754
Wolcott, IN (47995)	1446
Wolcottville, IN (46795)	4926
Woodburn, IN (46797)	3263
Worthington, IN (47471)	2147
Yoder, IN (46798)	1272
Yorktown, IN (47396)	6175
Zionsville, IN (46077)	22068
Addison, MI (49220)	2101
Adrian, MI (49221)	29700
Albion, MI (49224)	9318
Algonac, MI (48001)	10405
Allen, MI (49227)	1128
Allen Park, MI (48101)	24982
Allenton, MI (48002)	2839
Almont, MI (48003)	5301
Ann Arbor, MI (48103)	44859
Ann Arbor, MI (48104)	19845
Ann Arbor, MI (48105)	25072
Ann Arbor, MI (48108)	21112
Ann Arbor, MI (48109)	320
Applegate, MI (48401)	1213
Armada, MI (48005)	4755
Attica, MI (48412)	5052
Avoca, MI (48006)	3423
Bad Axe, MI (48413)	6417
Bancroft, MI (48414)	2073
Belleville, MI (48111)	34112
Birch Run, MI (48415)	8441
Birmingham, MI (48009)	17232
Blissfield, MI (49228)	4843
Bloomfield Hills, MI (48301)	12890
Bloomfield Hills, MI (48302)	14628
Bloomfield Hills, MI (48304)	14725
Brighton, MI (48114)	17927
Brighton, MI (48116)	24136
Britton, MI (49229)	2892
Brooklyn, MI (49230)	9108
Brown City, MI (48416)	4178
Burt, MI (48417)	2470
Byron, MI (48418)	3638
Camden, MI (49232)	2133
Capac, MI (48014)	3639
Carleton, MI (48117)	9029
Carsonville, MI (48419)	2162
Cement City, MI (49233)	2256
Center Line, MI (48015)	6482
Chelsea, MI (48118)	11363
Clarklake, MI (49234)	2391
Clarkston, MI (48346)	19308
Clarkston, MI (48348)	20501
Clawson, MI (48017)	10384
Clayton, MI (49235)	1799
Clinton, MI (49236)	4206
Clio, MI (48420)	18775
Columbiaville, MI (48421)	5737
Concord, MI (49237)	2637
Croswell, MI (48422)	5278
Davisburg, MI (48350)	6321
Davison, MI (48423)	27501
Dearborn, MI (48120)	6439
Melvindale, MI (48122)	8081
Dearborn, MI (48124)	27834
Dearborn, MI (48126)	33320
Dearborn, MI (48128)	9260
Dearborn Heights, MI (48125)	17112
Dearborn Heights, MI (48127)	29726
Decker, MI (48426)	799
Deckerville, MI (48427)	2319
Deerfield, MI (49238)	1455
Detroit, MI (48201)	5381
Detroit, MI (48202)	8794
Highland Park, MI (48203)	17195
Detroit, MI (48204)	17495
Detroit, MI (48205)	28697
Detroit, MI (48206)	12421
Detroit, MI (48207)	11555
Detroit, MI (48208)	5264
Detroit, MI (48209)	21385
Detroit, MI (48210)	18392
Detroit, MI (48211)	4092
Hamtramck, MI (48212)	24163
Detroit, MI (48213)	17255
Detroit, MI (48214)	13128
Detroit, MI (48215)	7950
Detroit, MI (48216)	2900
Detroit, MI (48217)	5019
River Rouge, MI (48218)	5294
Detroit, MI (48219)	32123
Ferndale, MI (48220)	17626
Detroit, MI (48221)	25946
Detroit, MI (48223)	16910
Detroit, MI (48224)	29980
Harper Woods, MI (48225)	11454
Detroit, MI (48226)	2673
Detroit, MI (48227)	29305
Detroit, MI (48228)	33935
Ecorse, MI (48229)	6395
Grosse Pointe, MI (48230)	15022
Detroit, MI (48234)	23901
Detroit, MI (48235)	31279
Grosse Pointe, MI (48236)	27762
Oak Park, MI (48237)	23430
Detroit, MI (48238)	19496
Redford, MI (48239)	29037
Redford, MI (48240)	14577
Dexter, MI (48130)	12687
Dryden, MI (48428)	4339
Dundee, MI (48131)	5737
Durand, MI (48429)	7476
Eastpointe, MI (48021)	25824
Emmett, MI (48022)	2309
Fair Haven, MI (48023)	4422
Farmington, MI (48331)	20379
Farmington, MI (48334)	15493
Farmington, MI (48335)	19642
Farmington, MI (48336)	21693
Fenton, MI (48430)	31424
Flat Rock, MI (48134)	18191
Flint, MI (48502)	565
Flint, MI (48503)	15930
Flint, MI (48504)	20474
Flint, MI (48505)	15571
Flint, MI (48506)	20992
Flint, MI (48507)	22763
Burton, MI (48509)	8434
Burton, MI (48519)	6349
Burton, MI (48529)	7111
Flint, MI (48532)	15352
Flushing, MI (48433)	23338
Fostoria, MI (48435)	1818
Fraser, MI (48026)	12549
Gaines, MI (48436)	3455
Garden City, MI (48135)	23673
Goodells, MI (48027)	2799
Goodrich, MI (48438)	6166
Grand Blanc, MI (48439)	41062
Grass Lake, MI (49240)	7545
Gregory, MI (48137)	4183
Grosse Ile, MI (48138)	9918
Hanover, MI (49241)	2051
Harbor Beach, MI (48441)	3590
Harsens Island, MI (48028)	995
Hartland, MI (48353)	5519
Hazel Park, MI (48030)	12323
Highland, MI (48356)	7394
Highland, MI (48357)	7382
Hillsdale, MI (49242)	10944
Holly, MI (48442)	17107
Homer, MI (49245)	3679
Horton, MI (49246)	2898
Hudson, MI (49247)	4620
Ida, MI (48140)	2855
Imlay City, MI (48444)	7774
Inkster, MI (48141)	17227
Jackson, MI (49201)	31779
Jackson, MI (49202)	14274
Jackson, MI (49203)	28618
Jasper, MI (49248)	787
Jeddo, MI (48032)	2024
Jerome, MI (49249)	2822
Jonesville, MI (49250)	4753
Keego Harbor, MI (48320)	3669
Filion, MI (48432)	584
Kinde, MI (48445)	1181
Lake Orion, MI (48359)	6478
Lake Orion, MI (48360)	9878
Lake Orion, MI (48362)	12952
Lambertville, MI (48144)	9173
Lapeer, MI (48446)	24889
Lennon, MI (48449)	2678
Leonard, MI (48367)	3847
Leslie, MI (49251)	5326
Lexington, MI (48450)	3914
Lincoln Park, MI (48146)	30304
Linden, MI (48451)	12872
Litchfield, MI (49252)	2162
Livonia, MI (48150)	24143
Livonia, MI (48152)	28302
Livonia, MI (48154)	35095
Manchester, MI (48158)	6621
Manitou Beach, MI (49253)	2546
Marine City, MI (48039)	6488
Marlette, MI (48453)	4196
Marysville, MI (48040)	8893
Melvin, MI (48454)	1137
Memphis, MI (48041)	3901
Metamora, MI (48455)	7097
Michigan Center, MI (49254)	2797
Milan, MI (48160)	10600
Milford, MI (48380)	6353
Milford, MI (48381)	11502
Minden City, MI (48456)	791
Palms, MI (48465)	525
Erie, MI (48133)	4859
La Salle, MI (48145)	3136
Luna Pier, MI (48157)	1183
Maybee, MI (48159)	2145
Monroe, MI (48161)	21254
Monroe, MI (48162)	23940
Newport, MI (48166)	9760
Montgomery, MI (49255)	1136
Montrose, MI (48457)	6924
Morenci, MI (49256)	3219
Clinton Township, MI (48035)	28191
Clinton Township, MI (48036)	17601
Clinton Township, MI (48038)	35541
Macomb, MI (48042)	23478
Mount Clemens, MI (48043)	11004
Macomb, MI (48044)	44871
Harrison Township, MI (48045)	20828
Mount Morris, MI (48458)	15858
Munith, MI (49259)	2172
New Baltimore, MI (48047)	33032
New Baltimore, MI (48051)	13716
New Boston, MI (48164)	7987
New Haven, MI (48048)	5809
New Haven, MI (48050)	1503
New Hudson, MI (48165)	5396
New Lothrop, MI (48460)	2069
North Adams, MI (49262)	1018
North Branch, MI (48461)	6935
North Street, MI (48049)	5066
Northville, MI (48167)	20597
Northville, MI (48168)	18684
Novi, MI (48374)	12379
Novi, MI (48375)	18652
Novi, MI (48377)	12404
Onondaga, MI (49264)	1680
Onsted, MI (49265)	4459
Ortonville, MI (48462)	11724
Osseo, MI (49266)	2468
Otisville, MI (48463)	4055
Ottawa Lake, MI (49267)	3610
Otter Lake, MI (48464)	1821
Oxford, MI (48370)	1519
Oxford, MI (48371)	19746
Palmyra, MI (49268)	950
Parma, MI (49269)	4862
Peck, MI (48466)	1330
Petersburg, MI (49270)	5287
Pinckney, MI (48169)	17834
Pittsford, MI (49271)	1859
Pleasant Lake, MI (49272)	2196
Plymouth, MI (48170)	36466
West Bloomfield, MI (48322)	26295
West Bloomfield, MI (48323)	16433
West Bloomfield, MI (48324)	15497
Auburn Hills, MI (48326)	16592
Pontiac, MI (48340)	16520
Pontiac, MI (48341)	10293
Pontiac, MI (48342)	11022
Port Austin, MI (48467)	2010
Port Hope, MI (48468)	1216
Fort Gratiot, MI (48059)	18546
Port Huron, MI (48060)	29832
Port Sanilac, MI (48469)	1113
Reading, MI (49274)	2833
Richmond, MI (48062)	8005
Columbus, MI (48063)	3573
Casco, MI (48064)	3568
Riga, MI (49276)	912
Rives Junction, MI (49277)	2809
Rochester, MI (48306)	24705
Rochester, MI (48307)	34852
Rochester, MI (48309)	24598
Oakland, MI (48363)	4269
Rockwood, MI (48173)	11095
Romeo, MI (48065)	9320
Ray, MI (48096)	3462
Romulus, MI (48174)	24582
Roseville, MI (48066)	38390
Royal Oak, MI (48067)	20103
Pleasant Ridge, MI (48069)	2338
Huntington Woods, MI (48070)	5750
Madison Heights, MI (48071)	23971
Berkley, MI (48072)	13233
Royal Oak, MI (48073)	28318
Ruth, MI (48470)	726
Saline, MI (48176)	18549
Sand Creek, MI (49279)	747
Sandusky, MI (48471)	4712
Smiths Creek, MI (48074)	7771
Snover, MI (48472)	1514
Franklin, MI (48025)	13289
Southfield, MI (48033)	12472
Southfield, MI (48034)	10307
Southfield, MI (48075)	16960
Southfield, MI (48076)	21278
South Lyon, MI (48178)	25398
South Rockwood, MI (48179)	2848
Spring Arbor, MI (49283)	2636
Springport, MI (49284)	2535
East China, MI (48054)	6490
Saint Clair, MI (48079)	10968
Saint Clair Shores, MI (48080)	19581
Saint Clair Shores, MI (48081)	18281
Saint Clair Shores, MI (48082)	14684
Stockbridge, MI (49285)	4912
Swartz Creek, MI (48473)	19851
Taylor, MI (48180)	50527
Tecumseh, MI (49286)	13188
Temperance, MI (48182)	18449
Tipton, MI (49287)	1917
Trenton, MI (48183)	36859
Troy, MI (48083)	19058
Troy, MI (48084)	12967
Troy, MI (48085)	21948
Troy, MI (48098)	19814
Ubly, MI (48475)	2465
Sterling Heights, MI (48310)	35157
Sterling Heights, MI (48312)	28581
Sterling Heights, MI (48313)	29518
Sterling Heights, MI (48314)	17293
Utica, MI (48315)	23605
Utica, MI (48316)	22654
Utica, MI (48317)	21920
Waldron, MI (49288)	1128
Commerce Township, MI (48382)	19589
Walled Lake, MI (48390)	19775
Warren, MI (48088)	19575
Warren, MI (48089)	23021
Warren, MI (48091)	23492
Warren, MI (48092)	21598
Warren, MI (48093)	19852
Washington, MI (48094)	15549
Washington, MI (48095)	4367
Waterford, MI (48327)	18206
Waterford, MI (48328)	19362
Waterford, MI (48329)	22191
White Lake, MI (48383)	10713
White Lake, MI (48386)	14995
Wayne, MI (48184)	13869
Westland, MI (48185)	39266
Westland, MI (48186)	28349
Canton, MI (48187)	42487
Canton, MI (48188)	34181
Whitmore Lake, MI (48189)	11257
Willis, MI (48191)	2979
Wixom, MI (48393)	14033
Wyandotte, MI (48192)	21934
Riverview, MI (48193)	12834
Southgate, MI (48195)	25736
Yale, MI (48097)	4393
Ypsilanti, MI (48197)	43735
Ypsilanti, MI (48198)	28359
Ada, MI (49301)	16822
Afton, MI (49705)	660
Akron, MI (48701)	1130
Alanson, MI (49706)	3763
Alden, MI (49612)	961
Alger, MI (48610)	2624
Allegan, MI (49010)	14231
Allendale, MI (49401)	8596
Alma, MI (48801)	9187
Alpena, MI (49707)	18648
Alto, MI (49302)	6917
Arcadia, MI (49613)	655
Ashley, MI (48806)	1367
Athens, MI (49011)	1862
Atlanta, MI (49709)	2859
Atlantic Mine, MI (49905)	1458
Auburn, MI (48611)	5784
Au Gres, MI (48703)	2759
Augusta, MI (49012)	3124
Au Train, MI (49806)	506
Bailey, MI (49303)	938
Baldwin, MI (49304)	2694
Bangor, MI (49013)	4084
Bannister, MI (48807)	716
Baraga, MI (49908)	1981
Bark River, MI (49807)	2832
Baroda, MI (49101)	2738
Barryton, MI (49305)	1784
Barton City, MI (48705)	420
Bath, MI (48808)	4288
Battle Creek, MI (49014)	16679
Battle Creek, MI (49015)	22475
Battle Creek, MI (49017)	17445
Battle Creek, MI (49037)	14320
Bay City, MI (48706)	34564
Bay City, MI (48708)	21270
Bay Port, MI (48720)	970
Bear Lake, MI (49614)	2285
Beaverton, MI (48612)	7567
Belding, MI (48809)	8802
Bellaire, MI (49615)	3716
Bellevue, MI (49021)	5247
Belmont, MI (49306)	8239
Benton Harbor, MI (49022)	22263
Benzonia, MI (49616)	1808
Berrien Center, MI (49102)	1111
Berrien Springs, MI (49103)	8724
Bessemer, MI (49911)	2196
Beulah, MI (49617)	2853
Big Rapids, MI (49307)	11456
Bitely, MI (49309)	1272
Blanchard, MI (49310)	2279
Bloomingdale, MI (49026)	1727
Boon, MI (49618)	633
Boyne City, MI (49712)	6690
Boyne Falls, MI (49713)	1591
Branch, MI (49402)	1082
Brant, MI (48614)	1120
Breckenridge, MI (48615)	2514
Brethren, MI (49619)	878
Bridgeport, MI (48722)	3016
Bridgman, MI (49106)	3997
Brimley, MI (49715)	2594
Bronson, MI (49028)	5165
Bruce Crossing, MI (49912)	769
Brutus, MI (49716)	660
Buchanan, MI (49107)	8367
Buckley, MI (49620)	2039
Burlington, MI (49029)	1383
Burr Oak, MI (49030)	2020
Byron Center, MI (49315)	17684
Cadillac, MI (49601)	17240
Caledonia, MI (49316)	17102
Calumet, MI (49913)	5571
Carney, MI (49812)	806
Caro, MI (48723)	9750
Carp Lake, MI (49718)	565
Carson City, MI (48811)	2500
Caseville, MI (48725)	2057
Casnovia, MI (49318)	1266
Cass City, MI (48726)	5034
Cassopolis, MI (49031)	6077
Cedar, MI (49621)	2648
Cedar Springs, MI (49319)	13048
Cedarville, MI (49719)	1260
Central Lake, MI (49622)	2182
Centreville, MI (49032)	2413
Ceresco, MI (49033)	1650
Champion, MI (49814)	1098
Charlevoix, MI (49720)	8298
Charlotte, MI (48813)	17851
Chase, MI (49623)	896
Chassell, MI (49916)	2315
Chatham, MI (49816)	659
Cheboygan, MI (49721)	11863
Chesaning, MI (48616)	6441
Clare, MI (48617)	6946
Clarksville, MI (48815)	1989
Clifford, MI (48727)	1009
Climax, MI (49034)	2071
Coldwater, MI (49036)	18378
Coleman, MI (48618)	4372
Coloma, MI (49038)	7664
Colon, MI (49040)	2644
Comstock Park, MI (49321)	13899
Conklin, MI (49403)	2226
Constantine, MI (49042)	4056
Cooks, MI (49817)	502
Coopersville, MI (49404)	7010
Copemish, MI (49625)	1029
Coral, MI (49322)	889
Cornell, MI (49818)	766
Corunna, MI (48817)	5045
Covert, MI (49043)	1657
Crystal, MI (48818)	1831
Crystal Falls, MI (49920)	3287
Curtis, MI (49820)	522
Custer, MI (49405)	1304
Dafter, MI (49724)	1024
Daggett, MI (49821)	1084
Dansville, MI (48819)	2325
Decatur, MI (49045)	4503
Deford, MI (48729)	1251
Delton, MI (49046)	5973
De Tour Village, MI (49725)	612
Dewitt, MI (48820)	14700
Dimondale, MI (48821)	5265
Dorr, MI (49323)	8096
Dowagiac, MI (49047)	11320
Dowling, MI (49050)	1395
Drummond Island, MI (49726)	957
Eagle, MI (48822)	2555
East Jordan, MI (49727)	5850
East Lansing, MI (48823)	27319
East Lansing, MI (48825)	443
East Leroy, MI (49051)	2225
East Tawas, MI (48730)	3876
Eaton Rapids, MI (48827)	13692
Eau Claire, MI (49111)	3454
Edmore, MI (48829)	2495
Edwardsburg, MI (49112)	8379
Union, MI (49130)	1590
Elk Rapids, MI (49629)	2099
Elkton, MI (48731)	1476
Ellsworth, MI (49729)	1249
Elmira, MI (49730)	1674
Elsie, MI (48831)	3025
Elwell, MI (48832)	1146
Empire, MI (49630)	1327
Engadine, MI (49827)	716
Escanaba, MI (49829)	13929
Essexville, MI (48732)	9540
Evart, MI (49631)	4486
Ewen, MI (49925)	501
Fairgrove, MI (48733)	1518
Fairview, MI (48621)	1043
Falmouth, MI (49632)	900
Farwell, MI (48622)	5088
Felch, MI (49831)	660
Fennville, MI (49408)	7155
Fenwick, MI (48834)	1836
Fife Lake, MI (49633)	2855
Fountain, MI (49410)	1366
Fowler, MI (48835)	2238
Fowlerville, MI (48836)	11351
Frankenmuth, MI (48734)	6822
Frankfort, MI (49635)	2913
Frederic, MI (49733)	1366
Freeland, MI (48623)	11109
Freeport, MI (49325)	1732
Free Soil, MI (49411)	1349
Fremont, MI (49412)	9387
Fruitport, MI (49415)	5553
Fulton, MI (49052)	861
Gagetown, MI (48735)	784
Galesburg, MI (49053)	5708
Galien, MI (49113)	1623
Garden, MI (49835)	653
Gaylord, MI (49735)	15067
Germfask, MI (49836)	619
Gladstone, MI (49837)	8702
Gladwin, MI (48624)	12391
Glen Arbor, MI (49636)	624
Glennie, MI (48737)	941
Gobles, MI (49055)	5164
Goetzville, MI (49736)	498
Gowen, MI (49326)	3102
Grand Haven, MI (49417)	25152
Grand Junction, MI (49056)	3030
Grand Ledge, MI (48837)	16490
Grand Rapids, MI (49503)	22041
Grand Rapids, MI (49504)	29137
Grand Rapids, MI (49505)	23814
Grand Rapids, MI (49506)	24510
Grand Rapids, MI (49507)	23888
Grand Rapids, MI (49508)	31228
Wyoming, MI (49509)	22250
Grand Rapids, MI (49512)	12213
Wyoming, MI (49519)	21348
Grand Rapids, MI (49525)	23349
Grand Rapids, MI (49534)	17146
Grand Rapids, MI (49544)	7557
Grand Rapids, MI (49546)	25323
Grand Rapids, MI (49548)	24124
Grandville, MI (49418)	23731
Grant, MI (49327)	6794
Grawn, MI (49637)	2982
Grayling, MI (49738)	7941
Greenbush, MI (48738)	1033
Greenville, MI (48838)	14296
Gulliver, MI (49840)	627
Gwinn, MI (49841)	5127
Hale, MI (48739)	3168
Hamilton, MI (49419)	6837
Hancock, MI (49930)	4781
Harbor Springs, MI (49740)	6424
Harrietta, MI (49638)	682
Harrison, MI (48625)	9643
Harrisville, MI (48740)	1991
Hart, MI (49420)	5171
Hartford, MI (49057)	5214
Haslett, MI (48840)	10635
Hastings, MI (49058)	15617
Hawks, MI (49743)	643
Hemlock, MI (48626)	5473
Henderson, MI (48841)	728
Hermansville, MI (49847)	819
Herron, MI (49744)	745
Hersey, MI (49639)	2070
Hesperia, MI (49421)	4648
Hessel, MI (49745)	841
Hickory Corners, MI (49060)	1566
Hillman, MI (49746)	2861
Holland, MI (49423)	35282
Holland, MI (49424)	37715
Holt, MI (48842)	17796
Holton, MI (49425)	2813
Honor, MI (49640)	1475
Hope, MI (48628)	1529
Hopkins, MI (49328)	3218
Houghton, MI (49931)	4735
Houghton Lake, MI (48629)	6010
Howard City, MI (49329)	6763
Howell, MI (48843)	35835
Howell, MI (48855)	12267
Hubbard Lake, MI (49747)	1525
Hubbardston, MI (48845)	809
Hudsonville, MI (49426)	28748
Idlewild, MI (49642)	480
Indian River, MI (49749)	3668
Interlochen, MI (49643)	5269
Ionia, MI (48846)	12086
Iron Mountain, MI (49801)	10098
Kingsford, MI (49802)	5364
Iron River, MI (49935)	4637
Irons, MI (49644)	1454
Ironwood, MI (49938)	6211
Ishpeming, MI (49849)	10076
Ithaca, MI (48847)	5112
Jenison, MI (49428)	22063
Johannesburg, MI (49751)	1609
Jones, MI (49061)	1361
Kalamazoo, MI (49001)	15484
Portage, MI (49002)	15993
Kalamazoo, MI (49004)	12982
Kalamazoo, MI (49006)	12928
Kalamazoo, MI (49007)	5718
Kalamazoo, MI (49008)	11602
Kalamazoo, MI (49009)	32845
Portage, MI (49024)	24373
Kalamazoo, MI (49048)	18574
Kaleva, MI (49645)	1356
Kalkaska, MI (49646)	6738
Kawkawlin, MI (48631)	4166
Kent City, MI (49330)	4387
Kewadin, MI (49648)	1955
Kingsley, MI (49649)	5310
Kingston, MI (48741)	1709
Lachine, MI (49753)	1636
Laingsburg, MI (48848)	6949
Lake, MI (48632)	3800
Lake Ann, MI (49650)	2679
Lake City, MI (49651)	5998
Lake Leelanau, MI (49653)	1640
Lake Linden, MI (49945)	2085
Lake Odessa, MI (48849)	4944
Lakeview, MI (48850)	3495
Lanse, MI (49946)	3309
Lansing, MI (48906)	19721
Lansing, MI (48910)	25921
Lansing, MI (48911)	30419
Lansing, MI (48912)	12231
Lansing, MI (48915)	6357
Lansing, MI (48917)	26721
Lansing, MI (48933)	1304
Lawrence, MI (49064)	3136
Lawton, MI (49065)	5697
Leland, MI (49654)	774
Leonidas, MI (49066)	570
Leroy, MI (49655)	2461
Levering, MI (49755)	1636
Lewiston, MI (49756)	3231
Lincoln, MI (48742)	1502
Linwood, MI (48634)	3899
Lowell, MI (49331)	13867
Ludington, MI (49431)	14232
Lupton, MI (48635)	1265
Luther, MI (49656)	1230
Luzerne, MI (48636)	702
Lyons, MI (48851)	1968
Mc Bain, MI (49657)	2910
Mc Millan, MI (49853)	1007
Mackinaw City, MI (49701)	1099
Mancelona, MI (49659)	5199
Manistee, MI (49660)	10941
Manistique, MI (49854)	5168
Manton, MI (49663)	4574
Maple City, MI (49664)	1843
Marcellus, MI (49067)	3737
Marenisco, MI (49947)	548
Marion, MI (49665)	3453
Marne, MI (49435)	3158
Marquette, MI (49855)	23966
Marshall, MI (49068)	12659
Martin, MI (49070)	2102
Mason, MI (48854)	15925
Mattawan, MI (49071)	8532
Mayville, MI (48744)	3842
Mears, MI (49436)	1447
Mecosta, MI (49332)	2343
Mendon, MI (49072)	2691
Menominee, MI (49858)	10251
Merrill, MI (48637)	3037
Merritt, MI (49667)	477
Mesick, MI (49668)	2839
Michigamme, MI (49861)	483
Middleton, MI (48856)	793
Middleville, MI (49333)	9708
Midland, MI (48640)	26835
Midland, MI (48642)	27196
Mikado, MI (48745)	1056
Millersburg, MI (49759)	1296
Millington, MI (48746)	7519
Mio, MI (48647)	3345
Mohawk, MI (49950)	985
Montague, MI (49437)	5928
Moran, MI (49760)	623
Morley, MI (49336)	3060
Morrice, MI (48857)	2120
Mount Pleasant, MI (48858)	26098
Muir, MI (48860)	1125
Mulliken, MI (48861)	1462
Munger, MI (48747)	1397
Munising, MI (49862)	3436
Muskegon, MI (49440)	603
Muskegon, MI (49441)	29547
Muskegon, MI (49442)	28709
Muskegon, MI (49444)	18240
Muskegon, MI (49445)	18427
Nashville, MI (49073)	4000
National City, MI (48748)	1460
Naubinway, MI (49762)	543
Negaunee, MI (49866)	6861
Newaygo, MI (49337)	9582
Newberry, MI (49868)	3549
New Buffalo, MI (49117)	3094
New Era, MI (49446)	1898
Niles, MI (49120)	29740
Northport, MI (49670)	1656
Norway, MI (49870)	2890
Nunica, MI (49448)	2865
Oakley, MI (48649)	1505
Okemos, MI (48864)	16361
Olivet, MI (49076)	3277
Omer, MI (48749)	952
Onaway, MI (49765)	3049
Onekama, MI (49675)	998
Ontonagon, MI (49953)	2388
Orleans, MI (48865)	1447
Oscoda, MI (48750)	7173
Ossineke, MI (49766)	2134
Otsego, MI (49078)	7773
Ovid, MI (48866)	4004
Owendale, MI (48754)	820
Owosso, MI (48867)	22924
Paris, MI (49338)	1599
Paw Paw, MI (49079)	11301
Pelkie, MI (49958)	1014
Pellston, MI (49769)	1405
Pentwater, MI (49449)	2354
Perrinton, MI (48871)	1699
Perry, MI (48872)	6386
Petoskey, MI (49770)	14819
Pewamo, MI (48873)	1283
Pickford, MI (49774)	1603
Pierson, MI (49339)	1962
Pigeon, MI (48755)	2936
Pinconning, MI (48650)	6350
Plainwell, MI (49080)	13032
Portland, MI (48875)	8638
Posen, MI (49776)	1566
Potterville, MI (48876)	3389
Powers, MI (49874)	787
Prescott, MI (48756)	3059
Presque Isle, MI (49777)	1437
Prudenville, MI (48651)	3657
Pullman, MI (49450)	2303
Quincy, MI (49082)	5008
Quinnesec, MI (49876)	1117
Rapid City, MI (49676)	2766
Rapid River, MI (49878)	3098
Ravenna, MI (49451)	5145
Reed City, MI (49677)	5118
Reese, MI (48757)	3444
Remus, MI (49340)	2373
Republic, MI (49879)	861
Bentley, MI (48613)	966
Rhodes, MI (48652)	1437
Richland, MI (49083)	6387
Riverdale, MI (48877)	1862
Rock, MI (49880)	888
Rockford, MI (49341)	29358
Rodney, MI (49342)	1241
Rogers City, MI (49779)	3945
Roscommon, MI (48653)	7846
Rosebush, MI (48878)	1351
Rose City, MI (48654)	2012
Rothbury, MI (49452)	1585
Rudyard, MI (49780)	1535
Saginaw, MI (48601)	26197
Saginaw, MI (48602)	21079
Saginaw, MI (48603)	22938
Saginaw, MI (48604)	8209
Saginaw, MI (48607)	871
Saginaw, MI (48609)	11182
Saginaw, MI (48638)	10702
Saint Charles, MI (48655)	5465
Saint Helen, MI (48656)	3072
Saint Ignace, MI (49781)	3729
Beaver Island, MI (49782)	575
Saint Johns, MI (48879)	15165
Saint Joseph, MI (49085)	20883
Saint Louis, MI (48880)	5361
Sand Lake, MI (49343)	4652
Sanford, MI (48657)	6958
Saranac, MI (48881)	4526
Saugatuck, MI (49453)	2429
Sault Sainte Marie, MI (49783)	15048
Kincheloe, MI (49788)	1690
Sawyer, MI (49125)	1706
Schoolcraft, MI (49087)	5556
Scotts, MI (49088)	3473
Scottville, MI (49454)	3847
Sears, MI (49679)	1067
Sebewaing, MI (48759)	2983
Shelby, MI (49455)	4142
Shelbyville, MI (49344)	2861
Shepherd, MI (48883)	6035
Sheridan, MI (48884)	3469
Sherwood, MI (49089)	1412
Sidney, MI (48885)	787
Silverwood, MI (48760)	1040
Six Lakes, MI (48886)	1630
Skandia, MI (49885)	1486
Sodus, MI (49126)	1114
South Boardman, MI (49680)	1603
South Branch, MI (48761)	747
South Haven, MI (49090)	11182
Sparta, MI (49345)	10889
Spring Lake, MI (49456)	15900
Spruce, MI (48762)	1015
Standish, MI (48658)	4221
Stanton, MI (48888)	5074
Stanwood, MI (49346)	4468
Stephenson, MI (49887)	1891
Sterling, MI (48659)	2307
Stevensville, MI (49127)	9597
Sturgis, MI (49091)	15930
Sumner, MI (48889)	1188
Sunfield, MI (48890)	1782
Suttons Bay, MI (49682)	3847
Tawas City, MI (48763)	3972
Tekonsha, MI (49092)	1824
Thompsonville, MI (49683)	1680
Three Oaks, MI (49128)	3129
Three Rivers, MI (49093)	14374
Traverse City, MI (49684)	32444
Traverse City, MI (49685)	852
Traverse City, MI (49686)	27152
Traverse City, MI (49696)	446
Trenary, MI (49891)	549
Trufant, MI (49347)	1081
Turner, MI (48765)	584
Tustin, MI (49688)	2210
Twining, MI (48766)	1067
Twin Lake, MI (49457)	8627
Union City, MI (49094)	3344
Union Pier, MI (49129)	517
Unionville, MI (48767)	1896
Vandalia, MI (49095)	1576
Vanderbilt, MI (49795)	1583
Vassar, MI (48768)	8519
Vermontville, MI (49096)	2678
Vestaburg, MI (48891)	2251
Vicksburg, MI (49097)	9161
Vulcan, MI (49892)	1605
Wakefield, MI (49968)	1622
Walkerville, MI (49459)	1056
Wallace, MI (49893)	1577
Watersmeet, MI (49969)	924
Watervliet, MI (49098)	4796
Wayland, MI (49348)	9993
Webberville, MI (48892)	3864
Weidman, MI (48893)	4421
Wells, MI (49894)	661
Wellston, MI (49689)	1176
West Branch, MI (48661)	8860
West Olive, MI (49460)	7158
Westphalia, MI (48894)	2033
Wetmore, MI (49895)	716
Wheeler, MI (48662)	1293
White Cloud, MI (49349)	6013
Whitehall, MI (49461)	7813
White Pigeon, MI (49099)	4678
Whittemore, MI (48770)	1435
Williamsburg, MI (49690)	5525
Williamston, MI (48895)	9957
Wilson, MI (49896)	1313
Wolverine, MI (49799)	1785
Woodland, MI (48897)	1345
Zeeland, MI (49464)	23443
Antioch, IL (60002)	21271
Apple River, IL (61001)	985
Arlington Heights, IL (60004)	46798
Arlington Heights, IL (60005)	25773
Elk Grove Village, IL (60007)	31802
Rolling Meadows, IL (60008)	20385
Ashton, IL (61006)	1533
Baileyville, IL (61007)	492
Barrington, IL (60010)	40603
Belvidere, IL (61008)	29482
Buffalo Grove, IL (60089)	39466
Byron, IL (61010)	7177
Caledonia, IL (61011)	2701
Capron, IL (61012)	1911
Cary, IL (60013)	24334
Chadwick, IL (61014)	1081
Chana, IL (61015)	892
Cherry Valley, IL (61016)	4719
Crystal Lake, IL (60012)	10180
Crystal Lake, IL (60014)	43312
Dakota, IL (61018)	1006
Davis, IL (61019)	3112
Davis Junction, IL (61020)	2529
Deerfield, IL (60015)	25383
Des Plaines, IL (60016)	51984
Des Plaines, IL (60018)	25293
Dixon, IL (61021)	18516
Durand, IL (61024)	2360
East Dubuque, IL (61025)	4267
Elizabeth, IL (61028)	1785
Evanston, IL (60201)	28744
Evanston, IL (60202)	25691
Evanston, IL (60203)	3859
Forreston, IL (61030)	1963
Fox Lake, IL (60020)	8024
Fox River Grove, IL (60021)	5162
Franklin Grove, IL (61031)	1424
Freeport, IL (61032)	25273
Galena, IL (61036)	6066
Garden Prairie, IL (61038)	1170
German Valley, IL (61039)	756
Glencoe, IL (60022)	7975
Glenview, IL (60025)	36182
Glenview, IL (60026)	11243
Grayslake, IL (60030)	32359
Gurnee, IL (60031)	34042
Hanover, IL (61041)	1176
Harmon, IL (61042)	482
Harvard, IL (60033)	11934
Hebron, IL (60034)	1805
Highland Park, IL (60035)	28252
Highwood, IL (60040)	4259
Ingleside, IL (60041)	8326
Island Lake, IL (60042)	7500
Kenilworth, IL (60043)	2371
Lake Bluff, IL (60044)	8879
Lake Forest, IL (60045)	19270
Lake Villa, IL (60046)	30696
Lake Zurich, IL (60047)	38856
Lanark, IL (61046)	2642
Leaf River, IL (61047)	1556
Lena, IL (61048)	3840
Libertyville, IL (60048)	27042
Lincolnshire, IL (60069)	7647
Lindenwood, IL (61049)	488
Mchenry, IL (60050)	29103
Mchenry, IL (60051)	21238
Milledgeville, IL (61051)	1446
Monroe Center, IL (61052)	1072
Morton Grove, IL (60053)	21139
Mount Carroll, IL (61053)	2525
Mount Morris, IL (61054)	3327
Mount Prospect, IL (60056)	49568
Mundelein, IL (60060)	33334
Vernon Hills, IL (60061)	23581
Northbrook, IL (60062)	37511
North Chicago, IL (60064)	11143
Great Lakes, IL (60088)	3378
Orangeville, IL (61060)	1351
Oregon, IL (61061)	6224
Palatine, IL (60067)	36033
Palatine, IL (60074)	33175
Park Ridge, IL (60068)	34071
Pearl City, IL (61062)	1753
Pecatonica, IL (61063)	3595
Polo, IL (61064)	3304
Poplar Grove, IL (61065)	9106
Prospect Heights, IL (60070)	13923
Richmond, IL (60071)	3275
Ridott, IL (61067)	703
Ringwood, IL (60072)	890
Rochelle, IL (61068)	12360
Rock City, IL (61070)	965
Rock Falls, IL (61071)	12087
Rockford, IL (61101)	15650
Rockford, IL (61102)	14442
Rockford, IL (61103)	18507
Rockford, IL (61104)	12994
Rockford, IL (61107)	25807
Rockford, IL (61108)	24122
Rockford, IL (61109)	22512
Loves Park, IL (61111)	19706
Rockford, IL (61114)	14122
Machesney Park, IL (61115)	19647
Rockton, IL (61072)	10059
Roscoe, IL (61073)	18117
Round Lake, IL (60073)	48769
Savanna, IL (61074)	3840
Scales Mound, IL (61075)	935
Shannon, IL (61078)	1256
Skokie, IL (60076)	29619
Skokie, IL (60077)	22093
South Beloit, IL (61080)	8878
Spring Grove, IL (60081)	8813
Sterling, IL (61081)	18732
Stillman Valley, IL (61084)	2882
Stockton, IL (61085)	2996
Wadsworth, IL (60083)	8248
Warren, IL (61087)	1469
Wauconda, IL (60084)	14627
Waukegan, IL (60085)	52409
Waukegan, IL (60087)	22691
Wheeling, IL (60090)	32722
Wilmette, IL (60091)	25015
Winnebago, IL (61088)	5599
Winnetka, IL (60093)	18384
Winslow, IL (61089)	771
Winthrop Harbor, IL (60096)	6345
Wonder Lake, IL (60097)	9614
Woodstock, IL (60098)	27641
Zion, IL (60099)	24758
Abbotsford, WI (54405)	2501
Abrams, WI (54101)	2449
Adams, WI (53910)	2642
Adell, WI (53001)	1821
Albany, WI (53502)	2097
Algoma, WI (54201)	4577
Allenton, WI (53002)	2104
Almond, WI (54909)	1773
Amberg, WI (54102)	732
Amherst, WI (54406)	3079
Amherst Junction, WI (54407)	1371
Aniwa, WI (54408)	979
Antigo, WI (54409)	11005
Appleton, WI (54911)	21355
Appleton, WI (54913)	15663
Appleton, WI (54914)	25908
Appleton, WI (54915)	36576
Arena, WI (53503)	1623
Argonne, WI (54511)	1154
Argyle, WI (53504)	1786
Arlington, WI (53911)	1209
Arpin, WI (54410)	1858
Athelstane, WI (54104)	842
Athens, WI (54411)	4417
Auburndale, WI (54412)	1887
Avoca, WI (53506)	841
Bagley, WI (53801)	709
Baileys Harbor, WI (54202)	1232
Bancroft, WI (54921)	1242
Baraboo, WI (53913)	17033
Barneveld, WI (53507)	2000
Bear Creek, WI (54922)	1281
Beaver Dam, WI (53916)	19540
Belgium, WI (53004)	2980
Belleville, WI (53508)	4726
Belmont, WI (53510)	1278
Beloit, WI (53511)	38100
Benton, WI (53803)	1098
Berlin, WI (54923)	7417
Big Bend, WI (53103)	3591
Birnamwood, WI (54414)	2839
Black Creek, WI (54106)	4118
Black Earth, WI (53515)	2123
Blanchardville, WI (53516)	1910
Bloomington, WI (53804)	1167
Blue Mounds, WI (53517)	1592
Blue River, WI (53518)	1134
Bonduel, WI (54107)	3343
Boscobel, WI (53805)	3912
Boulder Junction, WI (54512)	1080
Bowler, WI (54416)	1253
Brandon, WI (53919)	2205
Briggsville, WI (53920)	431
Brillion, WI (54110)	4721
Bristol, WI (53104)	4883
Brodhead, WI (53520)	5948
Brookfield, WI (53005)	18831
Brookfield, WI (53045)	20181
Brooklyn, WI (53521)	3334
Brownsville, WI (53006)	1587
Browntown, WI (53522)	1037
Brussels, WI (54204)	1689
Burlington, WI (53105)	24797
Burnett, WI (53922)	916
Butler, WI (53007)	1497
Butternut, WI (54514)	1509
Caledonia, WI (53108)	3039
Cambria, WI (53923)	1857
Cambridge, WI (53523)	4548
Campbellsport, WI (53010)	6886
Cascade, WI (53011)	2029
Casco, WI (54205)	1910
Cassville, WI (53806)	1522
Catawba, WI (54515)	485
Cazenovia, WI (53924)	1161
Cecil, WI (54111)	1887
Cedarburg, WI (53012)	16791
Cedar Grove, WI (53013)	3041
Chili, WI (54420)	1126
Chilton, WI (53014)	6974
Cleveland, WI (53015)	2344
Clinton, WI (53525)	3413
Clintonville, WI (54929)	7331
Cobb, WI (53526)	541
Colby, WI (54421)	2733
Coleman, WI (54112)	1897
Colgate, WI (53017)	5184
Coloma, WI (54930)	1400
Columbus, WI (53925)	6886
Combined Locks, WI (54113)	2991
Conover, WI (54519)	1007
Cottage Grove, WI (53527)	8860
Crandon, WI (54520)	3232
Crivitz, WI (54114)	4436
Cross Plains, WI (53528)	5389
Cuba City, WI (53807)	3705
Cudahy, WI (53110)	15272
Curtiss, WI (54422)	866
Custer, WI (54423)	2092
Dalton, WI (53926)	1107
Dane, WI (53529)	1840
Darien, WI (53114)	2304
Darlington, WI (53530)	3993
Bryant, WI (54418)	1052
Deerbrook, WI (54424)	1494
Deerfield, WI (53531)	3717
De Forest, WI (53532)	12095
Delafield, WI (53018)	6693
Delavan, WI (53115)	13367
Denmark, WI (54208)	5462
De Pere, WI (54115)	34736
Dodgeville, WI (53533)	6231
Dorchester, WI (54425)	1594
Dousman, WI (53118)	6516
Eagle, WI (53119)	4987
Eagle River, WI (54521)	7167
East Troy, WI (53120)	8700
Eden, WI (53019)	1883
Edgar, WI (54426)	3829
Edgerton, WI (53534)	9944
Egg Harbor, WI (54209)	1270
Eland, WI (54427)	964
Elcho, WI (54428)	920
Eldorado, WI (54932)	995
Elkhart Lake, WI (53020)	3320
Elkhorn, WI (53121)	16134
Ellison Bay, WI (54210)	876
Elm Grove, WI (53122)	5744
Elroy, WI (53929)	2237
Endeavor, WI (53930)	1149
Evansville, WI (53536)	7310
Fall River, WI (53932)	2213
Fennimore, WI (53809)	3240
Fifield, WI (54524)	595
Fish Creek, WI (54212)	1020
Florence, WI (54121)	2644
Fond Du Lac, WI (54935)	36472
Fond Du Lac, WI (54937)	13861
Fontana, WI (53125)	1519
Forestville, WI (54213)	1230
Fort Atkinson, WI (53538)	16373
Fox Lake, WI (53933)	2554
Franksville, WI (53126)	6003
Fredonia, WI (53021)	4219
Fremont, WI (54940)	3575
Friendship, WI (53934)	3431
Genoa City, WI (53128)	5977
Germantown, WI (53022)	17426
Gillett, WI (54124)	3266
Gilman, WI (54433)	1412
Gleason, WI (54435)	1848
Glenbeulah, WI (53023)	1247
Glen Flora, WI (54526)	728
Glidden, WI (54527)	914
Goodman, WI (54125)	440
Grafton, WI (53024)	15327
Grand Marsh, WI (53936)	1244
Granton, WI (54436)	1566
Gratiot, WI (53541)	802
Green Bay, WI (54301)	18784
Green Bay, WI (54302)	24078
Green Bay, WI (54303)	20472
Green Bay, WI (54304)	23746
Green Bay, WI (54311)	27745
Green Bay, WI (54313)	33490
Greendale, WI (53129)	12551
Green Lake, WI (54941)	2449
Greenleaf, WI (54126)	3462
Greenville, WI (54942)	7278
Greenwood, WI (54437)	2255
Gresham, WI (54128)	1375
Hales Corners, WI (53130)	6991
Franklin, WI (53132)	29520
Hancock, WI (54943)	1552
Harshaw, WI (54529)	983
Hartford, WI (53027)	19325
Hartland, WI (53029)	18493
Hatley, WI (54440)	2619
Hawkins, WI (54530)	641
Hazel Green, WI (53811)	2687
Hazelhurst, WI (54531)	1278
Helenville, WI (53137)	1472
Highland, WI (53543)	1433
Hilbert, WI (54129)	3165
Hillpoint, WI (53937)	803
Hollandale, WI (53544)	717
Horicon, WI (53032)	4341
Hortonville, WI (54944)	7598
Hubertus, WI (53033)	4862
Hurley, WI (54534)	1996
Hustisford, WI (53034)	1653
Iola, WI (54945)	3077
Irma, WI (54442)	986
Iron Ridge, WI (53035)	2123
Ixonia, WI (53036)	2436
Jackson, WI (53037)	8192
Janesville, WI (53545)	19544
Janesville, WI (53546)	26010
Janesville, WI (53548)	14931
Jefferson, WI (53549)	8830
Johnson Creek, WI (53038)	3374
Juda, WI (53550)	1088
Junction City, WI (54443)	1910
Juneau, WI (53039)	3685
Kansasville, WI (53139)	2554
Kaukauna, WI (54130)	21782
Kenosha, WI (53140)	21042
Kenosha, WI (53142)	27162
Kenosha, WI (53143)	17971
Kenosha, WI (53144)	20705
Keshena, WI (54135)	2191
Kewaskum, WI (53040)	7220
Kewaunee, WI (54216)	5308
Kiel, WI (53042)	6012
Kimberly, WI (54136)	5634
Kohler, WI (53044)	2141
Krakow, WI (54137)	975
Sobieski, WI (54171)	3037
Lac Du Flambeau, WI (54538)	2316
Lake Geneva, WI (53147)	13593
Lake Mills, WI (53551)	7285
Lake Tomahawk, WI (54539)	1192
Lakewood, WI (54138)	866
Lancaster, WI (53813)	5200
Land O Lakes, WI (54540)	1167
Lannon, WI (53046)	979
Laona, WI (54541)	1158
Larsen, WI (54947)	2461
La Valle, WI (53941)	2415
Lena, WI (54139)	2846
Linden, WI (53553)	512
Little Chute, WI (54140)	7526
Little Suamico, WI (54141)	2333
Livingston, WI (53554)	908
Lodi, WI (53555)	7702
Loganville, WI (53943)	934
Lomira, WI (53048)	3005
Lone Rock, WI (53556)	2236
Long Lake, WI (54542)	448
Lowell, WI (53557)	447
Loyal, WI (54446)	2343
Lublin, WI (54447)	446
Luxemburg, WI (54217)	6559
Lyndon Station, WI (53944)	1953
Mc Farland, WI (53558)	9991
Middleton, WI (53562)	21892
Verona, WI (53593)	17746
Madison, WI (53703)	12945
Madison, WI (53704)	37614
Madison, WI (53705)	20296
Madison, WI (53711)	39830
Madison, WI (53713)	17493
Madison, WI (53714)	14039
Madison, WI (53715)	4622
Madison, WI (53716)	16904
Madison, WI (53717)	10564
Madison, WI (53718)	9962
Madison, WI (53719)	24312
Madison, WI (53726)	2908
Madison, WI (53744)	461
Malone, WI (53049)	2247
Manawa, WI (54949)	3041
Manitowish Waters, WI (54545)	837
Manitowoc, WI (54220)	33528
Marathon, WI (54448)	3892
Maribel, WI (54227)	1519
Marinette, WI (54143)	12920
Marion, WI (54950)	2448
Markesan, WI (53946)	3738
Marshall, WI (53559)	5237
Hewitt, WI (54441)	767
Marshfield, WI (54449)	22768
Mauston, WI (53948)	6725
Mayville, WI (53050)	6276
Mazomanie, WI (53560)	3210
Medford, WI (54451)	9722
Mellen, WI (54546)	1037
Menasha, WI (54952)	21502
Menomonee Falls, WI (53051)	32430
Mercer, WI (54547)	1320
Merrill, WI (54452)	16733
Merrimac, WI (53561)	1465
Milladore, WI (54454)	1011
Milton, WI (53563)	9665
Milwaukee, WI (53202)	15593
Milwaukee, WI (53203)	1181
Milwaukee, WI (53204)	26940
Milwaukee, WI (53205)	6125
Milwaukee, WI (53206)	16288
Milwaukee, WI (53207)	29019
Milwaukee, WI (53208)	20642
Milwaukee, WI (53209)	34779
Milwaukee, WI (53210)	18640
Milwaukee, WI (53211)	22723
Milwaukee, WI (53212)	19048
Milwaukee, WI (53213)	22083
Milwaukee, WI (53214)	27867
Milwaukee, WI (53215)	43304
Milwaukee, WI (53216)	23254
Milwaukee, WI (53217)	26784
Milwaukee, WI (53218)	29160
Milwaukee, WI (53219)	28040
Milwaukee, WI (53220)	22062
Milwaukee, WI (53221)	30366
Milwaukee, WI (53222)	20761
Milwaukee, WI (53223)	22220
Milwaukee, WI (53224)	15826
Milwaukee, WI (53225)	19500
Milwaukee, WI (53226)	15838
Milwaukee, WI (53227)	19721
Milwaukee, WI (53228)	13045
Milwaukee, WI (53233)	3853
Saint Francis, WI (53235)	7537
Mineral Point, WI (53565)	4230
Minocqua, WI (54548)	4625
Mishicot, WI (54228)	2500
Monroe, WI (53566)	13670
Montello, WI (53949)	4925
Montfort, WI (53569)	1025
Monticello, WI (53570)	2335
Montreal, WI (54550)	644
Mosinee, WI (54455)	15768
Mountain, WI (54149)	1029
Mount Calvary, WI (53057)	1434
Mount Hope, WI (53816)	646
Mount Horeb, WI (53572)	8648
Mukwonago, WI (53149)	17162
Muscoda, WI (53573)	2607
Muskego, WI (53150)	22907
Nashotah, WI (53058)	3012
Neenah, WI (54956)	37234
Neillsville, WI (54456)	5071
Nekoosa, WI (54457)	7567
Neopit, WI (54150)	607
Neosho, WI (53059)	1637
Neshkoro, WI (54960)	2353
New Franken, WI (54229)	3837
New Glarus, WI (53574)	3436
New Holstein, WI (53061)	4485
New Lisbon, WI (53950)	3606
New London, WI (54961)	12143
Newton, WI (53063)	1484
Niagara, WI (54151)	3100
North Freedom, WI (53951)	2188
North Prairie, WI (53153)	2302
Oak Creek, WI (53154)	29273
Oakfield, WI (53065)	1933
Oconomowoc, WI (53066)	30069
Oconto, WI (54153)	5974
Oconto Falls, WI (54154)	4707
Ogdensburg, WI (54962)	1001
Ogema, WI (54459)	955
Okauchee, WI (53069)	705
Omro, WI (54963)	5976
Oneida, WI (54155)	4667
Oostburg, WI (53070)	4286
Oregon, WI (53575)	13628
Orfordville, WI (53576)	1953
Oshkosh, WI (54901)	23996
Oshkosh, WI (54902)	18650
Oshkosh, WI (54904)	18688
Owen, WI (54460)	1949
Oxford, WI (53952)	2726
Palmyra, WI (53156)	2648
Pardeeville, WI (53954)	6107
Park Falls, WI (54552)	3999
Pelican Lake, WI (54463)	649
Dunbar, WI (54119)	521
Pembine, WI (54156)	1283
Peshtigo, WI (54157)	4866
Pewaukee, WI (53072)	22018
Phelps, WI (54554)	968
Phillips, WI (54555)	4413
Pickerel, WI (54465)	561
Pickett, WI (54964)	1008
Pine River, WI (54965)	1144
Pittsville, WI (54466)	2486
Plain, WI (53577)	1292
Plainfield, WI (54966)	1808
Platteville, WI (53818)	8697
Pleasant Prairie, WI (53158)	13763
Plover, WI (54467)	11702
Plymouth, WI (53073)	12855
Portage, WI (53901)	11733
Port Edwards, WI (54469)	1517
Porterfield, WI (54159)	1257
Port Washington, WI (53074)	11391
Potosi, WI (53820)	2285
Pound, WI (54161)	2380
Poynette, WI (53955)	5207
Prairie Du Chien, WI (53821)	6854
Prairie Du Sac, WI (53578)	5424
Prentice, WI (54556)	1063
Presque Isle, WI (54557)	765
Princeton, WI (54968)	2528
Pulaski, WI (54162)	7731
Racine, WI (53402)	28457
Racine, WI (53403)	20689
Racine, WI (53404)	11319
Racine, WI (53405)	21505
Racine, WI (53406)	22235
Randolph, WI (53956)	2862
Random Lake, WI (53075)	3056
Redgranite, WI (54970)	2376
Reedsburg, WI (53959)	11632
Reedsville, WI (54230)	4030
Reeseville, WI (53579)	1564
Rewey, WI (53580)	495
Rhinelander, WI (54501)	17542
Rib Lake, WI (54470)	1579
Richfield, WI (53076)	3536
Richland Center, WI (53581)	8309
Ridgeway, WI (53582)	983
Ringle, WI (54471)	1697
Rio, WI (53960)	2876
Ripon, WI (54971)	8697
Rock Springs, WI (53961)	716
Rosendale, WI (54974)	1480
Rosholt, WI (54473)	2240
Rothschild, WI (54474)	3679
Rubicon, WI (53078)	1822
Rudolph, WI (54475)	1355
Saint Cloud, WI (53079)	1456
Saint Germain, WI (54558)	2094
Salem, WI (53168)	7434
Sauk City, WI (53583)	5021
Saukville, WI (53080)	5215
Saxon, WI (54559)	538
Sayner, WI (54560)	558
Scandinavia, WI (54977)	1175
Schofield, WI (54476)	15601
Seymour, WI (54165)	6903
Sharon, WI (53585)	1882
Shawano, WI (54166)	13751
Sheboygan, WI (53081)	35407
Sheboygan, WI (53083)	18664
Sheboygan Falls, WI (53085)	10252
Sherwood, WI (54169)	2488
Shiocton, WI (54170)	3364
Shullsburg, WI (53586)	1900
Silver Lake, WI (53170)	2069
Sister Bay, WI (54234)	1671
Slinger, WI (53086)	7406
South Milwaukee, WI (53172)	17557
South Wayne, WI (53587)	1140
Spencer, WI (54479)	3422
Spring Green, WI (53588)	3781
Stetsonville, WI (54480)	1019
Stevens Point, WI (54481)	27473
Stevens Point, WI (54482)	435
Stoughton, WI (53589)	17307
Stratford, WI (54484)	4254
Sturgeon Bay, WI (54235)	15527
Sturtevant, WI (53177)	5784
Suamico, WI (54173)	3685
Sullivan, WI (53178)	2457
Sun Prairie, WI (53590)	31182
Suring, WI (54174)	2530
Sussex, WI (53089)	16831
Theresa, WI (53091)	1872
Thiensville, WI (53092)	19622
Mequon, WI (53097)	4897
Three Lakes, WI (54562)	1804
Tigerton, WI (54486)	1975
Tomahawk, WI (54487)	8650
Tony, WI (54563)	617
Townsend, WI (54175)	953
Trevor, WI (53179)	5072
Twin Lakes, WI (53181)	6246
Two Rivers, WI (54241)	12935
Union Grove, WI (53182)	7498
Unity, WI (54488)	1073
Valders, WI (54245)	2127
Van Dyne, WI (54979)	1426
Vesper, WI (54489)	1357
Wabeno, WI (54566)	1273
Waldo, WI (53093)	1511
Wales, WI (53183)	2731
Walworth, WI (53184)	3654
Washington Island, WI (54246)	685
Waterford, WI (53185)	16655
Waterloo, WI (53594)	4736
Watertown, WI (53094)	15378
Watertown, WI (53098)	10020
New Berlin, WI (53146)	6932
New Berlin, WI (53151)	29852
Waukesha, WI (53186)	27870
Waukesha, WI (53188)	29965
Waukesha, WI (53189)	23540
Waunakee, WI (53597)	15317
Waupaca, WI (54981)	12600
Waupun, WI (53963)	9485
Wausau, WI (54401)	26343
Wausau, WI (54403)	19785
Wausaukee, WI (54177)	2508
Wautoma, WI (54982)	5982
Wauzeka, WI (53826)	1089
West Bend, WI (53090)	18753
West Bend, WI (53095)	24005
Westboro, WI (54490)	759
Westfield, WI (53964)	2955
Weyauwega, WI (54983)	3961
White Lake, WI (54491)	1375
Whitelaw, WI (54247)	2110
Whitewater, WI (53190)	10569
Wild Rose, WI (54984)	2719
Willard, WI (54493)	541
Williams Bay, WI (53191)	2421
Windsor, WI (53598)	2318
Winneconne, WI (54986)	4278
Wisconsin Dells, WI (53965)	9371
Wisconsin Rapids, WI (54494)	23860
Wisconsin Rapids, WI (54495)	6364
Withee, WI (54498)	1748
Wittenberg, WI (54499)	2550
Wonewoc, WI (53968)	1895
Woodruff, WI (54568)	4817
Wrightstown, WI (54180)	2409
Abingdon, IL (61410)	3179
Addison, IL (60101)	32865
Alexis, IL (61412)	1344
Algonquin, IL (60102)	28783
Lake In The Hills, IL (60156)	24751
Alpha, IL (61413)	1021
Altona, IL (61414)	798
Amboy, IL (61310)	3453
Armington, IL (61721)	552
Arrowsmith, IL (61722)	492
Ashkum, IL (60911)	1255
Astoria, IL (61501)	1601
Atlanta, IL (61723)	2146
Aurora, IL (60502)	17619
Aurora, IL (60503)	12502
Aurora, IL (60504)	31035
Aurora, IL (60505)	44855
Aurora, IL (60506)	41447
Avon, IL (61415)	1559
Bartlett, IL (60103)	37918
Streamwood, IL (60107)	34922
Hanover Park, IL (60133)	32187
Batavia, IL (60510)	25687
Beaverville, IL (60912)	464
Beecher, IL (60401)	6792
Bellwood, IL (60104)	16230
Bensenville, IL (60106)	17227
Benson, IL (61516)	633
Berwyn, IL (60402)	49199
Biggsville, IL (61418)	576
Big Rock, IL (60511)	1601
Blandinsville, IL (61420)	961
Bloomingdale, IL (60108)	19903
Bloomington, IL (61701)	27708
Bloomington, IL (61704)	35840
Bloomington, IL (61705)	7033
Blue Island, IL (60406)	19107
Bonfield, IL (60913)	1415
Bourbonnais, IL (60914)	22588
Braceville, IL (60407)	1472
Bradford, IL (61421)	1225
Bradley, IL (60915)	8933
Braidwood, IL (60408)	5188
Brimfield, IL (61517)	3009
Bristol, IL (60512)	1142
Brookfield, IL (60513)	16573
Buckingham, IL (60917)	491
Buckley, IL (60918)	829
Buda, IL (61314)	745
Bushnell, IL (61422)	2870
Cabery, IL (60919)	438
Calumet City, IL (60409)	28882
Cameron, IL (61423)	573
Canton, IL (61520)	12952
Carol Stream, IL (60188)	38160
Carlock, IL (61725)	1398
Carman, IL (61425)	427
Carpentersville, IL (60110)	31502
Channahon, IL (60410)	11286
Chatsworth, IL (60921)	1258
Chebanse, IL (60922)	2107
Chenoa, IL (61726)	2318
Chicago Heights, IL (60411)	43513
Chicago Ridge, IL (60415)	10940
Chillicothe, IL (61523)	9736
Cissna Park, IL (60924)	1455
Clarendon Hills, IL (60514)	8629
Clifton, IL (60927)	1985
Clinton, IL (61727)	8340
Coal City, IL (60416)	8082
Colfax, IL (61728)	1284
Compton, IL (61318)	614
Congerville, IL (61729)	967
Cornell, IL (61319)	1077
Cortland, IL (60112)	3717
Crescent City, IL (60928)	658
Crete, IL (60417)	13457
Cuba, IL (61427)	1944
Cullom, IL (60929)	632
Dahinda, IL (61428)	888
Dalzell, IL (61320)	635
Danforth, IL (60930)	708
Danvers, IL (61732)	1983
Deer Creek, IL (61733)	1017
Dekalb, IL (60115)	27301
Delavan, IL (61734)	2454
Dolton, IL (60419)	18685
Donovan, IL (60931)	562
Downers Grove, IL (60515)	24143
Downers Grove, IL (60516)	26828
Woodridge, IL (60517)	33708
Downs, IL (61736)	1671
Dundee, IL (60118)	14431
Dunlap, IL (61525)	8060
Dwight, IL (60420)	4271
Earlville, IL (60518)	3061
East Galesburg, IL (61430)	709
Edelstein, IL (61526)	1022
Edwards, IL (61528)	2369
Elburn, IL (60119)	8977
Elgin, IL (60120)	41967
Elgin, IL (60123)	40006
Elgin, IL (60124)	15745
Ellsworth, IL (61737)	454
Elmhurst, IL (60126)	39643
Elmwood, IL (61529)	2501
El Paso, IL (61738)	3711
Elwood, IL (60421)	3542
Essex, IL (60935)	944
Eureka, IL (61530)	5354
Fairbury, IL (61739)	4368
Fairview, IL (61432)	613
Farmington, IL (61531)	2898
Flanagan, IL (61740)	1382
Flossmoor, IL (60422)	8664
Forest Park, IL (60130)	11777
Forrest, IL (61741)	1506
Frankfort, IL (60423)	27614
Franklin Park, IL (60131)	15611
Schiller Park, IL (60176)	10063
Galesburg, IL (61401)	24692
Galva, IL (61434)	2788
Gardner, IL (60424)	2043
Geneva, IL (60134)	25644
Genoa, IL (60135)	6190
Gibson City, IL (60936)	3680
Gilberts, IL (60136)	5839
Gilman, IL (60938)	1755
Gilson, IL (61436)	830
Gladstone, IL (61437)	745
Glasford, IL (61533)	2187
Glen Ellyn, IL (60137)	33884
Glendale Heights, IL (60139)	28618
Glenwood, IL (60425)	7370
Goodfield, IL (61742)	973
Good Hope, IL (61438)	651
Grand Ridge, IL (61325)	882
Grant Park, IL (60940)	2875
Granville, IL (61326)	2157
Green Valley, IL (61534)	1543
Gridley, IL (61744)	1789
Groveland, IL (61535)	1536
Hampshire, IL (60140)	12187
Hanna City, IL (61536)	2753
Harvey, IL (60426)	20563
Markham, IL (60428)	8949
Hazel Crest, IL (60429)	12354
Hennepin, IL (61327)	1104
Henry, IL (61537)	2493
Herscher, IL (60941)	1810
Heyworth, IL (61745)	3820
Hinckley, IL (60520)	2570
Hinsdale, IL (60521)	16599
Oak Brook, IL (60523)	9306
Willowbrook, IL (60527)	24636
Darien, IL (60561)	22199
Homewood, IL (60430)	17515
Hoopeston, IL (60942)	4846
Hopedale, IL (61747)	1330
Hudson, IL (61748)	2633
Huntley, IL (60142)	23242
Industry, IL (61440)	687
Ipava, IL (61441)	790
Itasca, IL (60143)	9452
Crest Hill, IL (60403)	13949
Shorewood, IL (60404)	14726
Joliet, IL (60431)	19607
Joliet, IL (60432)	16476
Joliet, IL (60433)	13074
Joliet, IL (60435)	39376
Joliet, IL (60436)	13843
Kankakee, IL (60901)	27849
Keithsburg, IL (61442)	634
Kenney, IL (61749)	487
Kewanee, IL (61443)	11030
Kingston, IL (60145)	2371
Kirkland, IL (60146)	2405
Kirkwood, IL (61447)	875
Knoxville, IL (61448)	3341
Lacon, IL (61540)	2524
Ladd, IL (61329)	1165
La Grange, IL (60525)	27413
La Grange Park, IL (60526)	11281
La Harpe, IL (61450)	1469
La Moille, IL (61330)	1329
Lansing, IL (60438)	24440
La Salle, IL (61301)	8545
Lee, IL (60530)	570
Leland, IL (60531)	1705
Lemont, IL (60439)	20460
Bolingbrook, IL (60440)	44514
Bolingbrook, IL (60490)	16755
Le Roy, IL (61752)	3813
Lewistown, IL (61542)	3084
Lexington, IL (61753)	2690
Lisle, IL (60532)	23725
Little York, IL (61453)	566
Lockport, IL (60441)	29421
Romeoville, IL (60446)	31738
Homer Glen, IL (60491)	20436
Loda, IL (60948)	1309
Lomax, IL (61454)	605
Lombard, IL (60148)	45476
London Mills, IL (61544)	713
Lostant, IL (61334)	647
Lowpoint, IL (61545)	582
Ludlow, IL (60949)	485
Lyons, IL (60534)	8341
Mc Lean, IL (61754)	1183
Mc Nabb, IL (61335)	512
Mackinaw, IL (61755)	4031
Macomb, IL (61455)	12149
Magnolia, IL (61336)	533
Malta, IL (60150)	1538
Manhattan, IL (60442)	8622
Manito, IL (61546)	3744
Manteno, IL (60950)	9882
Maple Park, IL (60151)	3648
Mapleton, IL (61547)	3400
Maquon, IL (61458)	697
Marengo, IL (60152)	11146
Maroa, IL (61756)	2023
Marseilles, IL (61341)	7117
Martinton, IL (60951)	799
Matteson, IL (60443)	16892
Maywood, IL (60153)	18716
Westchester, IL (60154)	15100
Broadview, IL (60155)	6869
Mazon, IL (60444)	1522
Medinah, IL (60157)	2370
Melrose Park, IL (60160)	18523
Hillside, IL (60162)	6793
Berkeley, IL (60163)	4474
Melrose Park, IL (60164)	18328
Stone Park, IL (60165)	3480
Melvin, IL (60952)	574
Mendota, IL (61342)	7691
Metamora, IL (61548)	10670
Midlothian, IL (60445)	21818
Milford, IL (60953)	1936
Minier, IL (61759)	1390
Minonk, IL (61760)	2209
Minooka, IL (60447)	11915
Mokena, IL (60448)	21713
Momence, IL (60954)	5430
Monee, IL (60449)	7750
Monmouth, IL (61462)	9115
Montgomery, IL (60538)	21932
Morris, IL (60450)	18207
Morton, IL (61550)	15680
Naperville, IL (60540)	37518
Naperville, IL (60563)	30415
Naperville, IL (60564)	36024
Naperville, IL (60565)	37904
Neponset, IL (61345)	730
Newark, IL (60541)	2623
New Lenox, IL (60451)	30498
New Windsor, IL (61465)	1108
Normal, IL (61761)	32210
North Aurora, IL (60542)	14541
Oak Forest, IL (60452)	24390
Oak Lawn, IL (60453)	48181
Bridgeview, IL (60455)	13054
Hometown, IL (60456)	3690
Hickory Hills, IL (60457)	11600
Justice, IL (60458)	11295
Burbank, IL (60459)	23868
Oak Park, IL (60301)	1719
Oak Park, IL (60302)	27186
Oak Park, IL (60304)	14806
River Forest, IL (60305)	9672
Odell, IL (60460)	1364
Oglesby, IL (61348)	4100
Ohio, IL (61349)	913
Olympia Fields, IL (60461)	4156
Onarga, IL (60955)	1756
Oneida, IL (61467)	956
Oquawka, IL (61469)	1798
Orland Park, IL (60462)	36061
Orland Park, IL (60467)	23676
Oswego, IL (60543)	30518
Ottawa, IL (61350)	21047
Palos Heights, IL (60463)	13131
Palos Park, IL (60464)	9195
Park Forest, IL (60466)	22014
Paw Paw, IL (61353)	1164
Paxton, IL (60957)	4752
Pekin, IL (61554)	35550
Peoria, IL (61602)	782
Peoria, IL (61603)	12724
Peoria, IL (61604)	24471
Peoria, IL (61605)	11126
Peoria, IL (61606)	3711
Peoria, IL (61607)	9947
Creve Coeur, IL (61610)	4728
East Peoria, IL (61611)	22010
Peoria, IL (61614)	24235
Peoria, IL (61615)	19836
Peoria Heights, IL (61616)	5152
Peotone, IL (60468)	5343
Peru, IL (61354)	9410
Piper City, IL (60959)	884
Plainfield, IL (60544)	23940
Plainfield, IL (60585)	17396
Plainfield, IL (60586)	36924
Plano, IL (60545)	10825
Pontiac, IL (61764)	10677
Posen, IL (60469)	4520
Princeton, IL (61356)	9770
Princeville, IL (61559)	2968
Putnam, IL (61560)	619
Rankin, IL (60960)	815
Ransom, IL (60470)	570
Reddick, IL (60961)	729
Richton Park, IL (60471)	10443
Rio, IL (61472)	593
River Grove, IL (60171)	8701
Riverside, IL (60546)	13886
Roanoke, IL (61561)	2407
Robbins, IL (60472)	3628
Roberts, IL (60962)	427
Roseville, IL (61473)	1433
Rossville, IL (60963)	1465
Saint Anne, IL (60964)	4991
Saint Charles, IL (60174)	28079
Saint Charles, IL (60175)	21951
Sandwich, IL (60548)	10385
Saunemin, IL (61769)	568
Saybrook, IL (61770)	997
Hoffman Estates, IL (60169)	27194
Roselle, IL (60172)	22378
Schaumburg, IL (60173)	10992
Hoffman Estates, IL (60192)	13962
Schaumburg, IL (60193)	35424
Schaumburg, IL (60194)	18724
Schaumburg, IL (60195)	5549
Secor, IL (61771)	793
Seneca, IL (61360)	2987
Serena, IL (60549)	656
Shabbona, IL (60550)	1179
Sheffield, IL (61361)	1268
Sheldon, IL (60966)	1283
Sheridan, IL (60551)	3206
Smithfield, IL (61477)	545
Somonauk, IL (60552)	4017
South Elgin, IL (60177)	19124
South Holland, IL (60473)	18561
Sparland, IL (61565)	1334
Spring Valley, IL (61362)	5185
Stanford, IL (61774)	886
Steger, IL (60475)	8237
Steward, IL (60553)	715
Streator, IL (61364)	16497
Stronghurst, IL (61480)	1149
Sublette, IL (61367)	765
Sugar Grove, IL (60554)	10647
Summit Argo, IL (60501)	8586
Sycamore, IL (60178)	18735
Table Grove, IL (61482)	580
Thornton, IL (60476)	2010
Tinley Park, IL (60477)	36284
Country Club Hills, IL (60478)	13492
Tinley Park, IL (60487)	21960
Tiskilwa, IL (61368)	1283
Toluca, IL (61369)	1429
Tonica, IL (61370)	1233
Topeka, IL (61567)	608
Toulon, IL (61483)	1703
Towanda, IL (61776)	1322
Tremont, IL (61568)	4000
Trivoli, IL (61569)	1099
Union, IL (60180)	1465
Utica, IL (61373)	1899
Varna, IL (61375)	968
Vermont, IL (61484)	733
Verona, IL (60479)	696
Victoria, IL (61485)	541
Villa Park, IL (60181)	25438
Viola, IL (61486)	1358
Walnut, IL (61376)	1915
Wapella, IL (61777)	821
Warrenville, IL (60555)	12327
Washburn, IL (61570)	1572
Washington, IL (61571)	20715
Wataga, IL (61488)	1009
Waterman, IL (60556)	1741
Watseka, IL (60970)	5810
Wayne, IL (60184)	2281
Waynesville, IL (61778)	607
Wenona, IL (61377)	1187
West Brooklyn, IL (61378)	466
West Chicago, IL (60185)	29774
Western Springs, IL (60558)	11800
Westmont, IL (60559)	20758
Wheaton, IL (60187)	33167
Wheaton, IL (60189)	17898
Williamsfield, IL (61489)	787
Willow Springs, IL (60480)	4851
Wilmington, IL (60481)	10277
Winfield, IL (60190)	10080
Wood Dale, IL (60191)	12973
Woodhull, IL (61490)	1037
Palos Hills, IL (60465)	15256
Worth, IL (60482)	9167
Wyanet, IL (61379)	1201
Wyoming, IL (61491)	1841
Yates City, IL (61572)	934
Yorkville, IL (60560)	19311
Chicago, IL (60601)	7785
Chicago, IL (60602)	1657
Chicago, IL (60603)	1676
Chicago, IL (60604)	1192
Chicago, IL (60605)	15279
Chicago, IL (60606)	3110
Chicago, IL (60607)	15670
Chicago, IL (60608)	48270
Chicago, IL (60609)	41819
Chicago, IL (60610)	31564
Chicago, IL (60611)	22612
Chicago, IL (60612)	22624
Chicago, IL (60613)	36974
Chicago, IL (60614)	47140
Chicago, IL (60615)	27024
Chicago, IL (60616)	34744
Chicago, IL (60617)	61529
Chicago, IL (60618)	69391
Chicago, IL (60619)	48410
Chicago, IL (60620)	54534
Chicago, IL (60621)	22622
Chicago, IL (60622)	42176
Chicago, IL (60623)	57725
Chicago, IL (60624)	25492
Chicago, IL (60625)	56729
Chicago, IL (60626)	32581
Chicago, IL (60628)	53827
Chicago, IL (60629)	84106
Chicago, IL (60630)	44993
Chicago, IL (60631)	25301
Chicago, IL (60632)	63860
Chicago, IL (60633)	9538
Chicago, IL (60634)	63211
Chicago, IL (60636)	28682
Chicago, IL (60637)	30689
Chicago, IL (60638)	46470
Chicago, IL (60639)	65832
Chicago, IL (60640)	46688
Chicago, IL (60641)	56207
Chicago, IL (60642)	9637
Chicago, IL (60643)	40433
Chicago, IL (60644)	34236
Chicago, IL (60645)	33583
Chicago, IL (60646)	23311
Chicago, IL (60647)	62570
Chicago, IL (60649)	32247
Chicago, IL (60651)	47832
Chicago, IL (60652)	33721
Chicago, IL (60653)	18765
Chicago, IL (60654)	8539
Chicago, IL (60655)	24364
Chicago, IL (60656)	23812
Chicago, IL (60657)	51214
Chicago, IL (60659)	28547
Chicago, IL (60660)	30796
Chicago, IL (60661)	5726
Harwood Heights, IL (60706)	19711
Elmwood Park, IL (60707)	35121
Lincolnwood, IL (60712)	10969
Niles, IL (60714)	25584
Alsip, IL (60803)	18451
Cicero, IL (60804)	59521
Evergreen Park, IL (60805)	17191
Riverdale, IL (60827)	19042
Addieville, IL (62214)	1052
Albers, IL (62215)	1639
Albion, IL (62806)	2895
Alhambra, IL (62001)	1554
Allendale, IL (62410)	875
Alma, IL (62807)	702
Altamont, IL (62411)	3825
Alton, IL (62002)	25680
Alto Pass, IL (62905)	613
Alvin, IL (61811)	608
Anna, IL (62906)	5760
Arcola, IL (61910)	3744
Arenzville, IL (62611)	927
Argenta, IL (62501)	2340
Arthur, IL (61911)	3742
Ashland, IL (62612)	1679
Ashley, IL (62808)	1259
Ashmore, IL (61912)	1214
Assumption, IL (62510)	1442
Athens, IL (62613)	3489
Atwood, IL (61913)	1496
Auburn, IL (62615)	4870
Augusta, IL (62311)	745
Ava, IL (62907)	1840
Aviston, IL (62216)	2195
Baldwin, IL (62217)	679
Barry, IL (62312)	1708
Bartelso, IL (62218)	1370
Batchtown, IL (62006)	523
Bath, IL (62617)	608
Baylis, IL (62314)	514
Beardstown, IL (62618)	6269
Beecher City, IL (62414)	1562
Belle Rive, IL (62810)	940
Belleville, IL (62220)	16155
Belleville, IL (62221)	22845
Belleville, IL (62223)	15546
Scott Air Force Base, IL (62225)	4091
Belleville, IL (62226)	24404
Bement, IL (61813)	1672
Benld, IL (62009)	1440
Benton, IL (62812)	8744
Bethalto, IL (62010)	9675
Bethany, IL (61914)	1709
Bismarck, IL (61814)	1125
Blue Mound, IL (62513)	1513
Bluffs, IL (62621)	1022
Bluford, IL (62814)	1809
Bonnie, IL (62816)	986
Bowen, IL (62316)	597
Breese, IL (62230)	5579
Bridgeport, IL (62417)	2464
Brighton, IL (62012)	6068
Broadlands, IL (61816)	456
Brocton, IL (61917)	484
Brookport, IL (62910)	2177
Broughton, IL (62817)	472
Browning, IL (62624)	475
Brownstown, IL (62418)	1776
Brussels, IL (62013)	495
Buffalo, IL (62515)	803
Buncombe, IL (62912)	946
Bunker Hill, IL (62014)	3375
Butler, IL (62015)	489
Cairo, IL (62914)	2090
Camargo, IL (61919)	692
Campbell Hill, IL (62916)	800
Camp Point, IL (62320)	1945
Cantrall, IL (62625)	839
Carbondale, IL (62901)	13025
Carbondale, IL (62902)	4030
Carbondale, IL (62903)	2113
Carlinville, IL (62626)	6741
Carlyle, IL (62231)	6234
Carmi, IL (62821)	6190
Carrier Mills, IL (62917)	1881
Carrollton, IL (62016)	3404
Carterville, IL (62918)	7751
Carthage, IL (62321)	3556
Casey, IL (62420)	4031
Caseyville, IL (62232)	5641
Catlin, IL (61817)	2245
Cave In Rock, IL (62919)	697
Centralia, IL (62801)	16349
Cerro Gordo, IL (61818)	1478
Champaign, IL (61820)	13832
Champaign, IL (61821)	24584
Champaign, IL (61822)	18189
Chandlerville, IL (62627)	855
Chapin, IL (62628)	833
Charleston, IL (61920)	13933
Chatham, IL (62629)	11461
Chester, IL (62233)	5205
Chesterfield, IL (62630)	452
Chrisman, IL (61924)	1893
Christopher, IL (62822)	2324
Cisne, IL (62823)	1377
Claremont, IL (62421)	700
Clay City, IL (62824)	1379
Clayton, IL (62324)	1170
Cobden, IL (62920)	2573
Coffeen, IL (62017)	949
Colchester, IL (62326)	2079
Collinsville, IL (62234)	28157
Columbia, IL (62236)	11440
Cottage Hills, IL (62018)	2781
Coulterville, IL (62237)	2191
Cowden, IL (62422)	1012
Creal Springs, IL (62922)	2357
Crossville, IL (62827)	1017
Cutler, IL (62238)	547
Dahlgren, IL (62828)	1209
Dallas City, IL (62330)	1528
Dalton City, IL (61925)	895
Danville, IL (61832)	26283
Tilton, IL (61833)	1764
Danville, IL (61834)	6186
Dawson, IL (62520)	1386
Decatur, IL (62521)	30156
Decatur, IL (62522)	11233
Decatur, IL (62526)	26016
De Land, IL (61839)	545
De Soto, IL (62924)	2135
Dewey, IL (61840)	639
Dieterich, IL (62424)	1898
Divernon, IL (62530)	1391
Dix, IL (62830)	1176
Dongola, IL (62926)	1748
Dorsey, IL (62021)	878
Dow, IL (62022)	1116
Du Bois, IL (62831)	525
Dundas, IL (62425)	550
Dupo, IL (62239)	4029
Du Quoin, IL (62832)	7432
East Alton, IL (62024)	7855
East Carondelet, IL (62240)	1552
Easton, IL (62633)	597
East Saint Louis, IL (62201)	4041
East Saint Louis, IL (62203)	5599
East Saint Louis, IL (62204)	4817
East Saint Louis, IL (62205)	6052
East Saint Louis, IL (62206)	11761
East Saint Louis, IL (62207)	5510
Fairview Heights, IL (62208)	14457
Edgewood, IL (62426)	841
Edinburg, IL (62531)	1634
Edwardsville, IL (62025)	26229
Effingham, IL (62401)	16717
Eldorado, IL (62930)	4593
Eldred, IL (62027)	461
Elizabethtown, IL (62931)	1191
Elkhart, IL (62634)	782
Elkville, IL (62932)	1271
Ellis Grove, IL (62241)	960
Elsah, IL (62028)	856
Emden, IL (62635)	697
Energy, IL (62933)	1024
Enfield, IL (62835)	989
Equality, IL (62934)	776
Evansville, IL (62242)	1301
Ewing, IL (62836)	603
Fairfield, IL (62837)	7469
Fairmount, IL (61841)	1218
Farina, IL (62838)	1381
Farmer City, IL (61842)	2618
Farmersville, IL (62533)	885
Fieldon, IL (62031)	855
Fillmore, IL (62032)	621
Findlay, IL (62534)	1034
Fisher, IL (61843)	2127
Fithian, IL (61844)	930
Flat Rock, IL (62427)	1434
Flora, IL (62839)	5264
Forsyth, IL (62535)	3169
Fowler, IL (62338)	1341
Franklin, IL (62638)	1239
Freeburg, IL (62243)	5263
Fults, IL (62244)	873
Galatia, IL (62935)	1575
Geff, IL (62842)	681
Georgetown, IL (61846)	4006
Germantown, IL (62245)	1605
Gifford, IL (61847)	1124
Gillespie, IL (62033)	3967
Girard, IL (62640)	3126
Glenarm, IL (62536)	894
Glen Carbon, IL (62034)	11624
Godfrey, IL (62035)	14101
Golconda, IL (62938)	2049
Golden, IL (62339)	744
Golden Eagle, IL (62036)	592
Goreville, IL (62939)	2459
Grafton, IL (62037)	1699
Grand Chain, IL (62941)	663
Grand Tower, IL (62942)	508
Granite City, IL (62040)	35688
Grantsburg, IL (62943)	579
Grayville, IL (62844)	1729
Greenfield, IL (62044)	1717
Greenup, IL (62428)	2554
Greenview, IL (62642)	1275
Greenville, IL (62246)	6846
Griggsville, IL (62340)	1410
Hamilton, IL (62341)	2998
Hammond, IL (61929)	663
Hardin, IL (62047)	1324
Harrisburg, IL (62946)	10055
Hartford, IL (62048)	1177
Havana, IL (62644)	4282
Herrick, IL (62431)	1025
Herrin, IL (62948)	9755
Hidalgo, IL (62432)	508
Highland, IL (62249)	13961
Hillsboro, IL (62049)	5540
Hindsboro, IL (61930)	464
Homer, IL (61849)	1644
Hoyleton, IL (62803)	927
Hull, IL (62343)	619
Humboldt, IL (61931)	968
Hutsonville, IL (62433)	841
Illiopolis, IL (62539)	1202
Ina, IL (62846)	535
Indianola, IL (61850)	493
Irving, IL (62051)	739
Iuka, IL (62849)	1820
Jacksonville, IL (62650)	19645
Jerseyville, IL (62052)	10568
Jewett, IL (62436)	557
Johnston City, IL (62951)	4354
Jonesboro, IL (62952)	2746
Junction, IL (62954)	468
Kampsville, IL (62053)	527
Kane, IL (62054)	687
Kansas, IL (61933)	970
Karnak, IL (62956)	722
Kell, IL (62853)	816
Keyesport, IL (62253)	591
Kilbourne, IL (62655)	485
Kinmundy, IL (62854)	1471
Latham, IL (62543)	494
Lawrenceville, IL (62439)	6202
Lebanon, IL (62254)	4411
Lenzburg, IL (62255)	960
Lerna, IL (62440)	1042
Liberty, IL (62347)	2035
Lincoln, IL (62656)	13717
Litchfield, IL (62056)	7390
Loami, IL (62661)	1094
Loraine, IL (62349)	559
Louisville, IL (62858)	2462
Lovington, IL (61937)	1765
Mc Clure, IL (62957)	785
Mc Leansboro, IL (62859)	4344
Macedonia, IL (62860)	470
Macon, IL (62544)	1633
Madison, IL (62060)	3283
Mahomet, IL (61853)	11293
Makanda, IL (62958)	1893
Mansfield, IL (61854)	1367
Marine, IL (62061)	1517
Marion, IL (62959)	21050
Marissa, IL (62257)	2571
Dennison, IL (62423)	643
Marshall, IL (62441)	6204
Martinsville, IL (62442)	2139
Maryville, IL (62062)	6650
Mascoutah, IL (62258)	7924
Mason, IL (62443)	1358
Mason City, IL (62664)	2579
Mattoon, IL (61938)	17984
Mechanicsburg, IL (62545)	1115
Medora, IL (62063)	1056
Mendon, IL (62351)	1613
Meredosia, IL (62665)	1277
Metropolis, IL (62960)	9415
Middletown, IL (62666)	537
Millstadt, IL (62260)	6614
Monticello, IL (61856)	6850
Montrose, IL (62445)	808
Moro, IL (62067)	2152
Morrisonville, IL (62546)	1475
Mound City, IL (62963)	476
Mounds, IL (62964)	1072
Mount Auburn, IL (62547)	687
Mount Carmel, IL (62863)	8443
Mount Olive, IL (62069)	2743
Mount Pulaski, IL (62548)	1967
Mount Sterling, IL (62353)	3073
Mount Vernon, IL (62864)	19699
Mt Zion, IL (62549)	5477
Moweaqua, IL (62550)	2537
Mulberry Grove, IL (62262)	1499
Mulkeytown, IL (62865)	1627
Murphysboro, IL (62966)	12115
Murrayville, IL (62668)	1308
Nashville, IL (62263)	4818
Nauvoo, IL (62354)	1318
Nebo, IL (62355)	644
Neoga, IL (62447)	2870
New Athens, IL (62264)	2924
New Baden, IL (62265)	3656
New Berlin, IL (62670)	2825
New Canton, IL (62356)	478
New Douglas, IL (62074)	928
New Holland, IL (62671)	498
Newman, IL (61942)	1048
Newton, IL (62448)	5182
Niantic, IL (62551)	719
Niota, IL (62358)	602
Noble, IL (62868)	1683
Nokomis, IL (62075)	2868
Norris City, IL (62869)	2312
Oakdale, IL (62268)	692
Oakford, IL (62673)	485
Oakland, IL (61943)	1468
Oakwood, IL (61858)	2760
Oblong, IL (62449)	2722
Odin, IL (62870)	1714
O Fallon, IL (62269)	27358
Ogden, IL (61859)	1172
Okawville, IL (62271)	1916
Olive Branch, IL (62969)	557
Olmsted, IL (62970)	458
Olney, IL (62450)	10050
Omaha, IL (62871)	559
Opdyke, IL (62872)	909
Oreana, IL (62554)	1491
Ozark, IL (62972)	981
Palestine, IL (62451)	1846
Palmyra, IL (62674)	1101
Pana, IL (62557)	5912
Paris, IL (61944)	10511
Patoka, IL (62875)	998
Pawnee, IL (62558)	3170
Payson, IL (62360)	1482
Penfield, IL (61862)	479
Percy, IL (62272)	1258
Pesotum, IL (61863)	786
Petersburg, IL (62675)	5391
Philo, IL (61864)	1600
Pinckneyville, IL (62274)	5263
Pittsburg, IL (62974)	1232
Pittsfield, IL (62363)	4877
Plainville, IL (62365)	508
Pleasant Hill, IL (62366)	1163
Pleasant Plains, IL (62677)	2358
Plymouth, IL (62367)	1049
Pocahontas, IL (62275)	3017
Potomac, IL (61865)	1226
Prairie Du Rocher, IL (62277)	1108
Quincy, IL (62301)	26005
Quincy, IL (62305)	16445
Raleigh, IL (62977)	591
Ramsey, IL (62080)	2064
Rantoul, IL (61866)	11588
Raymond, IL (62560)	1310
Red Bud, IL (62278)	6013
Richview, IL (62877)	467
Ridge Farm, IL (61870)	1092
Ridgway, IL (62979)	1072
Riverton, IL (62561)	4698
Robinson, IL (62454)	8830
Rochester, IL (62563)	5440
Roodhouse, IL (62082)	2311
Rosiclare, IL (62982)	856
Roxana, IL (62084)	1316
Royalton, IL (62983)	1235
Rushville, IL (62681)	4479
Sadorus, IL (61872)	696
Saint Elmo, IL (62458)	1890
Saint Francisville, IL (62460)	992
Saint Jacob, IL (62281)	2134
Saint Joseph, IL (61873)	5582
Saint Peter, IL (62880)	629
Salem, IL (62881)	9380
Sandoval, IL (62882)	1860
San Jose, IL (62682)	819
Savoy, IL (61874)	5179
Scheller, IL (62883)	551
Sesser, IL (62884)	2385
Seymour, IL (61875)	680
Shawneetown, IL (62984)	1326
Shelbyville, IL (62565)	6411
Sherman, IL (62684)	4514
Shipman, IL (62685)	1729
Shobonier, IL (62885)	723
Shumway, IL (62461)	790
Sidell, IL (61876)	705
Sidney, IL (61877)	1500
Sigel, IL (62462)	1082
Simpson, IL (62985)	722
Smithboro, IL (62284)	481
Smithton, IL (62285)	3984
Sorento, IL (62086)	1176
South Roxana, IL (62087)	1547
Sparta, IL (62286)	4928
Springfield, IL (62701)	509
Springfield, IL (62702)	28847
Springfield, IL (62703)	21928
Springfield, IL (62704)	33869
Springfield, IL (62707)	7550
Springfield, IL (62711)	13944
Springfield, IL (62712)	8964
Staunton, IL (62088)	5808
Steeleville, IL (62288)	2533
Stewardson, IL (62463)	1097
Stonefort, IL (62987)	960
Stonington, IL (62567)	1041
Strasburg, IL (62465)	815
Sullivan, IL (61951)	6646
Sumner, IL (62466)	2101
Tallula, IL (62688)	687
Tamaroa, IL (62888)	1733
Tamms, IL (62988)	1242
Taylorville, IL (62568)	12674
Teutopolis, IL (62467)	3537
Texico, IL (62889)	759
Thebes, IL (62990)	841
Thomasboro, IL (61878)	1360
Thompsonville, IL (62890)	2171
Toledo, IL (62468)	2183
Tolono, IL (61880)	3725
Tower Hill, IL (62571)	1267
Trenton, IL (62293)	4136
Troy, IL (62294)	12382
Tuscola, IL (61953)	5541
Ullin, IL (62992)	738
Urbana, IL (61801)	14473
Urbana, IL (61802)	14743
Ursa, IL (62376)	1049
Valmeyer, IL (62295)	1311
Vandalia, IL (62471)	7261
Venice, IL (62090)	747
Vergennes, IL (62994)	600
Versailles, IL (62378)	785
Vienna, IL (62995)	3135
Villa Grove, IL (61956)	2512
Villa Ridge, IL (62996)	501
Virden, IL (62690)	3338
Virginia, IL (62691)	2119
Waggoner, IL (62572)	514
Walnut Hill, IL (62893)	892
Waltonville, IL (62894)	844
Warrensburg, IL (62573)	1374
Warsaw, IL (62379)	1792
Waterloo, IL (62298)	15025
Watson, IL (62473)	1210
Waverly, IL (62692)	1759
Wayne City, IL (62895)	1729
Weldon, IL (61882)	590
Westfield, IL (62474)	700
West Frankfort, IL (62896)	9625
West Salem, IL (62476)	1440
West Union, IL (62477)	776
Westville, IL (61883)	3804
Wheeler, IL (62479)	762
White Hall, IL (62092)	2208
White Heath, IL (61884)	1172
Williamsville, IL (62693)	1609
Willow Hill, IL (62480)	634
Winchester, IL (62694)	2757
Gays, IL (61928)	645
Windsor, IL (61957)	1600
Witt, IL (62094)	944
Woodlawn, IL (62898)	1741
Wood River, IL (62095)	9126
Worden, IL (62097)	2520
Xenia, IL (62899)	1377
Zeigler, IL (62999)	1263
Alexandria, MO (63430)	500
Armstrong, MO (65230)	556
Arnold, MO (63010)	30888
Ashland, MO (65010)	4886
Atlanta, MO (63530)	763
Augusta, MO (63332)	1267
Auxvasse, MO (65231)	2718
Ballwin, MO (63011)	32893
Ballwin, MO (63021)	50402
Barnett, MO (65011)	1615
Barnhart, MO (63012)	9017
Beaufort, MO (63013)	1449
Belle, MO (65013)	2639
Bellflower, MO (63333)	632
Berger, MO (63014)	687
Bevier, MO (63532)	1082
Blackwater, MO (65322)	506
Bland, MO (65014)	1763
Bonnots Mill, MO (65016)	1124
Boonville, MO (65233)	8691
Bowling Green, MO (63334)	5159
Brashear, MO (63533)	679
Brumley, MO (65017)	1145
Brunswick, MO (65236)	1106
Bunceton, MO (65237)	781
Cairo, MO (65239)	1172
Calhoun, MO (65323)	730
California, MO (65018)	6330
Callao, MO (63534)	650
Camdenton, MO (65020)	11399
Canton, MO (63435)	2821
Catawissa, MO (63015)	1866
Cedar Hill, MO (63016)	6849
Center, MO (63436)	990
Centertown, MO (65023)	1612
Centralia, MO (65240)	6330
Chamois, MO (65024)	923
Chesterfield, MO (63005)	16614
Chesterfield, MO (63017)	37018
Clarence, MO (63437)	1261
Clark, MO (65243)	1906
Clarksburg, MO (65025)	626
Clarksville, MO (63336)	959
Climax Springs, MO (65324)	1055
Cole Camp, MO (65325)	2531
Columbia, MO (65201)	19290
Columbia, MO (65202)	34973
Columbia, MO (65203)	42430
Crystal City, MO (63019)	3688
Curryville, MO (63339)	779
Defiance, MO (63341)	3278
De Soto, MO (63020)	16765
Dittmer, MO (63023)	4190
Downing, MO (63536)	615
Edina, MO (63537)	1501
Edwards, MO (65326)	1398
Eldon, MO (65026)	8807
Rocky Mount, MO (65072)	1311
Elsberry, MO (63343)	3572
Eolia, MO (63344)	1351
Eugene, MO (65032)	1457
Eureka, MO (63025)	12462
Ewing, MO (63440)	1136
Excello, MO (65247)	465
Fayette, MO (65248)	3271
Fenton, MO (63026)	38665
Festus, MO (63028)	21809
Florissant, MO (63031)	40192
Florissant, MO (63033)	35384
Florissant, MO (63034)	16252
Foley, MO (63347)	2497
Foristell, MO (63348)	5470
Fortuna, MO (65034)	459
Frankford, MO (63441)	948
Franklin, MO (65250)	529
Freeburg, MO (65035)	1494
French Village, MO (63036)	801
Fulton, MO (65251)	15601
Gerald, MO (63037)	2653
Glasgow, MO (65254)	1445
Glencoe, MO (63038)	6362
Gravois Mills, MO (65037)	3464
Gray Summit, MO (63039)	790
Green Castle, MO (63544)	640
Green City, MO (63545)	878
Green Ridge, MO (65332)	1243
Greentop, MO (63546)	1262
Grover, MO (63040)	7349
Hallsville, MO (65255)	3341
Hannibal, MO (63401)	17161
Harrisburg, MO (65256)	1611
Hartsburg, MO (65039)	1960
Hawk Point, MO (63349)	1642
Hazelwood, MO (63042)	16521
Maryland Heights, MO (63043)	19136
Bridgeton, MO (63044)	9095
Henley, MO (65040)	1078
Herculaneum, MO (63048)	2658
Hermann, MO (65041)	4808
Higbee, MO (65257)	1338
High Ridge, MO (63049)	14290
Hillsboro, MO (63050)	13130
Holts Summit, MO (65043)	8226
House Springs, MO (63051)	11892
Houstonia, MO (65333)	660
Hughesville, MO (65334)	748
Huntsville, MO (65259)	2282
Imperial, MO (63052)	22817
Jacksonville, MO (65260)	519
Jamestown, MO (65046)	987
Jefferson City, MO (65101)	22034
Jefferson City, MO (65109)	31959
Jonesburg, MO (63351)	1512
Kahoka, MO (63445)	3213
Kaiser, MO (65047)	969
Keytesville, MO (65261)	886
Kingdom City, MO (65262)	755
Kirksville, MO (63501)	13378
Whiteman Air Force Base, MO (65305)	2098
Knob Noster, MO (65336)	4822
Knox City, MO (63446)	512
Labadie, MO (63055)	2128
La Belle, MO (63447)	802
Laddonia, MO (63352)	914
La Grange, MO (63448)	1316
Lake Ozark, MO (65049)	5932
La Monte, MO (65337)	1642
Lancaster, MO (63548)	1036
La Plata, MO (63549)	1962
Leslie, MO (63056)	1722
Lewistown, MO (63452)	918
Lincoln, MO (65338)	2297
Linn, MO (65051)	3750
Linn Creek, MO (65052)	2683
Lohman, MO (65053)	1297
Lonedell, MO (63060)	1913
Loose Creek, MO (65054)	782
Louisiana, MO (63353)	3710
Macon, MO (63552)	6457
Madison, MO (65263)	1538
Malta Bend, MO (65339)	549
Marshall, MO (65340)	11859
Marthasville, MO (63357)	4788
Martinsburg, MO (65264)	710
Maywood, MO (63454)	815
Memphis, MO (63555)	2519
Meta, MO (65058)	938
Mexico, MO (65265)	12402
Middletown, MO (63359)	1168
Milan, MO (63556)	2856
Moberly, MO (65270)	12465
Mokane, MO (65059)	740
Monroe City, MO (63456)	3486
Montgomery City, MO (63361)	3619
Morrison, MO (65061)	609
Moscow Mills, MO (63362)	5071
Nelson, MO (65347)	542
New Bloomfield, MO (65063)	2892
New Cambria, MO (63558)	622
New Florence, MO (63363)	1323
New Franklin, MO (65274)	1366
New Haven, MO (63068)	4190
New London, MO (63459)	3489
Novinger, MO (63559)	1096
O Fallon, MO (63366)	41184
Lake Saint Louis, MO (63367)	16536
O Fallon, MO (63368)	35097
Old Monroe, MO (63369)	1976
Olean, MO (65064)	494
Osage Beach, MO (65065)	5184
Otterville, MO (65348)	1051
Owensville, MO (65066)	5424
Pacific, MO (63069)	11972
Palmyra, MO (63461)	4885
Paris, MO (65275)	2044
Perry, MO (63462)	1314
Pevely, MO (63070)	5406
Philadelphia, MO (63463)	537
Pilot Grove, MO (65276)	1304
Portage Des Sioux, MO (63373)	575
Prairie Home, MO (65068)	618
Queen City, MO (63561)	909
Rhineland, MO (65069)	601
Richwoods, MO (63071)	805
Robertsville, MO (63072)	2868
Rocheport, MO (65279)	1591
Rosebud, MO (63091)	1187
Russellville, MO (65074)	2550
Saint Ann, MO (63074)	12586
Saint Charles, MO (63301)	37910
Saint Charles, MO (63303)	39592
Saint Charles, MO (63304)	36489
Saint Clair, MO (63077)	9514
Saint Elizabeth, MO (65075)	696
Saint Louis, MO (63101)	1891
Saint Louis, MO (63102)	1002
Saint Louis, MO (63103)	3466
Saint Louis, MO (63104)	12834
Saint Louis, MO (63105)	12133
Saint Louis, MO (63106)	6439
Saint Louis, MO (63107)	7324
Saint Louis, MO (63108)	11066
Saint Louis, MO (63109)	22921
Saint Louis, MO (63110)	11920
Saint Louis, MO (63111)	13491
Saint Louis, MO (63112)	13186
Saint Louis, MO (63113)	8304
Saint Louis, MO (63114)	28958
Saint Louis, MO (63115)	14431
Saint Louis, MO (63116)	33439
Saint Louis, MO (63117)	7856
Saint Louis, MO (63118)	17087
Saint Louis, MO (63119)	28606
Saint Louis, MO (63120)	6483
Saint Louis, MO (63121)	19923
Saint Louis, MO (63122)	34584
Saint Louis, MO (63123)	43701
Saint Louis, MO (63124)	9209
Saint Louis, MO (63125)	26977
Saint Louis, MO (63126)	13964
Saint Louis, MO (63127)	4688
Saint Louis, MO (63128)	27038
Saint Louis, MO (63129)	48033
Saint Louis, MO (63130)	23019
Saint Louis, MO (63131)	16193
Saint Louis, MO (63132)	11820
Saint Louis, MO (63133)	5440
Saint Louis, MO (63134)	10420
Saint Louis, MO (63135)	16509
Saint Louis, MO (63136)	36386
Saint Louis, MO (63137)	15079
Saint Louis, MO (63138)	15187
Saint Louis, MO (63139)	18440
Saint Louis, MO (63141)	18236
Saint Louis, MO (63143)	7566
Saint Louis, MO (63144)	7549
Saint Louis, MO (63146)	24912
Saint Louis, MO (63147)	7834
Saint Peters, MO (63376)	63056
Saint Thomas, MO (65076)	604
Salisbury, MO (65281)	2532
Sedalia, MO (65301)	25948
Shelbina, MO (63468)	2272
Bethel, MO (63434)	479
Shelbyville, MO (63469)	1032
Silex, MO (63377)	1876
Slater, MO (65349)	1914
Smithton, MO (65350)	1471
Stover, MO (65078)	2694
Sturgeon, MO (65284)	1882
Sullivan, MO (63080)	10940
Sunrise Beach, MO (65079)	3514
Sweet Springs, MO (65351)	1882
Syracuse, MO (65354)	494
Taylor, MO (63471)	525
Tebbetts, MO (65080)	837
Thompson, MO (65285)	553
Tipton, MO (65081)	2425
Troy, MO (63379)	19199
Tuscumbia, MO (65082)	862
Union, MO (63084)	14489
Unionville, MO (63565)	2992
Valles Mines, MO (63087)	832
Valley Park, MO (63088)	6639
Vandalia, MO (63382)	2893
Versailles, MO (65084)	4925
Villa Ridge, MO (63089)	5202
Warrenton, MO (63383)	12737
Warsaw, MO (65355)	7658
Washington, MO (63090)	19208
Wellsville, MO (63384)	1502
Wentzville, MO (63385)	29286
West Alton, MO (63386)	484
Westphalia, MO (65085)	1152
Williamsburg, MO (63388)	626
Windsor, MO (65360)	3529
Winfield, MO (63389)	5164
Wright City, MO (63390)	7974
Washington, DC (20001)	24117
Washington, DC (20002)	36260
Washington, DC (20003)	17237
Washington, DC (20004)	1298
Washington, DC (20005)	8862
Washington, DC (20006)	1044
Washington, DC (20007)	17924
Washington, DC (20008)	22011
Washington, DC (20009)	35214
Washington, DC (20010)	21381
Washington, DC (20011)	46009
Washington, DC (20012)	10678
Washington, DC (20015)	13357
Washington, DC (20016)	22826
Washington, DC (20017)	12242
Washington, DC (20018)	12041
Washington, DC (20019)	36915
Washington, DC (20020)	34165
Washington, DC (20024)	8265
Washington, DC (20032)	23556
Washington, DC (20036)	4479
Washington, DC (20037)	5661
Accokeek, MD (20607)	8377
Aquasco, MD (20608)	722
Ashton, MD (20861)	1811
Avenue, MD (20609)	940
Bel Alton, MD (20611)	951
Beltsville, MD (20705)	21122
Bethesda, MD (20814)	22685
Chevy Chase, MD (20815)	24927
Bethesda, MD (20816)	13948
Bethesda, MD (20817)	31025
Bladensburg, MD (20710)	6493
Bowie, MD (20715)	21792
Bowie, MD (20716)	17493
Bowie, MD (20720)	17823
Bowie, MD (20721)	22471
Boyds, MD (20841)	7969
Brandywine, MD (20613)	10256
Brentwood, MD (20722)	4676
Brookeville, MD (20833)	6945
Bryans Road, MD (20616)	4871
Bryantown, MD (20617)	903
Burtonsville, MD (20866)	11721
Bushwood, MD (20618)	616
Cabin John, MD (20818)	1588
California, MD (20619)	8705
Callaway, MD (20620)	1254
Capitol Heights, MD (20743)	29683
District Heights, MD (20747)	30726
Chaptico, MD (20621)	1312
Charlotte Hall, MD (20622)	3891
Cheltenham, MD (20623)	2531
Chesapeake Beach, MD (20732)	8400
Churchton, MD (20733)	2606
Clarksburg, MD (20871)	10531
Clements, MD (20624)	1077
Clinton, MD (20735)	30519
College Park, MD (20740)	15633
Damascus, MD (20872)	11276
Dameron, MD (20628)	556
Deale, MD (20751)	1944
Dickerson, MD (20842)	1511
Dunkirk, MD (20754)	6409
Fort George G Meade, MD (20755)	6733
Fort Washington, MD (20744)	41540
Oxon Hill, MD (20745)	20874
Friendship, MD (20758)	746
Fulton, MD (20759)	2725
Gaithersburg, MD (20877)	26800
Gaithersburg, MD (20878)	52924
Gaithersburg, MD (20879)	21332
Gaithersburg, MD (20882)	12565
Montgomery Village, MD (20886)	27103
Germantown, MD (20874)	48336
Germantown, MD (20876)	20992
Glenn Dale, MD (20769)	5725
Great Mills, MD (20634)	5941
Greenbelt, MD (20770)	18966
Harwood, MD (20776)	2800
Highland, MD (20777)	3036
Hollywood, MD (20636)	8431
Hughesville, MD (20637)	4794
Huntingtown, MD (20639)	12778
Hyattsville, MD (20781)	8985
Hyattsville, MD (20782)	23691
Hyattsville, MD (20783)	29484
Hyattsville, MD (20784)	24037
Hyattsville, MD (20785)	27933
Indian Head, MD (20640)	7882
Issue, MD (20645)	744
Jessup, MD (20794)	7418
Kensington, MD (20895)	16190
Lanham, MD (20706)	31002
La Plata, MD (20646)	16450
Laurel, MD (20707)	26214
Laurel, MD (20708)	19398
Laurel, MD (20723)	24130
Laurel, MD (20724)	12891
Leonardtown, MD (20650)	10513
Lexington Park, MD (20653)	16545
Lothian, MD (20711)	5488
Lusby, MD (20657)	16379
Marbury, MD (20658)	1028
Mechanicsville, MD (20659)	19456
Mount Rainier, MD (20712)	6569
Nanjemoy, MD (20662)	2187
Newburg, MD (20664)	2300
North Beach, MD (20714)	3488
Olney, MD (20832)	21823
Owings, MD (20736)	7915
Park Hall, MD (20667)	533
Patuxent River, MD (20670)	873
Piney Point, MD (20674)	643
Pomfret, MD (20675)	1515
Poolesville, MD (20837)	5273
Port Republic, MD (20676)	2964
Port Tobacco, MD (20677)	2081
Prince Frederick, MD (20678)	9060
Ridge, MD (20680)	794
Riverdale, MD (20737)	15681
Rockville, MD (20850)	37165
Rockville, MD (20851)	11459
Rockville, MD (20852)	32220
Rockville, MD (20853)	26064
Potomac, MD (20854)	44511
Derwood, MD (20855)	13190
Saint Inigoes, MD (20684)	902
Saint Leonard, MD (20685)	5780
Sandy Spring, MD (20860)	1485
Savage, MD (20763)	2285
Shady Side, MD (20764)	3585
Silver Spring, MD (20901)	29903
Silver Spring, MD (20902)	39168
Silver Spring, MD (20903)	17654
Silver Spring, MD (20904)	44859
Silver Spring, MD (20905)	16516
Silver Spring, MD (20906)	53137
Silver Spring, MD (20910)	30661
Takoma Park, MD (20912)	19175
Solomons, MD (20688)	1920
Spencerville, MD (20868)	651
Sunderland, MD (20689)	1516
Tall Timbers, MD (20690)	671
Suitland, MD (20746)	22404
Temple Hills, MD (20748)	30423
Andrews Air Force Base, MD (20762)	2572
Tracys Landing, MD (20779)	1160
Upper Marlboro, MD (20772)	34695
Upper Marlboro, MD (20774)	35509
Valley Lee, MD (20692)	1054
Waldorf, MD (20601)	20090
Waldorf, MD (20602)	18650
Waldorf, MD (20603)	22217
Welcome, MD (20693)	1079
West River, MD (20778)	1676
White Plains, MD (20695)	7316
Aberdeen, MD (21001)	18383
Aberdeen Proving Ground, MD (21005)	1142
Abingdon, MD (21009)	25308
Accident, MD (21520)	1675
Adamstown, MD (21710)	3830
Annapolis, MD (21401)	30595
Annapolis, MD (21403)	25015
Annapolis, MD (21405)	555
Annapolis, MD (21409)	16232
Annapolis, MD (21402)	1657
Arnold, MD (21012)	18695
Baldwin, MD (21013)	4382
Baltimore, MD (21201)	9628
Baltimore, MD (21202)	10448
Towson, MD (21204)	12824
Baltimore, MD (21205)	9645
Baltimore, MD (21206)	38796
Gwynn Oak, MD (21207)	36682
Pikesville, MD (21208)	28007
Baltimore, MD (21209)	20922
Baltimore, MD (21210)	9266
Baltimore, MD (21211)	11927
Baltimore, MD (21212)	25043
Baltimore, MD (21213)	22290
Baltimore, MD (21214)	15609
Baltimore, MD (21215)	40096
Baltimore, MD (21216)	20336
Baltimore, MD (21217)	20560
Baltimore, MD (21218)	30285
Sparrows Point, MD (21219)	8039
Middle River, MD (21220)	31809
Essex, MD (21221)	33943
Dundalk, MD (21222)	44123
Baltimore, MD (21223)	15504
Baltimore, MD (21224)	33150
Brooklyn, MD (21225)	22734
Curtis Bay, MD (21226)	5435
Halethorpe, MD (21227)	26627
Catonsville, MD (21228)	39088
Baltimore, MD (21229)	33786
Baltimore, MD (21230)	23055
Baltimore, MD (21231)	9885
Parkville, MD (21234)	56528
Nottingham, MD (21236)	33445
Rosedale, MD (21237)	24396
Baltimore, MD (21239)	22147
Windsor Mill, MD (21244)	27753
Towson, MD (21286)	15367
Barton, MD (21521)	1050
Bel Air, MD (21014)	31074
Bel Air, MD (21015)	24922
Belcamp, MD (21017)	5504
Berlin, MD (21811)	18797
Big Pool, MD (21711)	842
Bishopville, MD (21813)	2464
Boonsboro, MD (21713)	8094
Brunswick, MD (21716)	4121
Knoxville, MD (21758)	4028
Cambridge, MD (21613)	13673
Cascade, MD (21719)	1331
Centreville, MD (21617)	8123
Chesapeake City, MD (21915)	2604
Chester, MD (21619)	5115
Chestertown, MD (21620)	9594
Church Creek, MD (21622)	441
Church Hill, MD (21623)	1457
Churchville, MD (21028)	2971
Clarksville, MD (21029)	10412
Clear Spring, MD (21722)	5046
Cockeysville, MD (21030)	20714
Colora, MD (21917)	2256
Columbia, MD (21044)	34780
Columbia, MD (21045)	32742
Columbia, MD (21046)	13087
Conowingo, MD (21918)	3628
Cordova, MD (21625)	2130
Crisfield, MD (21817)	3900
Crofton, MD (21114)	21751
Crownsville, MD (21032)	7811
Cumberland, MD (21502)	29642
Darlington, MD (21034)	3086
Davidsonville, MD (21035)	7106
Dayton, MD (21036)	1875
Deal Island, MD (21821)	826
Denton, MD (21629)	7338
Earleville, MD (21919)	2486
East New Market, MD (21631)	2308
Easton, MD (21601)	19388
Eden, MD (21822)	2353
Edgewater, MD (21037)	17576
Edgewood, MD (21040)	19332
Elkton, MD (21921)	33457
Ellicott City, MD (21042)	34548
Ellicott City, MD (21043)	34351
Emmitsburg, MD (21727)	3730
Fairplay, MD (21733)	1070
Fallston, MD (21047)	10915
Federalsburg, MD (21632)	5102
Finksburg, MD (21048)	9672
Fishing Creek, MD (21634)	538
Flintstone, MD (21530)	1224
Forest Hill, MD (21050)	16636
Frederick, MD (21701)	28730
Frederick, MD (21702)	32205
Frederick, MD (21703)	26766
Frederick, MD (21704)	10512
Freeland, MD (21053)	2820
Friendsville, MD (21531)	1787
Frostburg, MD (21532)	9484
Fruitland, MD (21826)	3806
Galena, MD (21635)	1757
Gambrills, MD (21054)	9367
Girdletree, MD (21829)	439
Glen Arm, MD (21057)	3718
Glen Burnie, MD (21060)	23756
Glen Burnie, MD (21061)	42373
Glenelg, MD (21737)	1280
Glenwood, MD (21738)	2975
Goldsboro, MD (21636)	939
Grantsville, MD (21536)	3225
Grasonville, MD (21638)	4211
Greensboro, MD (21639)	3629
Hagerstown, MD (21740)	44548
Hagerstown, MD (21742)	25720
Hampstead, MD (21074)	13625
Hancock, MD (21750)	3263
Elkridge, MD (21075)	21407
Hanover, MD (21076)	10451
Havre De Grace, MD (21078)	14843
Hebron, MD (21830)	3392
Henderson, MD (21640)	1212
Hurlock, MD (21643)	4935
Hydes, MD (21082)	825
Jarrettsville, MD (21084)	6986
Jefferson, MD (21755)	4903
Joppa, MD (21085)	14309
Keedysville, MD (21756)	3193
Kennedyville, MD (21645)	861
Keymar, MD (21757)	2417
Kingsville, MD (21087)	5343
Kitzmiller, MD (21538)	543
Linthicum Heights, MD (21090)	8675
Cooksville, MD (21723)	726
Little Orleans, MD (21766)	531
Lonaconing, MD (21539)	2079
Lutherville Timonium, MD (21093)	33490
Mc Henry, MD (21541)	1345
Manchester, MD (21102)	10360
Mardela Springs, MD (21837)	2123
Marion Station, MD (21838)	1537
Marydel, MD (21649)	1129
Maugansville, MD (21767)	1197
Middletown, MD (21769)	10249
Millersville, MD (21108)	15559
Millington, MD (21651)	2324
Monkton, MD (21111)	4550
Monrovia, MD (21770)	4816
Mount Airy, MD (21771)	26546
Mount Savage, MD (21545)	1667
Myersville, MD (21773)	4697
Newark, MD (21841)	736
Ijamsville, MD (21754)	5498
New Market, MD (21774)	10243
New Windsor, MD (21776)	5103
North East, MD (21901)	12892
Oakland, MD (21550)	11196
Ocean City, MD (21842)	9748
Odenton, MD (21113)	24516
Oldtown, MD (21555)	1402
Owings Mills, MD (21117)	43195
Oxford, MD (21654)	1155
Parkton, MD (21120)	6466
Parsonsburg, MD (21849)	2797
Pasadena, MD (21122)	51804
Perry Hall, MD (21128)	11387
Perryville, MD (21903)	4847
Phoenix, MD (21131)	6905
Pittsville, MD (21850)	2290
Pocomoke City, MD (21851)	5977
Point Of Rocks, MD (21777)	1298
Port Deposit, MD (21904)	5905
Preston, MD (21655)	4360
Princess Anne, MD (21853)	6140
Pylesville, MD (21132)	2367
Quantico, MD (21856)	805
Queen Anne, MD (21657)	1028
Queenstown, MD (21658)	3300
Randallstown, MD (21133)	23423
Rawlings, MD (21557)	1524
Reisterstown, MD (21136)	28903
Rhodesdale, MD (21659)	806
Ridgely, MD (21660)	3123
Rising Sun, MD (21911)	9243
Riva, MD (21140)	3133
Rock Hall, MD (21661)	2140
Rocky Ridge, MD (21778)	951
Rohrersville, MD (21779)	796
Royal Oak, MD (21662)	722
Sabillasville, MD (21780)	1300
Saint Michaels, MD (21663)	2855
Salisbury, MD (21801)	20691
Salisbury, MD (21804)	27098
Severn, MD (21144)	27098
Severna Park, MD (21146)	23707
Sharpsburg, MD (21782)	3567
Smithsburg, MD (21783)	7642
Snow Hill, MD (21863)	3963
Sparks Glencoe, MD (21152)	4930
Stevensville, MD (21666)	10970
Stockton, MD (21864)	522
Street, MD (21154)	5563
Sudlersville, MD (21668)	1369
Swanton, MD (21561)	2108
Sykesville, MD (21784)	33098
Taneytown, MD (21787)	9033
Thurmont, MD (21788)	10306
Tilghman, MD (21671)	655
Trappe, MD (21673)	2710
Union Bridge, MD (21791)	4524
Upperco, MD (21155)	2185
Vienna, MD (21869)	755
Walkersville, MD (21793)	8844
Warwick, MD (21912)	941
Westernport, MD (21562)	2374
West Friendship, MD (21794)	2181
Westminster, MD (21157)	30270
Westminster, MD (21158)	18082
Westover, MD (21871)	1524
Whaleyville, MD (21872)	604
Whiteford, MD (21160)	2155
White Hall, MD (21161)	5010
White Marsh, MD (21162)	3333
Willards, MD (21874)	1866
Williamsport, MD (21795)	7944
Woodbine, MD (21797)	7881
Woodsboro, MD (21798)	2188
Marriottsville, MD (21104)	4406
Woodstock, MD (21163)	6104
Worton, MD (21678)	1876
Wye Mills, MD (21679)	500
Delmar, MD (21875)	5235
Aldie, VA (20105)	9002
Alexandria, VA (22301)	9510
Alexandria, VA (22302)	14016
Alexandria, VA (22303)	11138
Alexandria, VA (22304)	36149
Alexandria, VA (22305)	11846
Alexandria, VA (22306)	24752
Alexandria, VA (22307)	8807
Alexandria, VA (22308)	11463
Alexandria, VA (22309)	26104
Alexandria, VA (22310)	24434
Alexandria, VA (22311)	13985
Alexandria, VA (22312)	24759
Alexandria, VA (22314)	24141
Alexandria, VA (22315)	23414
Amissville, VA (20106)	4141
Annandale, VA (22003)	45824
Arlington, VA (22201)	26353
Arlington, VA (22202)	16255
Arlington, VA (22203)	16425
Arlington, VA (22204)	38281
Arlington, VA (22205)	14698
Arlington, VA (22206)	16010
Arlington, VA (22207)	26631
Arlington, VA (22209)	8628
Fort Myer, VA (22211)	628
Arlington, VA (22213)	2545
Ashburn, VA (20147)	45259
Ashburn, VA (20148)	21971
Bealeton, VA (22712)	7400
Bentonville, VA (22610)	1566
Berryville, VA (22611)	7282
Bluemont, VA (20135)	2350
Boston, VA (22713)	1131
Castleton, VA (22716)	679
Boyce, VA (22620)	1744
Brandy Station, VA (22714)	975
Brightwood, VA (22715)	948
Bristow, VA (20136)	22107
Broad Run, VA (20137)	1651
Catharpin, VA (20143)	1029
Catlett, VA (20119)	3067
Centreville, VA (20120)	35432
Centreville, VA (20121)	22529
Clear Brook, VA (22624)	2287
Clifton, VA (20124)	13607
Cross Junction, VA (22625)	3013
Culpeper, VA (22701)	25160
Delaplane, VA (20144)	768
Dulles, VA (20189)	8097
Dumfries, VA (22025)	14495
Dumfries, VA (22026)	11855
Elkwood, VA (22718)	561
Chantilly, VA (20151)	18338
Chantilly, VA (20152)	19709
Fairfax, VA (22030)	40608
Fairfax, VA (22031)	24288
Fairfax, VA (22032)	25982
Fairfax, VA (22033)	31281
Fairfax Station, VA (22039)	17630
Falls Church, VA (22041)	20170
Falls Church, VA (22042)	27438
Falls Church, VA (22043)	19796
Falls Church, VA (22044)	10412
Falls Church, VA (22046)	13745
Flint Hill, VA (22627)	780
Fort Belvoir, VA (22060)	6745
Fort Valley, VA (22652)	1138
Front Royal, VA (22630)	24004
Gainesville, VA (20155)	23841
Goldvein, VA (22720)	764
Gore, VA (22637)	1784
Great Falls, VA (22066)	16197
Hamilton, VA (20158)	3203
Haymarket, VA (20169)	17324
Herndon, VA (20170)	34832
Herndon, VA (20171)	40571
Reston, VA (20190)	13786
Reston, VA (20191)	24549
Reston, VA (20194)	11543
Hume, VA (22639)	573
Jeffersonton, VA (22724)	2034
Leesburg, VA (20175)	21964
Leesburg, VA (20176)	37130
Lignum, VA (22726)	635
Linden, VA (22642)	3722
Lorton, VA (22079)	25937
Lovettsville, VA (20180)	5640
Mc Lean, VA (22101)	25869
Mc Lean, VA (22102)	18650
Aroda, VA (22709)	728
Madison, VA (22727)	4469
Manassas, VA (20109)	28662
Manassas, VA (20110)	34582
Manassas, VA (20111)	25129
Manassas, VA (20112)	22284
Marshall, VA (20115)	4132
Maurertown, VA (22644)	1767
Middleburg, VA (20117)	1131
Middletown, VA (22645)	3154
Midland, VA (22728)	2546
Nokesville, VA (20181)	7064
Paeonian Springs, VA (20129)	524
Purcellville, VA (20132)	11662
Quantico, VA (22134)	4215
Rapidan, VA (22733)	1091
Remington, VA (22734)	2573
Reva, VA (22735)	1686
Rileyville, VA (22650)	802
Rixeyville, VA (22737)	2576
Rochelle, VA (22738)	839
Round Hill, VA (20141)	4601
Sperryville, VA (22740)	1144
Burke, VA (22015)	38291
Springfield, VA (22150)	22990
Springfield, VA (22151)	15333
Springfield, VA (22152)	24957
Springfield, VA (22153)	28359
Star Tannery, VA (22654)	653
Stephens City, VA (22655)	16259
Stephenson, VA (22656)	2118
Sterling, VA (20164)	31855
Sterling, VA (20165)	28382
Sterling, VA (20166)	7729
Strasburg, VA (22657)	8855
Sumerduck, VA (22742)	1481
The Plains, VA (20198)	1567
Toms Brook, VA (22660)	1488
Triangle, VA (22172)	6518
Dunn Loring, VA (22027)	1968
Oakton, VA (22124)	15911
Vienna, VA (22180)	20270
Vienna, VA (22181)	13160
Vienna, VA (22182)	21776
Warrenton, VA (20186)	11491
Warrenton, VA (20187)	13112
Washington, VA (22747)	1089
Waterford, VA (20197)	1727
White Post, VA (22663)	1291
Winchester, VA (22601)	20057
Winchester, VA (22602)	23322
Winchester, VA (22603)	11470
Woodbridge, VA (22191)	44558
Woodbridge, VA (22192)	45434
Woodbridge, VA (22193)	60216
Woodstock, VA (22664)	7068
Accomac, VA (23301)	1346
Afton, VA (22920)	3352
Alberta, VA (23821)	1254
Amelia Court House, VA (23002)	8636
Arrington, VA (22922)	1431
Arvonia, VA (23004)	862
Ashland, VA (23005)	12231
Atlantic, VA (23303)	860
Aylett, VA (23009)	5622
Barboursville, VA (22923)	4284
Barhamsville, VA (23011)	944
Baskerville, VA (23915)	612
Basye, VA (22810)	805
Beaverdam, VA (23015)	3826
Belle Haven, VA (23306)	974
Blackstone, VA (23824)	5768
Bloxom, VA (23308)	1224
Bowling Green, VA (22427)	2786
Boydton, VA (23917)	2209
Boykins, VA (23827)	1103
Bracey, VA (23919)	1899
Bremo Bluff, VA (23022)	667
Bridgewater, VA (22812)	6902
Broadway, VA (22815)	7030
Brodnax, VA (23920)	2534
Buckingham, VA (23921)	1472
Buena Vista, VA (24416)	6616
Bumpass, VA (23024)	6528
Burgess, VA (22432)	791
Burkeville, VA (23922)	1715
Callao, VA (22435)	2029
Cape Charles, VA (23310)	2172
Capron, VA (23829)	1030
Caret, VA (22436)	679
Carrollton, VA (23314)	6486
Carrsville, VA (23315)	1214
Carson, VA (23830)	1343
Cartersville, VA (23027)	1070
Center Cross, VA (22437)	449
Charles City, VA (23030)	4060
Charlotte Court House, VA (23923)	1792
Charlottesville, VA (22901)	26610
Charlottesville, VA (22902)	16159
Charlottesville, VA (22903)	22192
Charlottesville, VA (22911)	13319
Chase City, VA (23924)	4597
Chesapeake, VA (23320)	42825
Chesapeake, VA (23321)	29411
Chesapeake, VA (23322)	51229
Chesapeake, VA (23323)	29870
Chesapeake, VA (23324)	17388
Chesapeake, VA (23325)	14707
Chester, VA (23831)	28331
Chester, VA (23836)	9709
Chesterfield, VA (23832)	29582
Chesterfield, VA (23838)	13788
Chincoteague Island, VA (23336)	2752
Church Road, VA (23833)	1846
Churchville, VA (24421)	3224
Clarksville, VA (23927)	3642
Clifton Forge, VA (24422)	4821
Cobbs Creek, VA (23035)	1072
Colonial Beach, VA (22443)	6288
Colonial Heights, VA (23834)	21644
Columbia, VA (23038)	1469
Courtland, VA (23837)	3421
Covington, VA (24426)	11647
Craigsville, VA (24430)	1243
Crewe, VA (23930)	4465
Crimora, VA (24431)	2321
Crozet, VA (22932)	5914
Crozier, VA (23039)	947
Cullen, VA (23934)	507
Cumberland, VA (23040)	3645
Dahlgren, VA (22448)	1503
Dayton, VA (22821)	4830
Deltaville, VA (23043)	1456
Dendron, VA (23839)	723
Elberon, VA (23846)	720
Dewitt, VA (23840)	1459
Dillwyn, VA (23936)	4432
Dinwiddie, VA (23841)	3033
Disputanta, VA (23842)	5924
Dolphin, VA (23843)	495
Doswell, VA (23047)	1946
Drakes Branch, VA (23937)	1413
Drewryville, VA (23844)	551
Dunnsville, VA (22454)	1216
Dutton, VA (23050)	640
Dyke, VA (22935)	779
Earlysville, VA (22936)	4714
Edinburg, VA (22824)	4975
Elkton, VA (22827)	8630
Emporia, VA (23847)	10290
Esmont, VA (22937)	1030
Exmore, VA (23350)	2274
Faber, VA (22938)	1067
Fairfield, VA (24435)	1631
Farmville, VA (23901)	9879
Farnham, VA (22460)	1336
Fishersville, VA (22939)	4474
Ford, VA (23850)	913
Fork Union, VA (23055)	905
Franklin, VA (23851)	10958
Fredericksburg, VA (22401)	15513
Fredericksburg, VA (22405)	24120
Fredericksburg, VA (22406)	16592
Fredericksburg, VA (22407)	45643
Fredericksburg, VA (22408)	22335
Freeman, VA (23856)	941
Free Union, VA (22940)	1131
Fulks Run, VA (22830)	1427
Gasburg, VA (23857)	578
Glen Allen, VA (23059)	25802
Glen Allen, VA (23060)	28869
Gloucester, VA (23061)	16693
Gloucester Point, VA (23062)	2440
Goochland, VA (23063)	4056
Gordonsville, VA (22942)	6217
Goshen, VA (24439)	917
Greenbackville, VA (23356)	954
Green Bay, VA (23942)	879
Greenville, VA (24440)	2186
Greenwood, VA (22943)	544
Grottoes, VA (24441)	5011
Gum Spring, VA (23065)	1356
Hague, VA (22469)	1438
Fort Monroe, VA (23651)	626
Hampton, VA (23661)	11294
Poquoson, VA (23662)	10997
Hampton, VA (23663)	10559
Hampton, VA (23664)	8675
Hampton, VA (23665)	3830
Hampton, VA (23666)	41120
Hampton, VA (23669)	32001
Hanover, VA (23069)	2561
Harrisonburg, VA (22801)	21001
Harrisonburg, VA (22802)	18590
Harrisonburg, VA (22803)	778
Hartfield, VA (23071)	1354
Hayes, VA (23072)	8539
Heathsville, VA (22473)	3434
Hinton, VA (22831)	709
Hopewell, VA (23860)	22021
Horntown, VA (23395)	482
Hot Springs, VA (24445)	2211
Hudgins, VA (23076)	553
Irvington, VA (22480)	1045
Ivor, VA (23866)	1840
Jarratt, VA (23867)	1804
Jetersville, VA (23083)	1615
Kenbridge, VA (23944)	3139
Kents Store, VA (23084)	1416
Keswick, VA (22947)	4203
Keysville, VA (23947)	3385
Kilmarnock, VA (22482)	2924
King George, VA (22485)	17291
King William, VA (23086)	2605
Kinsale, VA (22488)	1227
La Crosse, VA (23950)	2717
Lancaster, VA (22503)	2734
Lanexa, VA (23089)	4085
Lawrenceville, VA (23868)	3859
Lexington, VA (24450)	11305
Linville, VA (22834)	1107
Locust Grove, VA (22508)	10834
Locust Hill, VA (23092)	438
Lottsburg, VA (22511)	1211
Louisa, VA (23093)	9999
Lovingston, VA (22949)	1242
Luray, VA (22835)	9415
Lyndhurst, VA (22952)	1834
Mc Gaheysville, VA (22840)	3796
Mc Kenney, VA (23872)	1871
Machipongo, VA (23405)	738
Maidens, VA (23102)	2178
Manakin Sabot, VA (23103)	4721
Manquin, VA (23106)	887
Mathews, VA (23109)	1931
Mattaponi, VA (23110)	547
Mechanicsville, VA (23111)	31527
Mechanicsville, VA (23116)	24985
Meherrin, VA (23954)	1610
Melfa, VA (23410)	1566
Middlebrook, VA (24459)	716
Midlothian, VA (23112)	40263
Midlothian, VA (23113)	22168
Midlothian, VA (23114)	15899
Milford, VA (22514)	1905
Millboro, VA (24460)	1291
Mineral, VA (23117)	7507
Monterey, VA (24465)	1144
Montpelier, VA (23192)	5891
Montross, VA (22520)	4385
Moseley, VA (23120)	5279
Mount Crawford, VA (22841)	2419
Mount Jackson, VA (22842)	4050
Fort Defiance, VA (24437)	671
Mount Sidney, VA (24467)	1897
Mount Solon, VA (22843)	2013
Nellysford, VA (22958)	1698
New Canton, VA (23123)	1361
New Church, VA (23415)	1184
New Kent, VA (23124)	2689
New Market, VA (22844)	3657
Newport News, VA (23601)	20577
Newport News, VA (23602)	33650
Newport News, VA (23603)	3066
Fort Eustis, VA (23604)	3132
Newport News, VA (23605)	10962
Newport News, VA (23606)	21078
Newport News, VA (23607)	16229
Newport News, VA (23608)	36035
Newsoms, VA (23874)	886
Norfolk, VA (23502)	16141
Norfolk, VA (23503)	24283
Norfolk, VA (23504)	14428
Norfolk, VA (23505)	21199
Norfolk, VA (23507)	4678
Norfolk, VA (23508)	11290
Norfolk, VA (23509)	10465
Norfolk, VA (23510)	4153
Norfolk, VA (23511)	2195
Norfolk, VA (23513)	23235
Norfolk, VA (23517)	3470
Norfolk, VA (23518)	23206
Norfolk, VA (23521)	707
Norfolk, VA (23523)	5360
North, VA (23128)	1045
North Garden, VA (22959)	1457
Oak Hall, VA (23416)	488
Onancock, VA (23417)	2899
Onley, VA (23418)	1116
Orange, VA (22960)	7992
Painter, VA (23420)	1526
Palmyra, VA (22963)	13052
Pamplin, VA (23958)	2412
Parksley, VA (23421)	2851
Partlow, VA (22534)	2369
Keezletown, VA (22832)	962
Penn Laird, VA (22846)	1569
Fort Lee, VA (23801)	3702
Petersburg, VA (23803)	29382
Petersburg, VA (23805)	15737
Phenix, VA (23959)	894
Port Haywood, VA (23138)	797
Port Republic, VA (24471)	1190
Port Royal, VA (22535)	533
Portsmouth, VA (23701)	19970
Portsmouth, VA (23702)	9055
Portsmouth, VA (23703)	21884
Portsmouth, VA (23704)	13121
Portsmouth, VA (23707)	11025
Powhatan, VA (23139)	20842
Prince George, VA (23875)	9332
Prospect, VA (23960)	1502
Providence Forge, VA (23140)	4482
Quicksburg, VA (22847)	771
Quinton, VA (23141)	5865
Raphine, VA (24472)	1812
Red Oak, VA (23964)	880
Reedville, VA (22539)	1795
Rhoadesville, VA (22542)	1531
Rice, VA (23966)	1811
Henrico, VA (23075)	7531
Richmond, VA (23219)	1508
Richmond, VA (23220)	16861
Richmond, VA (23221)	10957
Richmond, VA (23222)	17607
Richmond, VA (23223)	32635
Richmond, VA (23224)	22615
Richmond, VA (23225)	29120
Richmond, VA (23226)	13674
Richmond, VA (23227)	19421
Henrico, VA (23228)	26502
Henrico, VA (23229)	27780
Richmond, VA (23230)	4678
Henrico, VA (23231)	28091
Henrico, VA (23233)	25562
Richmond, VA (23234)	31921
Richmond, VA (23235)	26806
Richmond, VA (23236)	23959
Richmond, VA (23237)	17931
Henrico, VA (23238)	21203
Henrico, VA (23294)	13518
Rockbridge Baths, VA (24473)	735
Rockville, VA (23146)	2761
Roseland, VA (22967)	1703
Ruckersville, VA (22968)	8084
Ruther Glen, VA (22546)	12545
Saint Stephens Church, VA (23148)	1312
Saluda, VA (23149)	2254
Sandston, VA (23150)	10558
Sandy Hook, VA (23153)	1309
Saxe, VA (23967)	794
Schuyler, VA (22969)	1037
Seaford, VA (23696)	3337
Sedley, VA (23878)	1019
Shacklefords, VA (23156)	1315
Shenandoah, VA (22849)	4048
Shipman, VA (22971)	1291
Singers Glen, VA (22850)	790
Skippers, VA (23879)	666
Skipwith, VA (23968)	662
Smithfield, VA (23430)	14674
South Hill, VA (23970)	6519
Spotsylvania, VA (22551)	13292
Spotsylvania, VA (22553)	14260
Spring Grove, VA (23881)	1453
Stafford, VA (22554)	41183
Stafford, VA (22556)	20731
Stanardsville, VA (22973)	4838
Stanley, VA (22851)	4608
Staunton, VA (24401)	27407
Stony Creek, VA (23882)	1975
Stuarts Draft, VA (24477)	8956
Suffolk, VA (23432)	1276
Suffolk, VA (23433)	1180
Suffolk, VA (23434)	37709
Suffolk, VA (23435)	22013
Suffolk, VA (23436)	775
Suffolk, VA (23437)	3577
Suffolk, VA (23438)	1455
Surry, VA (23883)	2133
Sutherland, VA (23885)	2433
Swoope, VA (24479)	1344
Tappahannock, VA (22560)	5667
Temperanceville, VA (23442)	896
Timberville, VA (22853)	3772
Toano, VA (23168)	5486
Topping, VA (23169)	902
Troy, VA (22974)	3443
Unionville, VA (22567)	2394
Urbanna, VA (23175)	1846
Verona, VA (24482)	4032
Vesuvius, VA (24483)	576
Victoria, VA (23974)	3019
Virginia Beach, VA (23451)	33789
Virginia Beach, VA (23452)	49874
Virginia Beach, VA (23453)	29451
Virginia Beach, VA (23454)	50900
Virginia Beach, VA (23455)	38373
Virginia Beach, VA (23456)	44836
Virginia Beach, VA (23457)	3890
Virginia Beach, VA (23459)	819
Virginia Beach, VA (23460)	563
Virginia Beach, VA (23462)	49323
Virginia Beach, VA (23464)	62321
Salisbury, NC (28146)	20958
Salisbury, NC (28147)	19006
Saluda, NC (28773)	2433
Sapphire, NC (28774)	750
Seven Springs, NC (28578)	3762
Calabash, NC (28467)	7097
Sunset Beach, NC (28468)	3548
Ocean Isle Beach, NC (28469)	5200
Wake, VA (23176)	482
Wakefield, VA (23888)	2039
Walkerton, VA (23177)	578
Warfield, VA (23889)	505
Warm Springs, VA (24484)	709
Warsaw, VA (22572)	4593
Waverly, VA (23890)	3255
Waynesboro, VA (22980)	26271
Weems, VA (22576)	1255
West Point, VA (23181)	4776
Weyers Cave, VA (24486)	2989
White Stone, VA (22578)	2107
Williamsburg, VA (23185)	35764
Williamsburg, VA (23188)	32724
Wilsons, VA (23894)	528
Windsor, VA (23487)	5268
Woodford, VA (22580)	3710
Yale, VA (23897)	483
Yorktown, VA (23690)	2181
Yorktown, VA (23692)	17083
Yorktown, VA (23693)	20679
Zuni, VA (23898)	1919
Advance, NC (27006)	12136
Ahoskie, NC (27910)	8247
Angier, NC (27501)	13444
Apex, NC (27502)	26612
Apex, NC (27523)	7555
Apex, NC (27539)	15115
Ararat, NC (27007)	1666
Asheboro, NC (27203)	15228
Asheboro, NC (27205)	25331
Aulander, NC (27805)	2599
Aurora, NC (27806)	1829
Aydlett, NC (27916)	528
Bahama, NC (27503)	3100
Bailey, NC (27807)	5302
Banner Elk, NC (28604)	4593
Barco, NC (27917)	499
Bath, NC (27808)	1919
Battleboro, NC (27809)	4020
Bear Creek, NC (27207)	2802
Belews Creek, NC (27009)	2402
Belhaven, NC (27810)	3030
Belvidere, NC (27919)	932
Bennett, NC (27208)	1320
Benson, NC (27504)	11185
Bethel, NC (27812)	2108
Biscoe, NC (27209)	3480
Blounts Creek, NC (27814)	1295
Blowing Rock, NC (28605)	3192
Boomer, NC (28606)	1662
Boone, NC (28607)	16910
Boonville, NC (27011)	4153
Broadway, NC (27505)	4810
Browns Summit, NC (27214)	8746
Bullock, NC (27507)	1344
Bunn, NC (27508)	1549
Burlington, NC (27215)	30712
Burlington, NC (27217)	27330
Butner, NC (27509)	3128
Camden, NC (27921)	4086
Candor, NC (27229)	3245
Carrboro, NC (27510)	10912
Cary, NC (27511)	27979
Cary, NC (27513)	35127
Cary, NC (27518)	16786
Cary, NC (27519)	31110
Castalia, NC (27816)	2056
Catawba, NC (28609)	4909
Cedar Grove, NC (27231)	1600
Chapel Hill, NC (27514)	19141
Chapel Hill, NC (27516)	26169
Chapel Hill, NC (27517)	19490
Chocowinity, NC (27817)	5886
Claremont, NC (28610)	8224
Clayton, NC (27520)	28384
Clayton, NC (27527)	14513
Clayton, NC (27528)	939
Clemmons, NC (27012)	22622
Cleveland, NC (27013)	4819
Climax, NC (27233)	2848
Coats, NC (27521)	4701
Cofield, NC (27922)	662
Coinjock, NC (27923)	477
Colerain, NC (27924)	2241
Colfax, NC (27235)	3794
Collettsville, NC (28611)	690
Columbia, NC (27925)	2936
Como, NC (27818)	1024
Connellys Springs, NC (28612)	8122
Conover, NC (28613)	19395
Conway, NC (27820)	2108
Corapeake, NC (27926)	1344
Corolla, NC (27927)	666
Creedmoor, NC (27522)	9765
Creston, NC (28615)	1450
Creswell, NC (27928)	1557
Crumpler, NC (28617)	1487
Currituck, NC (27929)	1097
Danbury, NC (27016)	1343
Deep Gap, NC (28618)	1837
Denton, NC (27239)	7225
Dobson, NC (27017)	6754
Durham, NC (27701)	13152
Durham, NC (27703)	33743
Durham, NC (27704)	25903
Durham, NC (27705)	31340
Durham, NC (27707)	31515
Durham, NC (27712)	17922
Durham, NC (27713)	37767
Eagle Springs, NC (27242)	1442
East Bend, NC (27018)	6402
Eden, NC (27288)	17582
Edenton, NC (27932)	9972
Efland, NC (27243)	3745
Elizabeth City, NC (27909)	29701
Elkin, NC (28621)	7675
Elk Park, NC (28622)	1756
Elm City, NC (27822)	6945
Elon, NC (27244)	8430
Enfield, NC (27823)	5924
Engelhard, NC (27824)	1011
Ennice, NC (28623)	1222
Eure, NC (27935)	1209
Fairfield, NC (27826)	491
Farmville, NC (27828)	6921
Ferguson, NC (28624)	1257
Fleetwood, NC (28626)	1705
Fountain, NC (27829)	1361
Four Oaks, NC (27524)	9233
Franklinton, NC (27525)	10237
Franklinville, NC (27248)	3445
Fremont, NC (27830)	3484
Fuquay Varina, NC (27526)	32081
Garner, NC (27529)	34351
Garysburg, NC (27831)	2230
Gaston, NC (27832)	2466
Gates, NC (27937)	2907
Gatesville, NC (27938)	1177
Germanton, NC (27019)	3331
Gibsonville, NC (27249)	9770
Glade Valley, NC (28627)	898
Goldsboro, NC (27530)	27804
Goldsboro, NC (27531)	543
Goldsboro, NC (27534)	23905
Goldston, NC (27252)	1471
Graham, NC (27253)	22736
Grandy, NC (27939)	2059
Granite Falls, NC (28630)	15602
Grassy Creek, NC (28631)	452
Greensboro, NC (27401)	11007
Greensboro, NC (27403)	12513
Greensboro, NC (27405)	30864
Greensboro, NC (27406)	40803
Greensboro, NC (27407)	35829
Greensboro, NC (27408)	14898
Greensboro, NC (27409)	11476
Greensboro, NC (27410)	43943
Greensboro, NC (27455)	23235
Greenville, NC (27834)	33975
Greenville, NC (27858)	32258
Grimesland, NC (27837)	4547
Halifax, NC (27839)	2090
Hamilton, NC (27840)	564
Hamptonville, NC (27020)	5076
Harbinger, NC (27941)	517
Harmony, NC (28634)	4110
Harrellsville, NC (27942)	617
Haw River, NC (27258)	5049
Hays, NC (28635)	3008
Henderson, NC (27536)	13695
Henderson, NC (27537)	16584
Henrico, NC (27842)	1123
Hertford, NC (27944)	8794
Hickory, NC (28601)	39530
Hickory, NC (28602)	21830
Hiddenite, NC (28636)	4269
High Point, NC (27260)	17208
High Point, NC (27262)	17405
High Point, NC (27263)	16748
High Point, NC (27265)	37630
Hildebran, NC (28637)	2320
Hillsborough, NC (27278)	20214
Hobbsville, NC (27946)	932
Hobgood, NC (27843)	870
Hollister, NC (27844)	2059
Holly Springs, NC (27540)	23508
Hudson, NC (28638)	9990
Hurdle Mills, NC (27541)	3156
Jackson, NC (27845)	1397
Jackson Springs, NC (27281)	1835
Jamestown, NC (27282)	13211
Jamesville, NC (27846)	2458
Jarvisburg, NC (27947)	686
Jefferson, NC (28640)	3656
Jonesville, NC (28642)	4239
Julian, NC (27283)	2812
Kelford, NC (27847)	598
Kenly, NC (27542)	7215
Kernersville, NC (27284)	42019
Kill Devil Hills, NC (27948)	9130
King, NC (27021)	14474
Kittrell, NC (27544)	3073
Kitty Hawk, NC (27949)	6888
Knightdale, NC (27545)	18838
Knotts Island, NC (27950)	1553
Lansing, NC (28643)	2556
Laurel Springs, NC (28644)	1115
Lawsonville, NC (27022)	1257
Leasburg, NC (27291)	1223
Lenoir, NC (28645)	34395
Lewiston Woodville, NC (27849)	1304
Lewisville, NC (27023)	10702
Lexington, NC (27292)	29284
Lexington, NC (27295)	29190
Liberty, NC (27298)	8345
Lillington, NC (27546)	11304
Linwood, NC (27299)	4206
Littleton, NC (27850)	5300
Louisburg, NC (27549)	16256
Lowgap, NC (27024)	1921
Lucama, NC (27851)	4238
Mc Grady, NC (28649)	728
Mc Leansville, NC (27301)	7421
Macclesfield, NC (27852)	2060
Macon, NC (27551)	1400
Madison, NC (27025)	8768
Maiden, NC (28650)	10381
Manns Harbor, NC (27953)	785
Manson, NC (27553)	1676
Manteo, NC (27954)	5270
Mayodan, NC (27027)	3373
Mebane, NC (27302)	21127
Merry Hill, NC (27957)	1163
Middlesex, NC (27557)	5805
Millers Creek, NC (28651)	5380
Milton, NC (27305)	1176
Mocksville, NC (27028)	20083
Moncure, NC (27559)	1898
Moravian Falls, NC (28654)	2994
Morganton, NC (28655)	36214
Morrisville, NC (27560)	18443
Mount Airy, NC (27030)	28946
Mount Gilead, NC (27306)	4804
Moyock, NC (27958)	8123
Murfreesboro, NC (27855)	3976
Nags Head, NC (27959)	2496
Nashville, NC (27856)	13101
New Hill, NC (27562)	1553
Newland, NC (28657)	5764
Newton, NC (28658)	21713
Norlina, NC (27563)	3303
North Wilkesboro, NC (28659)	15191
Oak City, NC (27857)	1012
Oak Ridge, NC (27310)	6630
Olin, NC (28660)	1726
Oxford, NC (27565)	19588
Pantego, NC (27860)	1546
Pelham, NC (27311)	2669
Pendleton, NC (27862)	545
Pfafftown, NC (27040)	9340
Pikeville, NC (27863)	9108
Pilot Mountain, NC (27041)	6299
Pine Hall, NC (27042)	622
Pinetops, NC (27864)	3881
Pinetown, NC (27865)	1543
Piney Creek, NC (28663)	515
Pinnacle, NC (27043)	4895
Pittsboro, NC (27312)	15224
Pleasant Garden, NC (27313)	5876
Pleasant Hill, NC (27866)	579
Plymouth, NC (27962)	5748
Point Harbor, NC (27964)	453
Poplar Branch, NC (27965)	424
Powells Point, NC (27966)	918
Princeton, NC (27569)	5958
Prospect Hill, NC (27314)	840
Providence, NC (27315)	1653
Purlear, NC (28665)	1891
Raleigh, NC (27601)	4807
Raleigh, NC (27603)	33789
Raleigh, NC (27604)	32169
Raleigh, NC (27605)	3570
Raleigh, NC (27606)	27654
Raleigh, NC (27607)	13438
Raleigh, NC (27608)	8837
Raleigh, NC (27609)	28038
Raleigh, NC (27610)	46641
Raleigh, NC (27612)	28478
Raleigh, NC (27613)	38110
Raleigh, NC (27614)	26794
Raleigh, NC (27615)	37234
Raleigh, NC (27616)	32778
Raleigh, NC (27617)	12300
Ramseur, NC (27316)	5344
Randleman, NC (27317)	13648
Reidsville, NC (27320)	29499
Rich Square, NC (27869)	1671
Roanoke Rapids, NC (27870)	20295
Roaring River, NC (28669)	2441
Robbins, NC (27325)	5174
Robersonville, NC (27871)	3502
Rocky Mount, NC (27801)	14319
Rocky Mount, NC (27803)	16468
Rocky Mount, NC (27804)	22882
Rolesville, NC (27571)	3451
Ronda, NC (28670)	2203
Roper, NC (27970)	2689
Rougemont, NC (27572)	5503
Roxboro, NC (27573)	8530
Roxboro, NC (27574)	11151
Ruffin, NC (27326)	3039
Rural Hall, NC (27045)	7167
Sandy Ridge, NC (27046)	1709
Sanford, NC (27330)	27541
Sanford, NC (27332)	21711
Scotland Neck, NC (27874)	3455
Seaboard, NC (27876)	1012
Seagrove, NC (27341)	4305
Selma, NC (27576)	11891
Semora, NC (27343)	1248
Shawboro, NC (27973)	1108
Sherrills Ford, NC (28673)	5113
Shiloh, NC (27974)	1009
Siler City, NC (27344)	13823
Siloam, NC (27047)	925
Sims, NC (27880)	2567
Smithfield, NC (27577)	16415
Snow Camp, NC (27349)	4917
Sophia, NC (27350)	5147
South Mills, NC (27976)	2768
Sparta, NC (28675)	4859
Spring Hope, NC (27882)	5961
Staley, NC (27355)	2100
Stantonsburg, NC (27883)	2693
Star, NC (27356)	2149
State Road, NC (28676)	2909
Statesville, NC (28625)	29245
Statesville, NC (28677)	25330
Stem, NC (27581)	2527
Stokes, NC (27884)	1129
Stokesdale, NC (27357)	6605
Stoneville, NC (27048)	6763
Stony Point, NC (28678)	4216
Sugar Grove, NC (28679)	1537
Summerfield, NC (27358)	11982
Sunbury, NC (27979)	1259
Swanquarter, NC (27885)	744
Tarboro, NC (27886)	16123
Taylorsville, NC (28681)	19347
Terrell, NC (28682)	1011
Thomasville, NC (27360)	34943
Thurmond, NC (28683)	1294
Timberlake, NC (27583)	5795
Tobaccoville, NC (27050)	3342
Todd, NC (28684)	1365
Traphill, NC (28685)	1455
Trinity, NC (27370)	12543
Troy, NC (27371)	5604
Tyner, NC (27980)	1705
Union Grove, NC (28689)	1664
Valdese, NC (28690)	7045
Vilas, NC (28692)	2922
Wake Forest, NC (27587)	41945
Walkertown, NC (27051)	6248
Walnut Cove, NC (27052)	8344
Walstonburg, NC (27888)	1889
Wanchese, NC (27981)	1385
Warrensville, NC (28693)	1116
Warrenton, NC (27589)	5232
Washington, NC (27889)	21102
Weldon, NC (27890)	1926
Wendell, NC (27591)	15773
West End, NC (27376)	7264
Westfield, NC (27053)	2495
West Jefferson, NC (28694)	6351
Whitakers, NC (27891)	4223
Whitsett, NC (27377)	5821
Wilkesboro, NC (28697)	9480
Williamston, NC (27892)	11259
Willow Spring, NC (27592)	11987
Wilson, NC (27893)	27714
Wilson, NC (27896)	15775
Windsor, NC (27983)	6409
Winston Salem, NC (27101)	12629
Winston Salem, NC (27103)	27102
Winston Salem, NC (27104)	24341
Winston Salem, NC (27105)	27361
Winston Salem, NC (27106)	34137
Winston Salem, NC (27107)	35465
Winston Salem, NC (27127)	26600
Winton, NC (27986)	948
Woodland, NC (27897)	1116
Woodleaf, NC (27054)	2319
Yadkinville, NC (27055)	11454
Blanch, NC (27212)	1108
Yanceyville, NC (27379)	3700
Youngsville, NC (27596)	12141
Zebulon, NC (27597)	16935
Zionville, NC (28698)	1562
Aberdeen, NC (28315)	8383
Albemarle, NC (28001)	18787
Albertson, NC (28508)	1536
Alexander, NC (28701)	2971
Alexis, NC (28006)	1071
Andrews, NC (28901)	3899
Arapahoe, NC (28510)	1267
Arden, NC (28704)	15146
Ash, NC (28420)	2587
Asheville, NC (28801)	8816
Asheville, NC (28803)	21626
Asheville, NC (28804)	15216
Asheville, NC (28805)	13279
Asheville, NC (28806)	28498
Atkinson, NC (28421)	1192
Atlantic, NC (28511)	492
Atlantic Beach, NC (28512)	2653
Autryville, NC (28318)	3570
Ayden, NC (28513)	7515
Bakersville, NC (28705)	4765
Barnardsville, NC (28709)	1828
Bayboro, NC (28515)	1543
Beaufort, NC (28516)	9176
Belmont, NC (28012)	16555
Bessemer City, NC (28016)	10243
Beulaville, NC (28518)	5628
Black Mountain, NC (28711)	9602
Bladenboro, NC (28320)	6012
Bolivia, NC (28422)	4859
Bolton, NC (28423)	1666
Bostic, NC (28018)	3952
Brasstown, NC (28902)	1073
Brevard, NC (28712)	12933
Bryson City, NC (28713)	6965
Bunnlevel, NC (28323)	2496
Burgaw, NC (28425)	7604
Burnsville, NC (28714)	11419
Cameron, NC (28326)	12101
Candler, NC (28715)	19048
Canton, NC (28716)	13388
Carolina Beach, NC (28428)	4913
Carthage, NC (28327)	11673
Casar, NC (28020)	2024
Cashiers, NC (28717)	2081
Castle Hayne, NC (28429)	6262
Cedar Mountain, NC (28718)	594
Cerro Gordo, NC (28430)	1455
Chadbourn, NC (28431)	5116
Charlotte, NC (28202)	6138
Charlotte, NC (28203)	8521
Charlotte, NC (28204)	3299
Charlotte, NC (28205)	31588
Charlotte, NC (28206)	8018
Charlotte, NC (28207)	7318
Charlotte, NC (28208)	24286
Charlotte, NC (28209)	15675
Charlotte, NC (28210)	34313
Charlotte, NC (28211)	23448
Charlotte, NC (28212)	26411
Charlotte, NC (28213)	25793
Charlotte, NC (28214)	27091
Charlotte, NC (28215)	41131
Charlotte, NC (28216)	35442
Charlotte, NC (28217)	18775
Charlotte, NC (28226)	32701
Charlotte, NC (28227)	39554
Charlotte, NC (28262)	23386
Charlotte, NC (28269)	56159
Charlotte, NC (28270)	26456
Charlotte, NC (28273)	25040
Charlotte, NC (28277)	51425
Charlotte, NC (28278)	15741
Cherokee, NC (28719)	6304
Cherryville, NC (28021)	10469
China Grove, NC (28023)	11700
Chinquapin, NC (28521)	1578
Clarendon, NC (28432)	1515
Clarkton, NC (28433)	3501
Clinton, NC (28328)	17813
Clyde, NC (28721)	7882
Columbus, NC (28722)	4969
Concord, NC (28025)	38160
Concord, NC (28027)	44852
Cornelius, NC (28031)	20400
Council, NC (28434)	927
Cove City, NC (28523)	2039
Cramerton, NC (28032)	2503
Crouse, NC (28033)	2407
Cullowhee, NC (28723)	4536
Currie, NC (28435)	1844
Dallas, NC (28034)	13059
Davidson, NC (28036)	11399
Deep Run, NC (28525)	2446
Delco, NC (28436)	1725
Denver, NC (28037)	15837
Dover, NC (28526)	1886
Dudley, NC (28333)	8200
Dunn, NC (28334)	17097
East Flat Rock, NC (28726)	2623
Elizabethtown, NC (28337)	7232
Ellenboro, NC (28040)	5311
Ellerbe, NC (28338)	3318
Emerald Isle, NC (28594)	3293
Ernul, NC (28527)	985
Erwin, NC (28339)	5166
Etowah, NC (28729)	3226
Evergreen, NC (28438)	1252
Fair Bluff, NC (28439)	1216
Fairmont, NC (28340)	7469
Fairview, NC (28730)	7645
Faison, NC (28341)	3329
Fayetteville, NC (28301)	10433
Fayetteville, NC (28303)	24909
Fayetteville, NC (28304)	29520
Fayetteville, NC (28305)	5241
Fayetteville, NC (28306)	30542
Fort Bragg, NC (28307)	12275
Pope Army Airfield, NC (28308)	452
Fayetteville, NC (28311)	26347
Fayetteville, NC (28312)	13747
Fayetteville, NC (28314)	42555
Flat Rock, NC (28731)	6479
Fletcher, NC (28732)	13344
Forest City, NC (28043)	14458
Franklin, NC (28734)	19590
Garland, NC (28441)	2472
Gastonia, NC (28052)	24059
Gastonia, NC (28054)	26414
Gastonia, NC (28056)	26053
Gibson, NC (28343)	1206
Glenville, NC (28736)	521
Gloucester, NC (28528)	495
Godwin, NC (28344)	2305
Gold Hill, NC (28071)	2330
Grantsboro, NC (28529)	1538
Green Mountain, NC (28740)	1741
Grifton, NC (28530)	5543
Grover, NC (28073)	4038
Hallsboro, NC (28442)	1237
Hamlet, NC (28345)	9267
Hampstead, NC (28443)	13880
Harkers Island, NC (28531)	1118
Harrells, NC (28444)	1619
Harrisburg, NC (28075)	13755
Havelock, NC (28532)	18917
Cherry Point, NC (28533)	1902
Hayesville, NC (28904)	6240
Hendersonville, NC (28739)	14540
Hendersonville, NC (28791)	10468
Hendersonville, NC (28792)	21168
Highlands, NC (28741)	2868
Hoffman, NC (28347)	654
Marston, NC (28363)	863
Holly Ridge, NC (28445)	4939
Hookerton, NC (28538)	1647
Hope Mills, NC (28348)	26469
Horse Shoe, NC (28742)	2647
Mills River, NC (28759)	5376
Hot Springs, NC (28743)	1476
Hubert, NC (28539)	11941
Huntersville, NC (28078)	42478
Indian Trail, NC (28079)	26134
Iron Station, NC (28080)	6088
Ivanhoe, NC (28447)	873
Jacksonville, NC (28540)	38293
Tarawa Terrace, NC (28543)	3732
Midway Park, NC (28544)	4338
Mccutcheon Field, NC (28545)	910
Jacksonville, NC (28546)	32677
Camp Lejeune, NC (28547)	4308
Kannapolis, NC (28081)	18974
Kannapolis, NC (28083)	17861
Kelly, NC (28448)	690
Kenansville, NC (28349)	2759
Kings Mountain, NC (28086)	20706
Kinston, NC (28501)	13575
Kinston, NC (28504)	16316
Kure Beach, NC (28449)	1492
La Grange, NC (28551)	10322
Lake Junaluska, NC (28745)	1389
Lake Lure, NC (28746)	1864
Lake Toxaway, NC (28747)	1451
Lake Waccamaw, NC (28450)	1689
Landis, NC (28088)	2633
Laurel Hill, NC (28351)	3743
Laurinburg, NC (28352)	16551
Lawndale, NC (28090)	5757
Leicester, NC (28748)	9543
Leland, NC (28451)	20410
Lilesville, NC (28091)	1777
Lincolnton, NC (28092)	28399
Linden, NC (28356)	3775
Locust, NC (28097)	4435
Longwood, NC (28452)	560
Lowell, NC (28098)	3117
Lumber Bridge, NC (28357)	2128
Lumberton, NC (28358)	23591
Lumberton, NC (28360)	8229
Mc Adenville, NC (28101)	721
Maggie Valley, NC (28751)	2660
Magnolia, NC (28453)	2754
Maple Hill, NC (28454)	1966
Marble, NC (28905)	2318
Marion, NC (28752)	22290
Marshall, NC (28753)	8350
Mars Hill, NC (28754)	5397
Marshville, NC (28103)	7924
Matthews, NC (28104)	23202
Matthews, NC (28105)	32992
Maxton, NC (28364)	9106
Maysville, NC (28555)	4234
Merritt, NC (28556)	749
Midland, NC (28107)	5436
Mill Spring, NC (28756)	3061
Monroe, NC (28110)	39034
Monroe, NC (28112)	19706
Mooresboro, NC (28114)	4469
Mooresville, NC (28115)	27584
Mooresville, NC (28117)	29568
Morehead City, NC (28557)	12355
Morven, NC (28119)	2078
Mount Holly, NC (28120)	16127
Mount Olive, NC (28365)	10931
Mount Pleasant, NC (28124)	5464
Mount Ulla, NC (28125)	2112
Murphy, NC (28906)	13138
Nakina, NC (28455)	1445
Nebo, NC (28761)	5833
New Bern, NC (28560)	21255
New Bern, NC (28562)	28900
New London, NC (28127)	4990
Newport, NC (28570)	16816
Newton Grove, NC (28366)	4031
Norwood, NC (28128)	5964
Oakboro, NC (28129)	4475
Old Fort, NC (28762)	5587
Oriental, NC (28571)	2170
Orrum, NC (28369)	1586
Otto, NC (28763)	2070
Parkton, NC (28371)	4854
Peachland, NC (28133)	2229
Pembroke, NC (28372)	9692
Penrose, NC (28766)	1342
Pinebluff, NC (28373)	1980
Pinehurst, NC (28374)	13526
Pineville, NC (28134)	7418
Pink Hill, NC (28572)	4576
Pisgah Forest, NC (28768)	5565
Polkton, NC (28135)	2710
Pollocksville, NC (28573)	1743
Raeford, NC (28376)	27467
Red Springs, NC (28377)	7879
Richfield, NC (28137)	2392
Richlands, NC (28574)	11627
Riegelwood, NC (28456)	2672
Robbinsville, NC (28771)	6115
Rockingham, NC (28379)	17809
Rockwell, NC (28138)	8491
Rocky Point, NC (28457)	7646
Roseboro, NC (28382)	5361
Rose Hill, NC (28458)	4597
Rosman, NC (28772)	1689
Rowland, NC (28383)	5194
Rutherfordton, NC (28139)	14594
Saint Pauls, NC (28384)	8796
Salemburg, NC (28385)	2431
Salisbury, NC (28144)	16371
Shallotte, NC (28470)	6333
Shannon, NC (28386)	3872
Shelby, NC (28150)	19605
Shelby, NC (28152)	16991
Smyrna, NC (28579)	480
Sneads Ferry, NC (28460)	6353
Snow Hill, NC (28580)	7417
Southern Pines, NC (28387)	9870
Southport, NC (28461)	13180
Oak Island, NC (28465)	5550
Spencer, NC (28159)	2388
Spindale, NC (28160)	2671
Spring Lake, NC (28390)	14565
Spruce Pine, NC (28777)	6996
Stanfield, NC (28163)	4116
Stanley, NC (28164)	11986
Stedman, NC (28391)	4502
Stella, NC (28582)	1345
Supply, NC (28462)	8438
Swannanoa, NC (28778)	7619
Swansboro, NC (28584)	9654
Sylva, NC (28779)	10102
Tabor City, NC (28463)	5443
Tar Heel, NC (28392)	1422
Teachey, NC (28464)	1590
Topton, NC (28781)	664
Trenton, NC (28585)	3017
Troutman, NC (28166)	7617
Tryon, NC (28782)	4735
Tuckasegee, NC (28783)	992
Turkey, NC (28393)	1590
Union Mills, NC (28167)	1793
Vale, NC (28168)	8020
Vanceboro, NC (28586)	5478
Vass, NC (28394)	3954
Wade, NC (28395)	2009
Wadesboro, NC (28170)	8450
Wagram, NC (28396)	2226
Wallace, NC (28466)	7221
Warne, NC (28909)	755
Warsaw, NC (28398)	4989
Waxhaw, NC (28173)	35179
Waynesville, NC (28785)	5289
Waynesville, NC (28786)	15174
Weaverville, NC (28787)	16686
White Oak, NC (28399)	1321
Whiteville, NC (28472)	13577
Whittier, NC (28789)	4234
Willard, NC (28478)	3452
Wilmington, NC (28401)	14224
Wilmington, NC (28403)	21508
Wilmington, NC (28405)	23100
Wilmington, NC (28409)	25626
Wilmington, NC (28411)	25564
Wilmington, NC (28412)	26821
Wingate, NC (28174)	6303
Winnabow, NC (28479)	3709
Winterville, NC (28590)	19315
Wrightsville Beach, NC (28480)	2209
Zirconia, NC (28790)	2321
Blacksburg, SC (29702)	7392
Catawba, SC (29704)	2937
Chester, SC (29706)	15352
Chesterfield, SC (29709)	4736
Clover, SC (29710)	23561
Edgemoor, SC (29712)	1893
Fort Lawn, SC (29714)	2202
Fort Mill, SC (29707)	13054
Fort Mill, SC (29708)	21099
Fort Mill, SC (29715)	19975
Hickory Grove, SC (29717)	1044
Jefferson, SC (29718)	2673
Lancaster, SC (29720)	32663
Mc Connells, SC (29726)	1384
Mount Croghan, SC (29727)	1078
Pageland, SC (29728)	7007
Richburg, SC (29729)	1893
Rock Hill, SC (29730)	38992
Rock Hill, SC (29732)	44079
Ruby, SC (29741)	1425
Sharon, SC (29742)	1975
Smyrna, SC (29743)	992
York, SC (29745)	22847
Abbeville, SC (29620)	10139
Adams Run, SC (29426)	1486
Alcolu, SC (29001)	1682
Anderson, SC (29621)	29826
Anderson, SC (29624)	10476
Anderson, SC (29625)	20343
Anderson, SC (29626)	9391
Andrews, SC (29510)	8445
Awendaw, SC (29429)	2344
Aynor, SC (29511)	4102
Galivants Ferry, SC (29544)	3649
Bamberg, SC (29003)	4851
Belton, SC (29627)	13569
Bennettsville, SC (29512)	12911
Bethune, SC (29009)	1849
Bishopville, SC (29010)	8554
Blackstock, SC (29014)	1439
Blair, SC (29015)	1222
Blenheim, SC (29516)	688
Blythewood, SC (29016)	13765
Bonneau, SC (29431)	4826
Bowman, SC (29018)	2971
Branchville, SC (29432)	2107
Buffalo, SC (29321)	2052
Cades, SC (29518)	1145
Calhoun Falls, SC (29628)	2078
Camden, SC (29020)	17071
Cameron, SC (29030)	1521
Campobello, SC (29322)	6871
Carlisle, SC (29031)	1099
Cassatt, SC (29032)	3156
Cayce, SC (29033)	8640
West Columbia, SC (29169)	16001
West Columbia, SC (29170)	16531
West Columbia, SC (29172)	7190
Central, SC (29630)	8493
Chapin, SC (29036)	16448
Chappells, SC (29037)	684
Charleston, SC (29401)	5783
Charleston, SC (29403)	11922
Charleston Afb, SC (29404)	1383
North Charleston, SC (29405)	17749
Charleston, SC (29406)	20525
Charleston, SC (29407)	27701
Hanahan, SC (29410)	11936
Charleston, SC (29412)	28668
Charleston, SC (29414)	26639
North Charleston, SC (29418)	17996
North Charleston, SC (29420)	15694
Charleston, SC (29492)	7977
Cheraw, SC (29520)	10687
Chesnee, SC (29323)	11286
Clemson, SC (29631)	7118
Cleveland, SC (29635)	1083
Clinton, SC (29325)	10622
Clio, SC (29525)	1747
Columbia, SC (29201)	8111
Columbia, SC (29203)	27309
Columbia, SC (29204)	13263
Columbia, SC (29205)	16600
Columbia, SC (29206)	15489
Columbia, SC (29209)	25598
Columbia, SC (29210)	25830
Columbia, SC (29212)	24187
Columbia, SC (29223)	39233
Columbia, SC (29229)	36287
Conway, SC (29526)	27572
Conway, SC (29527)	15768
Cope, SC (29038)	2048
Cordova, SC (29039)	3167
Cottageville, SC (29435)	3005
Coward, SC (29530)	2115
Cowpens, SC (29330)	6276
Cross, SC (29436)	3266
Cross Hill, SC (29332)	1873
Dalzell, SC (29040)	7022
Darlington, SC (29532)	14529
Darlington, SC (29540)	5086
Denmark, SC (29042)	3449
Dillon, SC (29536)	12738
Donalds, SC (29638)	2138
Dorchester, SC (29437)	1874
Due West, SC (29639)	1105
Duncan, SC (29334)	9012
Easley, SC (29640)	23405
Easley, SC (29642)	24584
Eastover, SC (29044)	4297
Edisto Island, SC (29438)	1976
Effingham, SC (29541)	7061
Ehrhardt, SC (29081)	972
Elgin, SC (29045)	16992
Elloree, SC (29047)	2762
Enoree, SC (29335)	3293
Eutawville, SC (29048)	3563
Fair Play, SC (29643)	2233
Florence, SC (29501)	32929
Florence, SC (29505)	18766
Florence, SC (29506)	13667
Fork, SC (29543)	448
Fountain Inn, SC (29644)	14854
Gable, SC (29051)	722
Gadsden, SC (29052)	1677
Gaffney, SC (29340)	15111
Gaffney, SC (29341)	14050
Gaston, SC (29053)	13483
Georgetown, SC (29440)	20441
Gilbert, SC (29054)	8067
Goose Creek, SC (29445)	43301
Gray Court, SC (29645)	7882
Great Falls, SC (29055)	3220
Greeleyville, SC (29056)	1940
Green Pond, SC (29446)	917
Green Sea, SC (29545)	1382
Greenville, SC (29601)	6135
Greenville, SC (29605)	25802
Greenville, SC (29607)	26061
Greenville, SC (29609)	20866
Greenville, SC (29611)	20333
Greenville, SC (29615)	29038
Greenville, SC (29617)	17904
Greenwood, SC (29646)	20381
Greenwood, SC (29649)	19625
Greer, SC (29650)	26997
Greer, SC (29651)	33565
Gresham, SC (29546)	2067
Hamer, SC (29547)	2092
Harleyville, SC (29448)	1946
Hartsville, SC (29550)	22614
Heath Springs, SC (29058)	3697
Hemingway, SC (29554)	7371
Hodges, SC (29653)	3802
Holly Hill, SC (29059)	4740
Hollywood, SC (29449)	6131
Honea Path, SC (29654)	7511
Hopkins, SC (29061)	11352
Huger, SC (29450)	2463
Inman, SC (29349)	23590
Irmo, SC (29063)	28536
Isle Of Palms, SC (29451)	3790
Iva, SC (29655)	5236
Jamestown, SC (29453)	996
Jenkinsville, SC (29065)	635
Joanna, SC (29351)	1165
Johns Island, SC (29455)	14830
Johnsonville, SC (29555)	4688
Jonesville, SC (29353)	3229
Kershaw, SC (29067)	6801
Kinards, SC (29355)	644
Kingstree, SC (29556)	9547
Ladson, SC (29456)	20484
Lake City, SC (29560)	10070
Lake View, SC (29563)	2149
Lamar, SC (29069)	3920
Landrum, SC (29356)	6528
Lane, SC (29564)	749
Latta, SC (29565)	5245
Laurens, SC (29360)	15909
Batesburg, SC (29006)	7015
Leesville, SC (29070)	11980
Lexington, SC (29072)	39334
Lexington, SC (29073)	32155
Liberty, SC (29657)	11688
Little Mountain, SC (29075)	2511
Little River, SC (29566)	13471
Little Rock, SC (29567)	767
Longs, SC (29568)	9099
Loris, SC (29569)	12428
Lugoff, SC (29078)	12901
Lyman, SC (29365)	8460
Lynchburg, SC (29080)	2443
Mc Bee, SC (29101)	2110
Mc Clellanville, SC (29458)	1980
Mc Coll, SC (29570)	2881
Manning, SC (29102)	13344
Marietta, SC (29661)	4357
Marion, SC (29571)	11838
Mauldin, SC (29662)	12247
Mayesville, SC (29104)	1365
Moncks Corner, SC (29461)	23943
Monetta, SC (29105)	1128
Moore, SC (29369)	11521
Mountain Rest, SC (29664)	1212
Mount Pleasant, SC (29464)	36456
Mount Pleasant, SC (29466)	23409
Mountville, SC (29370)	844
Mullins, SC (29574)	8786
Murrells Inlet, SC (29576)	20949
Myrtle Beach, SC (29572)	7182
Myrtle Beach, SC (29575)	13088
Myrtle Beach, SC (29577)	20742
Myrtle Beach, SC (29579)	24336
Myrtle Beach, SC (29588)	29718
Neeses, SC (29107)	2255
Nesmith, SC (29580)	1051
Newberry, SC (29108)	15490
New Zion, SC (29111)	1232
Nichols, SC (29581)	3317
Ninety Six, SC (29666)	5143
Norris, SC (29667)	451
North, SC (29112)	3561
North Myrtle Beach, SC (29582)	11455
Norway, SC (29113)	1238
Olanta, SC (29114)	1635
Orangeburg, SC (29115)	19814
Orangeburg, SC (29118)	11412
Pacolet, SC (29372)	3338
Pamplico, SC (29583)	4058
Patrick, SC (29584)	1833
Pauline, SC (29374)	2939
Pawleys Island, SC (29585)	12435
Pelion, SC (29123)	5619
Pelzer, SC (29669)	9623
Pendleton, SC (29670)	6495
Pickens, SC (29671)	14514
Piedmont, SC (29673)	20014
Pineville, SC (29468)	1447
Pinewood, SC (29125)	2290
Pinopolis, SC (29469)	761
Pomaria, SC (29126)	1895
Prosperity, SC (29127)	7028
Ravenel, SC (29470)	3345
Reevesville, SC (29471)	1193
Rembert, SC (29128)	3657
Ridge Spring, SC (29129)	2206
Ridgeville, SC (29472)	6169
Ridgeway, SC (29130)	4927
Roebuck, SC (29376)	5930
Round O, SC (29474)	1693
Rowesville, SC (29133)	811
Ruffin, SC (29475)	1930
Saint George, SC (29477)	5008
Saint Matthews, SC (29135)	6835
Saint Stephen, SC (29479)	5138
Salem, SC (29676)	4534
Salley, SC (29137)	1753
Salters, SC (29590)	1751
Saluda, SC (29138)	8004
Santee, SC (29142)	3951
Scranton, SC (29591)	3681
Sellers, SC (29592)	866
Seneca, SC (29672)	9293
Seneca, SC (29678)	15201
Silverstreet, SC (29145)	695
Simpsonville, SC (29680)	21575
Simpsonville, SC (29681)	40234
Six Mile, SC (29682)	3061
Smoaks, SC (29481)	1478
Society Hill, SC (29593)	1570
Spartanburg, SC (29301)	23385
Spartanburg, SC (29302)	13069
Spartanburg, SC (29303)	18300
Spartanburg, SC (29306)	10246
Spartanburg, SC (29307)	14016
Boiling Springs, SC (29316)	19403
Springfield, SC (29146)	1297
Starr, SC (29684)	3747
Sullivans Island, SC (29482)	1573
Summerton, SC (29148)	4443
Summerville, SC (29483)	51619
Summerville, SC (29485)	39303
Sumter, SC (29150)	28732
Shaw A F B, SC (29152)	2124
Sumter, SC (29153)	11621
Sumter, SC (29154)	22407
Sunset, SC (29685)	1071
Swansea, SC (29160)	6161
Tamassee, SC (29686)	713
Taylors, SC (29687)	32851
Timmonsville, SC (29161)	8774
Townville, SC (29689)	3152
Travelers Rest, SC (29690)	15487
Turbeville, SC (29162)	1982
Union, SC (29379)	13763
Vance, SC (29163)	1521
Wadmalaw Island, SC (29487)	2171
Wagener, SC (29164)	3414
Walhalla, SC (29691)	8224
Wallace, SC (29596)	1860
Walterboro, SC (29488)	16772
Ward, SC (29166)	751
Ware Shoals, SC (29692)	3718
Waterloo, SC (29384)	3020
Wedgefield, SC (29168)	2511
Wellford, SC (29385)	5656
Westminster, SC (29693)	10909
West Union, SC (29696)	3582
Whitmire, SC (29178)	2523
Williamston, SC (29697)	9672
Winnsboro, SC (29180)	10780
Woodruff, SC (29388)	11048
Acworth, GA (30101)	44804
Acworth, GA (30102)	29964
Adairsville, GA (30103)	11396
Alpharetta, GA (30004)	45452
Alpharetta, GA (30005)	27038
Alpharetta, GA (30009)	9051
Alpharetta, GA (30022)	51463
Alto, GA (30510)	4833
Aragon, GA (30104)	3835
Armuchee, GA (30105)	2263
Arnoldsville, GA (30619)	1225
Athens, GA (30601)	11851
Athens, GA (30605)	21744
Athens, GA (30606)	26938
Athens, GA (30607)	7685
Atlanta, GA (30303)	33905
Atlanta, GA (30305)	19084
Atlanta, GA (30306)	16362
Atlanta, GA (30307)	13838
Atlanta, GA (30308)	10226
Atlanta, GA (30309)	15857
Atlanta, GA (30310)	19613
Atlanta, GA (30311)	24266
Atlanta, GA (30312)	12278
Atlanta, GA (30313)	2783
Atlanta, GA (30314)	11865
Atlanta, GA (30315)	22397
Atlanta, GA (30316)	23221
Atlanta, GA (30317)	9531
Atlanta, GA (30318)	34418
Atlanta, GA (30319)	28448
Atlanta, GA (30324)	18894
Atlanta, GA (30326)	3443
Atlanta, GA (30327)	24665
Atlanta, GA (30328)	25021
Atlanta, GA (30329)	18677
Atlanta, GA (30331)	38527
Atlanta, GA (30336)	1245
Atlanta, GA (30337)	8133
Atlanta, GA (30338)	27642
Atlanta, GA (30339)	58926
Atlanta, GA (30340)	20626
Atlanta, GA (30341)	21075
Atlanta, GA (30342)	22085
Atlanta, GA (30344)	23804
Atlanta, GA (30345)	17952
Atlanta, GA (30346)	3318
Atlanta, GA (30349)	53061
Atlanta, GA (30350)	25506
Atlanta, GA (30354)	10897
Atlanta, GA (30360)	10858
Atlanta, GA (30363)	1505
Auburn, GA (30011)	12240
Austell, GA (30106)	15566
Austell, GA (30168)	18116
Avondale Estates, GA (30002)	4764
Baldwin, GA (30511)	3026
Ball Ground, GA (30107)	10682
Barnesville, GA (30204)	9083
Bethlehem, GA (30620)	9675
Bishop, GA (30621)	3685
Blairsville, GA (30512)	12816
Blue Ridge, GA (30513)	8079
Bogart, GA (30622)	8455
Bowdon, GA (30108)	6056
Bowersville, GA (30516)	1511
Bowman, GA (30624)	2157
Braselton, GA (30517)	9607
Bremen, GA (30110)	9923
Brooks, GA (30205)	2676
Buchanan, GA (30113)	4629
Buckhead, GA (30625)	1840
Buford, GA (30518)	34516
Buford, GA (30519)	31154
Canon, GA (30520)	3251
Canton, GA (30114)	37231
Canton, GA (30115)	28564
Carlton, GA (30627)	1684
Carnesville, GA (30521)	4005
Carrollton, GA (30116)	17606
Carrollton, GA (30117)	22971
Cartersville, GA (30120)	31159
Cartersville, GA (30121)	15766
Cave Spring, GA (30124)	2451
Cedartown, GA (30125)	17531
Cherry Log, GA (30522)	889
Clarkesville, GA (30523)	9883
Clarkston, GA (30021)	15145
Clayton, GA (30525)	6201
Clermont, GA (30527)	3419
Cleveland, GA (30528)	16648
Colbert, GA (30628)	5099
Comer, GA (30629)	3496
Commerce, GA (30529)	8453
Commerce, GA (30530)	4558
Concord, GA (30206)	2292
Conley, GA (30288)	6499
Conyers, GA (30012)	20467
Conyers, GA (30013)	20037
Conyers, GA (30094)	24556
Cornelia, GA (30531)	8704
Covington, GA (30014)	24356
Covington, GA (30016)	38269
Crawford, GA (30630)	1875
Crawfordville, GA (30631)	1233
Cumming, GA (30028)	15653
Cumming, GA (30040)	45130
Cumming, GA (30041)	43444
Dacula, GA (30019)	32732
Dahlonega, GA (30533)	17520
Dallas, GA (30132)	25321
Dallas, GA (30157)	34689
Danielsville, GA (30633)	6332
Dawsonville, GA (30534)	20167
Decatur, GA (30030)	20510
Decatur, GA (30032)	34467
Decatur, GA (30033)	22336
Decatur, GA (30034)	34866
Decatur, GA (30035)	15456
Demorest, GA (30535)	5384
Dewy Rose, GA (30634)	1904
Dillard, GA (30537)	955
Douglasville, GA (30134)	32452
Douglasville, GA (30135)	48247
Duluth, GA (30096)	49623
Duluth, GA (30097)	33363
Eastanollee, GA (30538)	2636
East Ellijay, GA (30539)	1445
Elberton, GA (30635)	12755
Ellenwood, GA (30294)	31079
Ellijay, GA (30536)	5037
Ellijay, GA (30540)	12728
Emerson, GA (30137)	1402
Epworth, GA (30541)	1465
Fairburn, GA (30213)	24200
Fairmount, GA (30139)	3221
Fayetteville, GA (30214)	21060
Fayetteville, GA (30215)	28423
Peachtree City, GA (30269)	31332
Flovilla, GA (30216)	1717
Flowery Branch, GA (30542)	25593
Forest Park, GA (30297)	19587
Franklin, GA (30217)	6520
Gainesville, GA (30501)	18767
Gainesville, GA (30504)	17167
Gainesville, GA (30506)	32865
Gainesville, GA (30507)	20209
Gay, GA (30218)	1707
Gillsville, GA (30543)	3456
Good Hope, GA (30641)	1310
Grantville, GA (30220)	4046
Grayson, GA (30017)	16626
Greensboro, GA (30642)	8748
Greenville, GA (30222)	3292
Griffin, GA (30223)	26236
Griffin, GA (30224)	19652
Hampton, GA (30228)	28888
Hartwell, GA (30643)	12472
Helen, GA (30545)	979
Hiawassee, GA (30546)	5420
Hiram, GA (30141)	17960
Hogansville, GA (30230)	6391
Homer, GA (30547)	2761
Hoschton, GA (30548)	13040
Hull, GA (30646)	5443
Jackson, GA (30233)	17221
Jasper, GA (30143)	17843
Jefferson, GA (30549)	16926
Jenkinsburg, GA (30234)	1643
Jonesboro, GA (30236)	35416
Jonesboro, GA (30238)	27283
Kennesaw, GA (30144)	38067
Kennesaw, GA (30152)	33285
Kingston, GA (30145)	6306
Lagrange, GA (30240)	22278
Lagrange, GA (30241)	18185
Lakemont, GA (30552)	1137
Lavonia, GA (30553)	5837
Lawrenceville, GA (30043)	61947
Lawrenceville, GA (30044)	63934
Lawrenceville, GA (30045)	50810
Lawrenceville, GA (30046)	2772
Lexington, GA (30648)	2295
Lilburn, GA (30047)	48371
Lindale, GA (30147)	3484
Lithia Springs, GA (30122)	16833
Lithonia, GA (30038)	27454
Lithonia, GA (30058)	39848
Locust Grove, GA (30248)	18286
Loganville, GA (30052)	48549
Lula, GA (30554)	6043
Luthersville, GA (30251)	1916
Mc Caysville, GA (30555)	1807
Mcdonough, GA (30252)	32305
Mcdonough, GA (30253)	39530
Mableton, GA (30126)	29224
Madison, GA (30650)	10026
Mansfield, GA (30055)	2567
Marble Hill, GA (30148)	639
Marietta, GA (30008)	20427
Marietta, GA (30060)	23627
Marietta, GA (30062)	53468
Marietta, GA (30064)	37766
Marietta, GA (30066)	46080
Marietta, GA (30067)	33810
Marietta, GA (30068)	28538
Martin, GA (30557)	3777
Maysville, GA (30558)	4032
Meansville, GA (30256)	2180
Milner, GA (30257)	3333
Mineral Bluff, GA (30559)	3019
Molena, GA (30258)	1930
Monroe, GA (30655)	18109
Monroe, GA (30656)	12039
Moreland, GA (30259)	2576
Morganton, GA (30560)	3290
Morrow, GA (30260)	18588
Mount Airy, GA (30563)	4196
Murrayville, GA (30564)	3798
Newborn, GA (30056)	2104
Newnan, GA (30263)	41478
Newnan, GA (30265)	25560
Nicholson, GA (30565)	3830
Norcross, GA (30071)	17175
Norcross, GA (30092)	27101
Norcross, GA (30093)	32902
Oakwood, GA (30566)	6624
Oxford, GA (30054)	9519
Palmetto, GA (30268)	7252
Pendergrass, GA (30567)	2551
Powder Springs, GA (30127)	48326
Rabun Gap, GA (30568)	1511
Rayle, GA (30660)	815
Rex, GA (30273)	12398
Riverdale, GA (30274)	24347
Riverdale, GA (30296)	22048
Rockmart, GA (30153)	13703
Rome, GA (30161)	24576
Rome, GA (30165)	28535
Roopville, GA (30170)	2372
Roswell, GA (30075)	44807
Roswell, GA (30076)	34455
Royston, GA (30662)	6217
Rutledge, GA (30663)	2372
Rydal, GA (30171)	2739
Sautee Nacoochee, GA (30571)	2294
Scottdale, GA (30079)	2558
Senoia, GA (30276)	11150
Sharpsburg, GA (30277)	17054
Silver Creek, GA (30173)	5414
Smyrna, GA (30080)	37216
Smyrna, GA (30082)	20747
Snellville, GA (30039)	33328
Snellville, GA (30078)	27489
Social Circle, GA (30025)	7568
Statham, GA (30666)	6422
Stephens, GA (30667)	589
Stockbridge, GA (30281)	51336
Stone Mountain, GA (30083)	39661
Stone Mountain, GA (30087)	30003
Stone Mountain, GA (30088)	19487
Suches, GA (30572)	868
Suwanee, GA (30024)	55195
Talking Rock, GA (30175)	4487
Tallapoosa, GA (30176)	5269
Talmo, GA (30575)	1316
Tate, GA (30177)	643
Taylorsville, GA (30178)	3091
Temple, GA (30179)	13219
The Rock, GA (30285)	634
Thomaston, GA (30286)	17636
Tiger, GA (30576)	1911
Tignall, GA (30668)	1368
Toccoa, GA (30577)	16693
Tucker, GA (30084)	28906
Tyrone, GA (30290)	7212
Union City, GA (30291)	15038
Union Point, GA (30669)	2476
Villa Rica, GA (30180)	26821
Waco, GA (30182)	2084
Waleska, GA (30183)	4162
Washington, GA (30673)	5956
Watkinsville, GA (30677)	14161
White, GA (30184)	5508
White Plains, GA (30678)	964
Whitesburg, GA (30185)	3108
Williamson, GA (30292)	4640
Winder, GA (30680)	29471
Winston, GA (30187)	7398
Winterville, GA (30683)	5562
Woodbury, GA (30293)	2377
Woodstock, GA (30188)	43717
Woodstock, GA (30189)	30483
Young Harris, GA (30582)	3420
Zebulon, GA (30295)	3582"""

import random, sys

def helper():
    print """The cityPicker use cases are:\n python cityPicker.py\n\t(if you have no constraints)\n python cityPicker.py [optional max. city size]\n\t(if you have an upper bound), or \n python cityPicker.py [opt. max. city size] [opt. min. city size]\n\t(if you have upper and lower bound constraints)
For reference, the percentiles of city-size are
\t10%:  780 (one in ten cities have fewer than 780 residents)
\t20%:  1205
\t30%:  1798
\t40%:  2713
\t50%:  4249
\t60%:  6900
\t70%:  11193
\t80%:  17389
\t90%:  25680
\t100%: 88503 (all cities have at most 88503 residents)"""

if len(sys.argv) == 1:
    mn = 0
    mx = 3000000
elif len(sys.argv) == 2:
    try:
        mx = int(sys.argv[1])
    except:
        print "WOAH! Gotta give me an integer as an upper bound argument, not THAT nonsense."
        helper()
        sys.exit(0)
    mn = 0
elif len(sys.argv) == 3:
    try:
        mn = int(sys.argv[2])
    except:
        print "WOAH! Gotta give me an integer as a lower bound argument, not THAT nonsense."
        helper()
        sys.exit(0)
    try:
        mx = int(sys.argv[1])
    except:
        print "WOAH! Gotta give me an integer as an upper bound argument, not THAT nonsense."
        helper()
        sys.exit(0)
else:
    print "Sorry, you've given me an inappropriate number of arguments."
    helper()
    sys.exit(0)
    
N = 0
tups = []
lines = zipdata.split('\n')
for line in lines:
    spline = line.split('\t')
    city = spline[0].strip()
    pop = int(spline[1])
    if pop < mn or pop > mx:
        continue
    tup = (city,pop)
    N += pop
    tups.append(tup)

val = random.random()*N
s = 0
flag = True
for tup in tups:
    s+=tup[1]
    if s > val:
        print tup[0], '\t', tup[1]
        flag = False
        break
if flag:
    print "Sorry, couldn't find a city that meets your constraints."
