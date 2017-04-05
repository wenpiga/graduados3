def vista(request, *args, **kwargs):
	response = f(request, *args, **kwargs)
	result = StringIO.StringIO()
	pdf = pisa.pisaDocument(StringIO.StringIO(response.encode("UTF-8")), result)
	if not pdf.err:
		response = HttpResponse(result.getvalue(), mimetype='application/pdf')
		return response
		return HttpResponse('Error al generar el PDF: %s' % cgi.escape(response))
	return vista