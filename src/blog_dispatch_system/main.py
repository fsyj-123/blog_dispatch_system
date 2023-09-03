from flask import Flask, request, jsonify

from blog_dispatch_system.log import init_log
from blog_dispatch_system.scheduler import BlogScheduler
from blog_dispatch_system.plugins import plugin_factory

app = Flask(__name__)
init_log()


@app.route('/publish', methods=['POST'])
def publish_blog():
    data = request.get_json()
    if 'blog_content' not in data or 'platforms' not in data:
        return jsonify({"error": "Invalid input data"}), 400

    blog_content = data['blog_content']
    platforms = data['platforms']
    kwargs = data['kwargs']

    if not platforms:
        return jsonify({"error": "No platforms specified"}), 400

    platform_plugins = plugin_factory.load_plugins(platforms, **kwargs)
    # 调度发布博客到指定平台
    BlogScheduler.schedule_publish(platform_plugins, blog_content)

    return jsonify({"message": "Blog published successfully"}), 200


if __name__ == '__main__':
    app.run(debug=True, port=5001)
