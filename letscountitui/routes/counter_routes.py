"""Routes for counters"""

from flask import Blueprint, redirect, render_template, request, url_for

from letscountitui.utilities.utils import DataRetrieval

bp = Blueprint("counter", __name__, url_prefix="/counters")


@bp.route("/")
def list_counters():
    """List all counters"""
    data_retrieval = DataRetrieval()
    counters = data_retrieval.get_data()
    return render_template(
        "counter/list_counters.html",
        counters=counters,
        url_create_counter=url_for("counter.list_counters"),
    )


@bp.route("/<counter_id>")
def show_counter(counter_id):
    """Show a specific counter"""
    data_retrieval = DataRetrieval()
    counters = data_retrieval.get_data()
    counter = [c for c in counters if c["uuid"] == counter_id][0]
    return render_template("counter/show_counter.html", counter=counter)


@bp.route("/decrease/<counter_id>")
def decrease_counter(counter_id):
    """Decrease a specific counter"""
    data_retrieval = DataRetrieval()
    data_retrieval.decrease_counter(counter_id)
    return redirect(url_for("counter.show_counter", counter_id=counter_id))


@bp.route("/increase/<counter_id>")
def increase_counter(counter_id):
    """Increase a specific counter"""
    data_retrieval = DataRetrieval()
    data_retrieval.increase_counter(counter_id)
    return redirect(url_for("counter.show_counter", counter_id=counter_id))


@bp.route("/update/<counter_id>", methods=["POST"])
def update_counter(counter_id: str):
    """Update a counter"""
    new_count = request.form["new_count"]
    data_retrieval = DataRetrieval()
    data_retrieval.update_counter(counter_id, new_count)
    counter_data = data_retrieval.get_data()
    counter = [c for c in counter_data if c["uuid"] == counter_id]
    the_counter = counter[0]
    return render_template("counter/one_counter.html", counter=the_counter)


@bp.route("/create", methods=["POST", "GET"])
def create_counter():
    """Create a counter"""
    if request.method == "GET":
        return render_template("counter/create_counter.html")
    name = request.form["name"]
    initial_count = request.form["initial_value"]
    data_retrieval = DataRetrieval()
    counter_creation = data_retrieval.create_counter(name, initial_count)
    return redirect(
        url_for("counter.show_counter", counter_id=counter_creation["uuid"])
    )
