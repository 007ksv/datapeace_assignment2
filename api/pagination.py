from rest_framework import pagination


'''
	Defining CustomPagination Class so that we can define default page_size
	and changing the default 'page_size' query_param to 'limit'.
'''


class CustomPaginationClass(pagination.PageNumberPagination):
	page_size = 5																				# default page size
	page_size_query_param = 'limit'														# limit the content shows per page