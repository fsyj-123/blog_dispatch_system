from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

filter_script = """
let tags = arguments[0]
let prefixes = arguments[1]

const selectedElems = []
tags.forEach((tag) => {
  const attributes = tag.attributes;
  let prefix_has = new Array(prefixes.length)
    prefix_has.fill(false)
  // 检查每个属性是否包含data-v-
  for (let i = 0; i < attributes.length; i++) {
    const attributeName = attributes[i].name;
      for (let j = 0; j < prefixes.length; j++) {
          if (!prefix_has[j] && attributeName.startsWith(prefixes[j])) {
              prefix_has[j] = true
              break
          }
      }
  }
  if (prefix_has.every((element) => element === true)) {
      selectedElems.push(tag)
  }
});
return selectedElems;
"""


def find_tag_prefix(tag: str, prefix: list, driver: WebDriver) -> list:
    tags = driver.find_elements(By.TAG_NAME, tag)
    return driver.execute_script(filter_script, tags, prefix)
