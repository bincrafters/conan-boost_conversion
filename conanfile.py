#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.68.0@bincrafters/stable")

class BoostConversionConan(base.BoostBaseConan):
    name = "boost_conversion"
    url = "https://github.com/bincrafters/conan-boost_conversion"
    lib_short_names = ["conversion"]
    header_only_libs = ["conversion"]
    b2_requires = [
        "boost_assert",
        "boost_config",
        "boost_smart_ptr",
        "boost_throw_exception",
        "boost_type_traits",
        "boost_typeof"
    ]
