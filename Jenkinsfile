stage("Build and Publish") {
    // such as d2l-en and d2l-zh
  def REPO_NAME = env.JOB_NAME.split('/')[0]
    // such as en and zh
  def LANG = REPO_NAME.split('-')[1]
    // The current branch or the branch this PR will merge into
  def TARGET_BRANCH = env.CHANGE_TARGET ? env.CHANGE_TARGET : env.BRANCH_NAME
  // such as d2l-en-master
  def TASK = REPO_NAME + '-' + TARGET_BRANCH
  node {
    ws("workspace/${TASK}") {
      checkout scm
      // conda environment
      def ENV_NAME = "${TASK}-${EXECUTOR_NUMBER}";
      // assign two GPUs to each build
      def EID = EXECUTOR_NUMBER.toInteger()
      def CUDA_VISIBLE_DEVICES=(EID*2).toString() + ',' + (EID*2+1).toString();

      sh label: "Build Environment", script: """set -ex
      conda env update -n ${ENV_NAME} -f static/build.yml
      conda activate ${ENV_NAME}
      pip list
      nvidia-smi
      """

      sh label: "Sanity Check", script: """set -ex
      conda activate ${ENV_NAME}
      d2lbook build outputcheck tabcheck
      """


      pip install gluoncv --pre
      pip install mxnet-cu101
      pip install git+https://github.com/d2l-ai/d2l-book
      python setup.py develop
      pip list
      """

      sh label: "Check Execution Output", script: """set -ex
      conda activate ${ENV_NAME}
      d2lbook build outputcheck
      """

      sh label: "Execute Notebooks", script: """set -ex
      conda activate ${ENV_NAME}
      export CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES}
      export LD_LIBRARY_PATH=/usr/local/cuda-10.1/lib64
      d2lbook build eval
      """

      sh label:"Build HTML", script:"""set -ex
      conda activate ${ENV_NAME}
      d2lbook build html
      """

      sh label:"Build PDF", script:"""set -ex
      conda activate ${ENV_NAME}
      which rsvg-convert
      rsvg-convert --version
      # d2lbook build pdf
      """

      sh label:"Build Package", script:"""set -ex
      conda activate ${ENV_NAME}
      """

      if (env.BRANCH_NAME == 'master') {
        sh label:"Publish", script:"""set -ex
        conda activate ${ENV_NAME}
        d2lbook deploy html # pkg pdf
      """
      }
	}
  }
}
