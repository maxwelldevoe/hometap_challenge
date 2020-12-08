from flask import Flask, jsonify, request
from data import PROPERTIES

app = Flask(__name__)

@app.route('/', methods=["GET"])
def septic_check():
    """
    Endpoint to determine if given address has a septic system.
    Args:
        address (string) - Home Address
        zip (int) - Zip Code
    Returns:
        Boolean
    """

    request_params = request.args.to_dict()

    """
    address and zip are required params for the housecanary API so we need to validate
    those params before making the request
    """
    if "address" not in request_params.keys():

        """
        normally we would have a logger set up here which would log the keyerror and return
        but in this case, return the missing param message
        """

        return jsonify({"response": "Missing required parameter: address"})
    elif "zip" not in request_params.keys():
        return jsonify({"response": "Missing required parameter: zip"})
    
    """
    since we can't actually hit the housecanary API, we'll pretend
    response = requests.get(f"https://api.housecanary.com/v2/property/details?address={request_params["address"]}&zipcode={request_params["zip"]}", headers={"api_key": "fkjdfkd_4555jfdsd"})
    """

    current_property = {}
    # use mock data
    for house in PROPERTIES:
        if request_params["address"].lower() == house["address"].lower():
            current_property = house
            break

    if "sewer" not in current_property["property/details"]["result"]["property"]:
        return jsonify({"response": "API did not return sewer property"})
    elif current_property["property/details"]["result"]["property"]["sewer"] == "septic":
        return jsonify({
            "address": current_property["address"],
            "septic": True
        })
    else:
        return jsonify({
            "address": current_property["address"],
            "septic": False
        })
    

    return jsonify(request_params)


if __name__ == '__main__':
    app.run(debug=True)