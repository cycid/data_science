from flask import Flask, jsonify, request
from data_module import Data as data





app=Flask(__name__)
my_data=data()




@app.route('/api/last_10_records', methods=['GET'])
def get_records():
	answer={'last 10 added records': my_data.get()}
	return jsonify(answer)


	


@app.route('/api/add_record', methods=['POST'])
def add_record():
	print('something')
	record = request.json
	print(record)
	my_data.add(record)	
	return jsonify({'New added record': record})
	

	


@app.route('/api/delete_record', methods=["DELETE"])
def delete_record():	
	record = request.json
	my_data.delete(record['id'])	
	return jsonify({'Removed record' : record})




if __name__=='__main__':
	app.run(host='0.0.0.0', port='5000')
