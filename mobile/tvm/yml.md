      - name: Build and Install TVM
        if: matrix.os == 'ubuntu-latest'
        run: |
          git clone https://github.com/apache/incubator-tvm tvm --recursive
          cd tvm
          mkdir -p build
          cp cmake/config.cmake build
          echo set\(USE_LLVM ON\) >> build/config.cmake
          echo set\(USE_GRAPH_RUNTIME ON\) >> build/config.cmake
          echo set\(USE_BLAS openblas\) >> build/config.cmake
          cd build
          cmake .. -G Ninja
          ninja
          cd ../python
          python -m pip install -U -e .

https://github.com/szha/gluon-nlp/blob/master/.github/workflows/unittests.yml
